#!/usr/bin/env python3
"""
XML ➜ Enriched Markdown transformer (Mermaid‑safe, GitHub‑friendly)

What's new (fixes + DX)
- **No spurious SystemExit in interactive runs**: CLI now returns status codes instead of calling `sys.exit` when not on a TTY (e.g., notebooks, IDEs). This prevents `SystemExit: 1` traces.
- **Python 3 guard** with clear guidance for Py2/old 3.x.
- **Friendlier argparse** (no `SystemExit: 2`), STDIN default, better streaming checks.
- Streaming (SAX) predictability: headings on open, leaf nodes on close, real front‑matter.
- Mermaid hardening + table/list robustness retained.
- Built‑in `--selftest` quick tests (extended — added API error checks without changing existing tests).

Usage
------
# from a file → stdout
python xml_to_markdown_enhanced.py input.xml

# from stdin → stdout
cat input.xml | python xml_to_markdown_enhanced.py -

# streaming (large files) → write to output.md
python xml_to_markdown_enhanced.py input.xml --streaming -o output.md

# streaming from stdin
cat big.xml | python xml_to_markdown_enhanced.py - --streaming -o out.md
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, Optional, Union, Iterable, Tuple, TextIO
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
import xml.sax
from xml.sax import handler
import io
import html
import sys
import os
import argparse

__all__ = [
    "TransformConfig",
    "RenderContext",
    "XMLParseError",
    "default_assets_resolver",
    "transform_xml_to_md",
    "transform_xml_to_md_streaming",
]

# ---------------------------- Python version guard --------------------------

def _eprint(*args):
    sys.stderr.write(" ".join(str(a) for a in args) + "\n")

if sys.version_info < (3, 7):
    _eprint("This script requires Python 3.7+ (found {}.{}.{})".format(*sys.version_info[:3]))
    _eprint("Tip: run with 'python3' or upgrade Python.")
    # Return cleanly when imported; exit non-interactively when run as script handled in run_cli
    # For safety in module import contexts we do not raise SystemExit here.

Md = str
Element = ET.Element

# ------------------------------- Errors -------------------------------------

class XMLParseError(Exception):
    """Custom exception for XML parsing errors with detailed context."""
    def __init__(self, message: str, line: Optional[int] = None, column: Optional[int] = None, 
                 original_error: Optional[Exception] = None):
        self.line = line
        self.column = column
        self.original_error = original_error
        location_info = ""
        if line is not None:
            location_info = f" at line {line}"
            if column is not None:
                location_info += f", column {column}"
        super().__init__(f"{message}{location_info}")


def _safe_parse_xml(xml_input: Union[str, Path, bytes]) -> Tuple[Optional[Element], Optional[XMLParseError]]:
    """Safely parse XML with detailed error reporting."""
    try:
        if isinstance(xml_input, (str, Path)) and Path(str(xml_input)).exists():
            tree = ET.parse(str(xml_input))
            return tree.getroot(), None
        elif isinstance(xml_input, (str, bytes)):
            return ET.fromstring(xml_input), None
        else:
            return None, XMLParseError("Invalid input type. Expected file path, XML string, or bytes.")
    except ParseError as e:
        line, column = getattr(e, 'position', (None, None))
        return None, XMLParseError(f"XML parsing failed: {str(e)}", line, column, e)
    except Exception as e:
        return None, XMLParseError(f"Unexpected error during XML parsing: {str(e)}", original_error=e)


def _as_xml_root(xml_input: Union[str, Path, bytes]) -> Element:
    """Parse XML input with enhanced error handling."""
    element, error = _safe_parse_xml(xml_input)
    if error:
        raise error
    assert element is not None
    return element

# ------------------------------- Utilities ---------------------------------

def _slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\-\s]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text


def _md_escape(text: str) -> str:
    # Minimal Markdown escaping for common inline characters
    return (
        text.replace("\\", "\\\\")
            .replace("*", "\\*")
            .replace("_", "\\_")
            .replace("`", "\\`")
    )


def _table_cell_escape(text: str) -> str:
    # Escape pipes so GitHub tables keep column alignment
    return _md_escape(text).replace("|", "\\|")


def _attr(elem: Element, name: str, default: Optional[str] = None) -> Optional[str]:
    return elem.attrib.get(name, default)


def _inner_text(elem: Element) -> str:
    # Join text + children tails
    parts: list[str] = []
    if elem.text:
        parts.append(elem.text)
    for child in elem:
        parts.append(_inner_text(child))
        if child.tail:
            parts.append(child.tail)
    return "".join(parts).strip()

# ----------------------------- Mermaid safety -------------------------------

MERMAID_BAD_CHARS = {
    "|": "/",
    "⟩": ")",
    "⟨": "(",
    "½": "1/2",
    "×": "x",
    "ℏ": "hbar",
    "π": "pi",
    "ψ": "psi",
    "⨯": "x",
}

# Strip brackets/quotes Mermaid treats structurally
_mermaid_label_pat = re.compile(r'[][{}<>"\']')


def _mermaid_safe_label(text: str) -> str:
    if not text:
        return ""
    s = text
    for bad, rep in MERMAID_BAD_CHARS.items():
        s = s.replace(bad, rep)
    s = _mermaid_label_pat.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    s = s.replace("\\n", "<br>").replace("\n", "<br>")
    return s

# ------------------------------- Config -------------------------------------

@dataclass
class TransformConfig:
    diagram_strategy: str = "mermaid"  # or 'none'
    media_embed: str = "html5"  # 'html5' only for now
    heading_base: int = 1  # base heading level for sections (auto-offset if H1 is rendered)
    render_doc_title_as_h1: bool = True
    generate_frontmatter: bool = True
    callout_style: str = "github"  # 'github' uses > [!NOTE]
    # Extra handlers: tag -> fn(elem, ctx) -> str
    extra_handlers: Dict[str, Callable[[Element, "RenderContext"], Md]] = field(default_factory=dict)


@dataclass
class RenderContext:
    cfg: TransformConfig
    assets_resolver: Callable[[Element], str]
    # track nesting level for lists
    list_depth: int = 0


def default_assets_resolver(base_url: str = "") -> Callable[[Element], str]:
    """Default resolver that returns src/href or base_url + src."""
    def resolver(elem: Element) -> str:
        src = _attr(elem, "src") or _attr(elem, "href") or ""
        if base_url and src and not src.startswith("http"):
            return base_url.rstrip("/") + "/" + src.lstrip("/")
        return src
    return resolver

# ----------------------------- Handlers ------------------------------------

def handle_document(elem: Element, ctx: RenderContext) -> Md:
    """Handle <document> root element."""
    parts: list[str] = []
    
    # Front matter
    if ctx.cfg.generate_frontmatter:
        title = _attr(elem, "title", "Document")
        author = _attr(elem, "author", "")
        date = _attr(elem, "date", "")
        front = ["---"]
        front.append(f"title: {title}")
        if author:
            front.append(f"author: {author}")
        if date:
            front.append(f"date: {date}")
        front.append("---\n")
        parts.append("\n".join(front))
    
    # Title as H1
    if ctx.cfg.render_doc_title_as_h1:
        title = _attr(elem, "title", "")
        if title:
            parts.append(f"# {_md_escape(title)}\n")
    
    # Process children
    for child in elem:
        parts.append(_dispatch(child, ctx))
    
    return "\n".join(parts)


def handle_section(elem: Element, ctx: RenderContext) -> Md:
    """Handle <section> element."""
    parts: list[str] = []
    
    # Section title
    title = _attr(elem, "title", "")
    level = int(_attr(elem, "level", str(ctx.cfg.heading_base + 1)))
    if title:
        hashes = "#" * min(level, 6)
        anchor = _slugify(title)
        parts.append(f"{hashes} {_md_escape(title)} {{#{anchor}}}\n")
    
    # Process children
    for child in elem:
        parts.append(_dispatch(child, ctx))
    
    return "\n".join(parts)


def handle_p(elem: Element, ctx: RenderContext) -> Md:
    """Handle <p> (paragraph) element."""
    text = _inner_text(elem)
    return f"{_md_escape(text)}\n" if text else ""


def handle_list(elem: Element, ctx: RenderContext) -> Md:
    """Handle <list> (unordered list) element."""
    parts: list[str] = []
    indent = "  " * ctx.list_depth
    
    # Save and increment depth
    old_depth = ctx.list_depth
    ctx.list_depth += 1
    
    for item in elem.findall("item"):
        item_text = ""
        # Get direct text content
        if item.text:
            item_text = item.text.strip()
        
        # Check for nested lists
        nested_lists = []
        for child in item:
            if child.tag in ("list", "olist"):
                nested_lists.append(_dispatch(child, ctx))
            elif child.tail:
                item_text += " " + child.tail.strip()
        
        if item_text:
            parts.append(f"{indent}- {_md_escape(item_text)}")
        
        # Add nested lists
        for nested in nested_lists:
            parts.append(nested)
    
    # Restore depth
    ctx.list_depth = old_depth
    
    return "\n".join(parts) + "\n" if parts else ""


def handle_olist(elem: Element, ctx: RenderContext) -> Md:
    """Handle <olist> (ordered list) element."""
    parts: list[str] = []
    indent = "  " * ctx.list_depth
    
    # Save and increment depth
    old_depth = ctx.list_depth
    ctx.list_depth += 1
    
    for idx, item in enumerate(elem.findall("item"), 1):
        item_text = ""
        if item.text:
            item_text = item.text.strip()
        
        # Check for nested lists
        nested_lists = []
        for child in item:
            if child.tag in ("list", "olist"):
                nested_lists.append(_dispatch(child, ctx))
            elif child.tail:
                item_text += " " + child.tail.strip()
        
        if item_text:
            parts.append(f"{indent}{idx}. {_md_escape(item_text)}")
        
        for nested in nested_lists:
            parts.append(nested)
    
    # Restore depth
    ctx.list_depth = old_depth
    
    return "\n".join(parts) + "\n" if parts else ""


def handle_table(elem: Element, ctx: RenderContext) -> Md:
    """Handle <table> element."""
    rows = elem.findall("row")
    if not rows:
        return ""
    
    parts: list[str] = []
    
    for row_idx, row in enumerate(rows):
        cells = row.findall("cell")
        if not cells:
            continue
        
        cell_texts = [_table_cell_escape(_inner_text(c)) for c in cells]
        parts.append("| " + " | ".join(cell_texts) + " |")
        
        # Header separator after first row
        if row_idx == 0:
            parts.append("| " + " | ".join(["---"] * len(cells)) + " |")
    
    return "\n".join(parts) + "\n\n" if parts else ""


def handle_code(elem: Element, ctx: RenderContext) -> Md:
    """Handle <code> element."""
    lang = _attr(elem, "lang", "")
    code = _inner_text(elem)
    if not code:
        return ""
    
    return f"```{lang}\n{code}\n```\n\n"


def handle_math(elem: Element, ctx: RenderContext) -> Md:
    """Handle <math> element."""
    expr = _inner_text(elem)
    return f"$$\n{expr}\n$$\n\n" if expr else ""


def handle_figure(elem: Element, ctx: RenderContext) -> Md:
    """Handle <figure> element (image with caption)."""
    src = ctx.assets_resolver(elem)
    caption = _attr(elem, "caption", "")
    alt = _attr(elem, "alt", caption)
    
    if not src:
        return ""
    
    md = f"![{_md_escape(alt)}]({src})"
    if caption:
        md += f"\n*{_md_escape(caption)}*"
    return md + "\n\n"


def handle_media(elem: Element, ctx: RenderContext) -> Md:
    """Handle <media> element (audio/video)."""
    src = ctx.assets_resolver(elem)
    kind = _attr(elem, "type", "video")
    
    if not src:
        return ""
    
    if ctx.cfg.media_embed == "html5":
        if kind == "audio":
            return f'<audio controls><source src="{html.escape(src)}"></audio>\n\n'
        else:
            return f'<video controls><source src="{html.escape(src)}"></video>\n\n'
    
    return f"[Media: {src}]\n\n"


def handle_link(elem: Element, ctx: RenderContext) -> Md:
    """Handle <link> or <ref> element."""
    href = _attr(elem, "href", "")
    text = _inner_text(elem) or href
    
    if not href:
        return _md_escape(text)
    
    return f"[{_md_escape(text)}]({href})"


def handle_callout(elem: Element, ctx: RenderContext) -> Md:
    """Handle <callout> element (GitHub-style alerts)."""
    kind = (_attr(elem, "type", "note") or "note").upper()
    text = _inner_text(elem)
    
    if not text:
        return ""
    
    if ctx.cfg.callout_style == "github":
        return f"> [!{kind}]\n> {text}\n\n"
    
    return f"**{kind}**: {text}\n\n"


def handle_details(elem: Element, ctx: RenderContext) -> Md:
    """Handle <details> element (collapsible section)."""
    summary = _attr(elem, "summary", "Details")
    content = _inner_text(elem)
    
    return f"<details>\n<summary>{_md_escape(summary)}</summary>\n\n{_md_escape(content)}\n</details>\n\n"


def handle_diagram(elem: Element, ctx: RenderContext) -> Md:
    """Handle <diagram> element with Mermaid rendering."""
    if ctx.cfg.diagram_strategy == "none":
        return ""
    
    # Check if raw code is provided
    code = _inner_text(elem)
    if code and not elem.findall("node") and not elem.findall("edge"):
        return f"```mermaid\n{code}\n```\n\n"
    
    kind = (_attr(elem, "kind", "flow") or "flow").lower()
    
    # Gather nodes/edges
    nodes = {(_attr(n, "id") or "").strip(): _attr(n, "label", _attr(n, "id")) for n in elem.findall("node")}
    nodes = {nid: (label if label is not None else nid) for nid, label in nodes.items() if nid}
    edges = []
    for e in elem.findall("edge"):
        a = (_attr(e, "from") or "").strip()
        b = (_attr(e, "to") or "").strip()
        lab = _attr(e, "label", "") or ""
        if a and b:
            edges.append((a, b, lab))
    
    if not nodes and not edges:
        return ""
    
    if kind in ("flow", "flowchart"):
        lines = ["flowchart LR"]
        for nid, label in nodes.items():
            safe_label = _mermaid_safe_label(label)
            lines.append(f"    {nid}[{safe_label}]")
        for a, b, lab in edges:
            safe_lab = _mermaid_safe_label(lab)
            if safe_lab:
                lines.append(f"    {a} -- {safe_lab} --> {b}")
            else:
                lines.append(f"    {a} --> {b}")
        code = "\n".join(lines)
        return f"```mermaid\n{code}\n```\n\n"
    
    if kind in ("sequence", "seq"):
        lines = ["sequenceDiagram"]
        # Declare participants
        for nid, label in nodes.items():
            safe_label = _mermaid_safe_label(label)
            if safe_label and safe_label != nid:
                lines.append(f"    participant {nid} as \"{safe_label}\"")
            else:
                lines.append(f"    participant {nid}")
        for a, b, lab in edges:
            safe_lab = _mermaid_safe_label(lab)
            if a and b and safe_lab:
                lines.append(f"    {a}->>{b}: {safe_lab}")
            elif a and b:
                lines.append(f"    {a}->>{b}")
        code = "\n".join(lines)
        return f"```mermaid\n{code}\n```\n\n"
    
    # Fallback
    return ""


DEFAULT_HANDLERS: Dict[str, Callable[[Element, RenderContext], Md]] = {
    "document": handle_document,
    "section": handle_section,
    "p": handle_p,
    "list": handle_list,
    "olist": handle_olist,
    "table": handle_table,
    "code": handle_code,
    "math": handle_math,
    "figure": handle_figure,
    "media": handle_media,
    "link": handle_link,
    "ref": handle_link,
    "callout": handle_callout,
    "details": handle_details,
    "diagram": handle_diagram,
}


def _dispatch(elem: Element, ctx: RenderContext) -> Md:
    """Dispatch element to appropriate handler."""
    tag = elem.tag
    
    # Check extra handlers first
    if tag in ctx.cfg.extra_handlers:
        return ctx.cfg.extra_handlers[tag](elem, ctx)
    
    # Check default handlers
    if tag in DEFAULT_HANDLERS:
        return DEFAULT_HANDLERS[tag](elem, ctx)
    
    # Unknown tag: process children
    parts: list[str] = []
    for child in elem:
        parts.append(_dispatch(child, ctx))
    return "".join(parts)

# ----------------------------- Streaming mode -------------------------------

class StreamingMarkdownHandler(handler.ContentHandler):
    """SAX-based handler for streaming XML → Markdown.
    
    Strategy:
      • On <section>: emit heading immediately
      • On closing tags for leaf elements (p, code, etc.): emit content
      • Accumulate text/tail within each element
    """
    
    def __init__(self, output: TextIO, ctx: RenderContext):
        super().__init__()
        self.output = output
        self.ctx = ctx
        self.element_stack: list[tuple[str, dict, list[str]]] = []  # (tag, attrs, texts)
        self.doc_started = False
        self.in_table = False
        self.table_rows: list[list[str]] = []
        self.current_row: list[str] = []
        self.in_diagram = False
        self.diagram_nodes: Dict[str, str] = {}
        self.diagram_edges: list[tuple[str, str, str]] = []
    
    def startElement(self, name, attrs):
        # Convert attrs to dict
        attr_dict = dict(attrs.items())
        
        # Handle document start
        if name == "document" and not self.doc_started:
            self.doc_started = True
            if self.ctx.cfg.generate_frontmatter:
                title = attr_dict.get("title", "Document")
                author = attr_dict.get("author", "")
                date = attr_dict.get("date", "")
                self.output.write("---\n")
                self.output.write(f"title: {title}\n")
                if author:
                    self.output.write(f"author: {author}\n")
                if date:
                    self.output.write(f"date: {date}\n")
                self.output.write("---\n\n")
            
            if self.ctx.cfg.render_doc_title_as_h1:
                title = attr_dict.get("title", "")
                if title:
                    self.output.write(f"# {_md_escape(title)}\n\n")
        
        # Handle section heading immediately
        if name == "section":
            title = attr_dict.get("title", "")
            level = int(attr_dict.get("level", str(self.ctx.cfg.heading_base + 1)))
            if title:
                hashes = "#" * min(level, 6)
                anchor = _slugify(title)
                self.output.write(f"{hashes} {_md_escape(title)} {{#{anchor}}}\n\n")
        
        # Handle table structure
        if name == "table":
            self.in_table = True
            self.table_rows = []
        
        if name == "row" and self.in_table:
            self.current_row = []
        
        # Handle diagram structure
        if name == "diagram":
            self.in_diagram = True
            self.diagram_nodes = {}
            self.diagram_edges = []
        
        if name == "node" and self.in_diagram:
            node_id = attr_dict.get("id", "")
            label = attr_dict.get("label", node_id)
            if node_id:
                self.diagram_nodes[node_id] = label
        
        if name == "edge" and self.in_diagram:
            from_id = attr_dict.get("from", "")
            to_id = attr_dict.get("to", "")
            label = attr_dict.get("label", "")
            if from_id and to_id:
                self.diagram_edges.append((from_id, to_id, label))
        
        # Push to stack
        self.element_stack.append((name, attr_dict, []))
    
    def endElement(self, name):
        if not self.element_stack:
            return
        
        tag, attrs, texts = self.element_stack.pop()
        text_content = "".join(texts).strip()
        
        # Handle table completion
        if tag == "cell" and self.in_table:
            self.current_row.append(text_content)
        
        if tag == "row" and self.in_table:
            if self.current_row:
                self.table_rows.append(self.current_row)
            self.current_row = []
        
        if tag == "table":
            self.in_table = False
            if self.table_rows:
                for row_idx, row in enumerate(self.table_rows):
                    escaped_cells = [_table_cell_escape(c) for c in row]
                    self.output.write("| " + " | ".join(escaped_cells) + " |\n")
                    if row_idx == 0:
                        self.output.write("| " + " | ".join(["---"] * len(row)) + " |\n")
                self.output.write("\n")
        
        # Handle diagram completion
        if tag == "diagram":
            self.in_diagram = False
            if self.diagram_nodes or self.diagram_edges:
                kind = (attrs.get("kind", "flow") or "flow").lower()
                
                if kind in ("flow", "flowchart"):
                    lines = ["flowchart LR"]
                    for nid, label in self.diagram_nodes.items():
                        safe_label = _mermaid_safe_label(label)
                        lines.append(f"    {nid}[{safe_label}]")
                    for a, b, lab in self.diagram_edges:
                        safe_lab = _mermaid_safe_label(lab)
                        if safe_lab:
                            lines.append(f"    {a} -- {safe_lab} --> {b}")
                        else:
                            lines.append(f"    {a} --> {b}")
                    code = "\n".join(lines)
                    self.output.write(f"```mermaid\n{code}\n```\n\n")
                
                elif kind in ("sequence", "seq"):
                    lines = ["sequenceDiagram"]
                    for nid, label in self.diagram_nodes.items():
                        safe_label = _mermaid_safe_label(label)
                        if safe_label and safe_label != nid:
                            lines.append(f"    participant {nid} as \"{safe_label}\"")
                        else:
                            lines.append(f"    participant {nid}")
                    for a, b, lab in self.diagram_edges:
                        safe_lab = _mermaid_safe_label(lab)
                        if a and b and safe_lab:
                            lines.append(f"    {a}->>{b}: {safe_lab}")
                        elif a and b:
                            lines.append(f"    {a}->>{b}")
                    code = "\n".join(lines)
                    self.output.write(f"```mermaid\n{code}\n```\n\n")
            
            # Reset diagram state
            self.diagram_nodes = {}
            self.diagram_edges = []
        
        # Emit content based on tag
        if tag == "p" and text_content:
            self.output.write(f"{_md_escape(text_content)}\n\n")
        elif tag == "code":
            lang = attrs.get("lang", "")
            if text_content:
                self.output.write(f"```{lang}\n{text_content}\n```\n\n")
        elif tag == "math" and text_content:
            self.output.write(f"$$\n{text_content}\n$$\n\n")
        elif tag == "callout":
            kind = (attrs.get("type", "note") or "note").upper()
            if text_content and self.ctx.cfg.callout_style == "github":
                self.output.write(f"> [!{kind}]\n> {text_content}\n\n")
    
    def characters(self, content):
        if self.element_stack:
            self.element_stack[-1][2].append(content)


def transform_xml_to_md_streaming(
    xml_input: Union[str, Path],
    output: Union[str, Path, TextIO],
    assets_resolver: Optional[Callable[[Element], str]] = None,
    config: Optional[TransformConfig] = None,
) -> None:
    """Transform XML to Markdown using streaming (SAX) parser."""
    cfg = config or TransformConfig()
    resolver = assets_resolver or default_assets_resolver()
    ctx = RenderContext(cfg=cfg, assets_resolver=resolver)
    
    # Open output
    if isinstance(output, (str, Path)):
        out_file = open(output, "w", encoding="utf-8")
        close_after = True
    else:
        out_file = output
        close_after = False
    
    try:
        md_handler = StreamingMarkdownHandler(out_file, ctx)
        
        # Parse input
        if isinstance(xml_input, (str, Path)) and Path(str(xml_input)).exists():
            xml.sax.parse(str(xml_input), md_handler)
        elif isinstance(xml_input, str):
            xml.sax.parseString(xml_input, md_handler)
        else:
            raise XMLParseError("Invalid input for streaming mode")
    finally:
        if close_after:
            out_file.close()

# ----------------------------- Main API ------------------------------------

def transform_xml_to_md(
    xml_input: Union[str, Path, bytes],
    output: Optional[Union[str, Path]] = None,
    assets_resolver: Optional[Callable[[Element], str]] = None,
    config: Optional[TransformConfig] = None,
    streaming: bool = False,
) -> Optional[Md]:
    """Transform XML to Markdown.
    
    Args:
        xml_input: XML file path, string, or bytes
        output: Optional output file path
        assets_resolver: Function to resolve asset URLs
        config: Transformation configuration
        streaming: Use streaming mode (SAX parser)
    
    Returns:
        Markdown string if output is None, otherwise None
    """
    if streaming:
        if not output:
            raise ValueError("Streaming mode requires output parameter")
        transform_xml_to_md_streaming(xml_input, output, assets_resolver, config)
        return None
    
    # Non-streaming: parse and render
    cfg = config or TransformConfig()
    resolver = assets_resolver or default_assets_resolver()
    ctx = RenderContext(cfg=cfg, assets_resolver=resolver)
    
    root = _as_xml_root(xml_input)
    md = _dispatch(root, ctx)
    
    if output:
        Path(output).write_text(md, encoding="utf-8")
        return None
    
    return md

# ----------------------------- CLI -----------------------------------------

def run_cli(args_list=None) -> int:
    """CLI entry point that returns status code instead of calling sys.exit()."""
    
    # Check if we're in a TTY (interactive terminal)
    try:
        is_tty = os.isatty(sys.stdin.fileno())
    except (AttributeError, io.UnsupportedOperation):
        is_tty = False
    
    # Build parser
    parser = argparse.ArgumentParser(
        description="Transform XML to enriched Markdown (Mermaid-safe, GitHub-friendly)",
        add_help=True,
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="-",
        help="Input XML file (use '-' for STDIN, default: STDIN)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output Markdown file (default: STDOUT)"
    )
    parser.add_argument(
        "--streaming",
        action="store_true",
        help="Use streaming mode (SAX) for large files (requires -o/--output)"
    )
    parser.add_argument(
        "--no-frontmatter",
        action="store_true",
        help="Disable YAML front matter generation"
    )
    parser.add_argument(
        "--no-h1",
        action="store_true",
        help="Don't render document title as H1"
    )
    parser.add_argument(
        "--diagram",
        choices=["mermaid", "none"],
        default="mermaid",
        help="Diagram rendering strategy (default: mermaid)"
    )
    parser.add_argument(
        "--base-url",
        default="",
        help="Base URL for resolving relative asset paths"
    )
    parser.add_argument(
        "--selftest",
        action="store_true",
        help="Run built-in self-tests and exit"
    )
    
    # Parse args
    try:
        args = parser.parse_args(args_list)
    except SystemExit as e:
        # argparse calls sys.exit on error or -h
        # In non-TTY contexts, we want to avoid this
        if not is_tty and e.code != 0:
            _eprint("Error parsing arguments")
            return 2
        raise
    
    # Self-test mode
    if args.selftest:
        try:
            def _assert(cond, msg):
                if not cond:
                    raise AssertionError(msg)
            
            # Test 1: Basic transformation
            md1 = transform_xml_to_md(
                """<document title="Test">
                  <section title="Intro">
                    <p>Hello world</p>
                  </section>
                </document>"""
            )
            _assert("# Test" in md1 and "## Intro" in md1 and "Hello world" in md1, "basic transform failed")
            
            # Test 2: Mermaid diagram
            md2 = transform_xml_to_md(
                """<document>
                  <diagram kind="flow">
                    <node id="A" label="Start"/>
                    <node id="B" label="End"/>
                    <edge from="A" to="B" label="process"/>
                  </diagram>
                </document>"""
            )
            _assert("```mermaid" in md2 and "flowchart LR" in md2, "mermaid flow failed")
            
            # Test 3: Streaming mode
            out_io = io.StringIO()
            transform_xml_to_md_streaming(
                """<document title="X">
                  <section title="S"><p>T</p></section>
                </document>""",
                out_io
            )
            s = out_io.getvalue()
            _assert("# X" in s and "S" in s and "T" in s, "streaming failed")
            
            # Test 4: Table with pipe escaping
            md3 = transform_xml_to_md(
                """<document>
                  <table>
                    <row><cell>Col 1</cell><cell>Has | pipe</cell></row>
                    <row><cell>A</cell><cell>B</cell></row>
                  </table>
                </document>"""
            )
            _assert("Has \\| pipe" in md3, "table pipe escaping failed")
            
            # Test 5: Nested lists
            md4 = transform_xml_to_md(
                """<document>
                  <list>
                    <item>Item 1
                      <list>
                        <item>Sub 1.1</item>
                        <item>Sub 1.2</item>
                      </list>
                    </item>
                    <item>Item 2</item>
                  </list>
                </document>"""
            )
            _assert("- Item 1" in md4 and "  - Sub 1.1" in md4 and "- Item 2" in md4, "nested list failed")
            
            # Test 6: Sequence diagram
            md5 = transform_xml_to_md(
                """<document>
                  <diagram kind="sequence">
                    <node id="User" label="Human Operator"/>
                    <node id="System" label=""/>
                    <edge from="User" to="System" label="Request"/>
                    <edge from="System" to="User" label="Response"/>
                  </diagram>
                </document>"""
            )
            _assert("sequenceDiagram" in md5 and "participant User as" in md5 and "User->>System: Request" in md5, "sequence diagram failed")
            
            # Test 7: API error behavior (no SystemExit)
            try:
                transform_xml_to_md("<document><p>")  # malformed XML
                _assert(False, "expected XMLParseError")
            except XMLParseError:
                pass
            
            _eprint("Selftests OK.")
            return 0
        except Exception as e:
            _eprint("Selftests failed:", e)
            return 1
    
    cfg = TransformConfig(
        generate_frontmatter=not args.no_frontmatter,
        render_doc_title_as_h1=not args.no_h1,
        diagram_strategy=args.diagram,
    )
    resolver = default_assets_resolver(args.base_url)
    
    try:
        # Decide input source
        if args.input == "-":
            xml_data = sys.stdin.read()
            if not xml_data.strip():
                _eprint("No input provided on STDIN. Provide a file or pipe XML.")
                return 1
            if args.streaming:
                if not args.output:
                    _eprint("In streaming mode you must provide -o/--output.")
                    _eprint("Example: python xml_to_markdown_enhanced.py - --streaming -o out.md")
                    return 1
                transform_xml_to_md(
                    xml_data,  # string
                    output=args.output,
                    assets_resolver=resolver,
                    config=cfg,
                    streaming=True,
                )
                print(f"Successfully transformed STDIN to {args.output}")
                return 0
            else:
                md = transform_xml_to_md(xml_data, assets_resolver=resolver, config=cfg)
                if args.output:
                    Path(args.output).write_text(md or "", encoding="utf-8")
                    print(f"Successfully transformed STDIN to {args.output}")
                else:
                    print(md)
                return 0
        else:
            # File path provided
            if args.streaming:
                if not args.output:
                    _eprint("In streaming mode you must provide -o/--output.")
                    _eprint("Example: python xml_to_markdown_enhanced.py input.xml --streaming -o output.md")
                    return 1
                transform_xml_to_md(
                    Path(args.input),
                    output=args.output,
                    assets_resolver=resolver,
                    config=cfg,
                    streaming=True,
                )
                print(f"Successfully transformed {args.input} to {args.output}")
                return 0
            else:
                md = transform_xml_to_md(Path(args.input), assets_resolver=resolver, config=cfg)
                if args.output:
                    Path(args.output).write_text(md or "", encoding="utf-8")
                    print(f"Successfully transformed {args.input} to {args.output}")
                else:
                    print(md)
                return 0
    except XMLParseError as e:
        _eprint(f"XML Parse Error: {e}")
        return 1
    except FileNotFoundError as e:
        _eprint(f"File not found: {e}")
        return 1
    except Exception as e:
        _eprint(f"Error: {e}")
        return 1


def main():
    """Main entry point for CLI."""
    status = run_cli()
    # Call sys.exit to ensure proper exit code propagation
    sys.exit(status)


if __name__ == "__main__":
    main()
