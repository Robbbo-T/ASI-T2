# XML to Markdown Transformer

A comprehensive XML to Markdown transformer with Mermaid diagram support, GitHub-friendly formatting, and streaming capabilities.

## Features

- ✅ **Mermaid Diagram Support**: Converts XML diagram definitions to Mermaid syntax
  - Flow diagrams (flowchart)
  - Sequence diagrams
  - Safe character escaping for Mermaid compatibility
  
- ✅ **GitHub-Friendly Markdown**:
  - GitHub-style callouts (`> [!NOTE]`, `> [!WARNING]`, etc.)
  - Proper table formatting with pipe escaping
  - Nested lists with correct indentation
  - YAML front matter
  
- ✅ **Streaming Mode**: Handle large XML files efficiently using SAX parser

- ✅ **Robust Error Handling**: 
  - Detailed XML parse error messages with line/column information
  - No spurious `SystemExit` exceptions in library usage
  - Proper exit codes for CLI usage

- ✅ **Python 3.7+ Support**: Version guard with helpful error messages

- ✅ **Built-in Self-Tests**: Comprehensive test suite with `--selftest` flag

## Installation

No additional dependencies required beyond Python 3.7+ standard library.

```bash
# Make executable (optional)
chmod +x scripts/xml_to_markdown_enhanced.py
```

## Usage

### Basic Usage

```bash
# Transform a file to stdout
python3 scripts/xml_to_markdown_enhanced.py input.xml

# Read from stdin
cat input.xml | python3 scripts/xml_to_markdown_enhanced.py -

# Write to file
python3 scripts/xml_to_markdown_enhanced.py input.xml -o output.md
```

### Streaming Mode (for large files)

```bash
# Streaming requires output file
python3 scripts/xml_to_markdown_enhanced.py large.xml --streaming -o output.md

# Streaming from stdin
cat large.xml | python3 scripts/xml_to_markdown_enhanced.py - --streaming -o output.md
```

### Options

```bash
# Disable front matter
python3 scripts/xml_to_markdown_enhanced.py input.xml --no-frontmatter

# Disable H1 title rendering
python3 scripts/xml_to_markdown_enhanced.py input.xml --no-h1

# Disable diagram rendering
python3 scripts/xml_to_markdown_enhanced.py input.xml --diagram none

# Set base URL for relative assets
python3 scripts/xml_to_markdown_enhanced.py input.xml --base-url https://example.com/assets
```

### Self-Tests

```bash
# Run built-in tests
python3 scripts/xml_to_markdown_enhanced.py --selftest
```

## Supported XML Elements

### Document Structure

- `<document>` - Root element with optional `title`, `author`, `date` attributes
- `<section>` - Sections with `title` and `level` attributes
- `<p>` - Paragraphs

### Lists

- `<list>` - Unordered lists
- `<olist>` - Ordered lists
- `<item>` - List items (supports nesting)

### Tables

```xml
<table>
  <row>
    <cell>Header 1</cell>
    <cell>Header 2</cell>
  </row>
  <row>
    <cell>Data 1</cell>
    <cell>Data 2</cell>
  </row>
</table>
```

### Code & Math

- `<code lang="python">` - Code blocks with language syntax
- `<math>` - LaTeX math equations (rendered as `$$...$$`)

### Diagrams

#### Flow Diagram
```xml
<diagram kind="flow">
  <node id="A" label="Start"/>
  <node id="B" label="End"/>
  <edge from="A" to="B" label="process"/>
</diagram>
```

#### Sequence Diagram
```xml
<diagram kind="sequence">
  <node id="User" label="User"/>
  <node id="System" label="System"/>
  <edge from="User" to="System" label="Request"/>
  <edge from="System" to="User" label="Response"/>
</diagram>
```

### Media & Links

- `<figure src="..." caption="..." alt="..."/>` - Images
- `<media type="video" src="..."/>` - Audio/Video (HTML5 embed)
- `<link href="...">text</link>` - Links
- `<ref href="...">text</ref>` - References (alias for link)

### Callouts

```xml
<callout type="note">Important information</callout>
<callout type="warning">Warning message</callout>
<callout type="important">Critical notice</callout>
```

Renders as GitHub-style alerts:
```markdown
> [!NOTE]
> Important information
```

### Details (Collapsible)

```xml
<details summary="Click to expand">
  Hidden content here
</details>
```

## API Usage

The script can also be used as a Python library:

```python
from scripts.xml_to_markdown_enhanced import (
    transform_xml_to_md,
    transform_xml_to_md_streaming,
    TransformConfig,
    default_assets_resolver,
)

# Basic transformation
markdown = transform_xml_to_md("<document><p>Hello</p></document>")

# With custom config
config = TransformConfig(
    generate_frontmatter=False,
    render_doc_title_as_h1=True,
    diagram_strategy="mermaid",
)
markdown = transform_xml_to_md("input.xml", config=config)

# Streaming mode
transform_xml_to_md_streaming(
    "large.xml",
    output="output.md",
    config=config,
)

# Custom asset resolver
def my_resolver(elem):
    src = elem.attrib.get("src", "")
    return f"https://cdn.example.com/{src}"

markdown = transform_xml_to_md(
    "input.xml",
    assets_resolver=my_resolver,
)

# Use run_cli() to avoid SystemExit in interactive contexts
from scripts.xml_to_markdown_enhanced import run_cli
status = run_cli(["input.xml", "-o", "output.md"])
print(f"Status: {status}")
```

## Error Handling

The script provides detailed error messages:

```bash
$ python3 scripts/xml_to_markdown_enhanced.py invalid.xml
XML Parse Error: XML parsing failed: not well-formed (invalid token): line 5, column 12 at line 5, column 12
$ echo $?
1
```

For library usage, catch `XMLParseError`:

```python
from scripts.xml_to_markdown_enhanced import transform_xml_to_md, XMLParseError

try:
    md = transform_xml_to_md("<document><p>")  # malformed
except XMLParseError as e:
    print(f"Parse error: {e}")
    print(f"Line: {e.line}, Column: {e.column}")
```

## Example

Input XML:
```xml
<document title="My Document">
  <section title="Introduction">
    <p>Welcome to the document.</p>
  </section>
  <section title="Diagram">
    <diagram kind="flow">
      <node id="A" label="Start"/>
      <node id="B" label="End"/>
      <edge from="A" to="B" label="go"/>
    </diagram>
  </section>
</document>
```

Output Markdown:
```markdown
---
title: My Document
---

# My Document

## Introduction {#introduction}

Welcome to the document.

## Diagram {#diagram}

```mermaid
flowchart LR
    A[Start]
    B[End]
    A -- go --> B
```
```

## Python Version Requirements

- Requires Python 3.7 or higher
- Uses only standard library modules (no external dependencies)
- Type hints compatible with Python 3.7+

## License

Part of the ASI-T2 repository. See main repository LICENSE for details.
