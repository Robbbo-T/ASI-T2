#!/usr/bin/env python3
"""
Generate technical diagrams from figure placeholder descriptions in markdown files.
Creates blueprint-style technical diagrams for ATA-42 OS documentation.
"""

import re
import os
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch, Circle
from matplotlib.lines import Line2D
import textwrap

# Blueprint color palette
BLUEPRINT_BG = '#0d1b2a'
BLUEPRINT_FG = '#e0e1dd'
BLUEPRINT_ACCENT = '#778da9'
BLUEPRINT_HIGHLIGHT = '#415a77'
BLUEPRINT_LINE = '#778da9'

class FigureGenerator:
    """Generate blueprint-style technical diagrams"""
    
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def setup_blueprint_style(self, fig, ax):
        """Apply blueprint styling to figure"""
        fig.patch.set_facecolor(BLUEPRINT_BG)
        ax.set_facecolor(BLUEPRINT_BG)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
    def wrap_text(self, text, width=30):
        """Wrap text to specified width"""
        return '\n'.join(textwrap.wrap(text, width=width))
        
    def generate_platform_stack(self, filename):
        """Generate AQUA-OS platform stack overview"""
        fig, ax = plt.subplots(figsize=(12, 8))
        self.setup_blueprint_style(fig, ax)
        
        # Stack layers from bottom to top
        layers = [
            ("Hardware", 1, "Core CPU/Memory/IO"),
            ("Separation Kernel", 2.5, "Time & Space Partitioning"),
            ("APEX Services", 4, "Partition/Process/Time/IPC/HM"),
            ("I/O Manager & HM", 5.5, "Device Mediation"),
            ("Partitions", 7, "FCC | NAV | DISPLAYS | MAINT")
        ]
        
        for i, (name, y_pos, desc) in enumerate(layers):
            # Draw box
            box = FancyBboxPatch((1, y_pos), 8, 1, 
                                boxstyle="round,pad=0.05",
                                edgecolor=BLUEPRINT_LINE, 
                                facecolor=BLUEPRINT_HIGHLIGHT,
                                linewidth=2)
            ax.add_patch(box)
            
            # Add text
            ax.text(5, y_pos + 0.5, f"{name}\n{desc}", 
                   ha='center', va='center',
                   color=BLUEPRINT_FG, fontsize=10, weight='bold')
            
            # Add arrows between layers (except last)
            if i < len(layers) - 1:
                arrow = FancyArrowPatch((5, y_pos + 1), (5, y_pos + 1.3),
                                      arrowstyle='->', mutation_scale=20,
                                      color=BLUEPRINT_ACCENT, linewidth=1.5)
                ax.add_patch(arrow)
        
        # Add DAL callouts
        ax.text(9.5, 7.5, "DAL A-D", ha='center', va='center',
               color=BLUEPRINT_ACCENT, fontsize=8, style='italic',
               bbox=dict(boxstyle='round', facecolor=BLUEPRINT_BG, 
                        edgecolor=BLUEPRINT_ACCENT, linewidth=1))
        
        ax.text(9.5, 4.5, "DO-297\nRoles", ha='center', va='center',
               color=BLUEPRINT_ACCENT, fontsize=8, style='italic',
               bbox=dict(boxstyle='round', facecolor=BLUEPRINT_BG, 
                        edgecolor=BLUEPRINT_ACCENT, linewidth=1))
        
        plt.title("AQUA-OS Platform Stack", color=BLUEPRINT_FG, fontsize=14, pad=20)
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150, facecolor=BLUEPRINT_BG)
        plt.close()
        
    def generate_context_diagram(self, filename):
        """Generate aircraft systems context diagram"""
        fig, ax = plt.subplots(figsize=(12, 8))
        self.setup_blueprint_style(fig, ax)
        
        # Central AQUA-OS box
        center_box = FancyBboxPatch((3.5, 4), 3, 2,
                                   boxstyle="round,pad=0.1",
                                   edgecolor=BLUEPRINT_LINE,
                                   facecolor=BLUEPRINT_HIGHLIGHT,
                                   linewidth=2)
        ax.add_patch(center_box)
        ax.text(5, 5, "AQUA-OS\nPartitions", ha='center', va='center',
               color=BLUEPRINT_FG, fontsize=11, weight='bold')
        
        # Partition boxes
        partitions = [
            ("FCC", 5, 6.5), ("NAV", 3.8, 5), 
            ("DISPLAYS", 6.2, 5), ("MAINT", 5, 3.5)
        ]
        for name, x, y in partitions:
            box = Rectangle((x-0.3, y-0.2), 0.6, 0.4,
                          edgecolor=BLUEPRINT_ACCENT,
                          facecolor=BLUEPRINT_BG,
                          linewidth=1)
            ax.add_patch(box)
            ax.text(x, y, name, ha='center', va='center',
                   color=BLUEPRINT_FG, fontsize=8)
        
        # External systems
        systems = [
            ("Aircraft\nSystems", 1, 7, "AFDX"),
            ("Avionics\nBus", 1, 5, "ARINC 429"),
            ("Sensors", 1, 3, "AFDX"),
            ("Cockpit\nDisplays", 9, 7, "AFDX"),
            ("External\nSystems", 9, 3, "ARINC 429")
        ]
        
        for name, x, y, protocol in systems:
            box = FancyBboxPatch((x-0.5, y-0.4), 1, 0.8,
                                boxstyle="round,pad=0.05",
                                edgecolor=BLUEPRINT_LINE,
                                facecolor=BLUEPRINT_BG,
                                linewidth=1.5)
            ax.add_patch(box)
            ax.text(x, y, name, ha='center', va='center',
                   color=BLUEPRINT_FG, fontsize=8)
            
            # Draw connection lines
            if x < 5:
                arrow = FancyArrowPatch((x+0.5, y), (3.5, 5),
                                      arrowstyle='<->', mutation_scale=15,
                                      color=BLUEPRINT_ACCENT, linewidth=1.5)
                ax.add_patch(arrow)
                ax.text((x+4)/2, (y+5)/2, protocol, ha='center', va='bottom',
                       color=BLUEPRINT_ACCENT, fontsize=7, style='italic')
            else:
                arrow = FancyArrowPatch((x-0.5, y), (6.5, 5),
                                      arrowstyle='<->', mutation_scale=15,
                                      color=BLUEPRINT_ACCENT, linewidth=1.5)
                ax.add_patch(arrow)
                ax.text((x+6)/2, (y+5)/2, protocol, ha='center', va='bottom',
                       color=BLUEPRINT_ACCENT, fontsize=7, style='italic')
        
        plt.title("AQUA-OS Context Diagram", color=BLUEPRINT_FG, fontsize=14, pad=20)
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150, facecolor=BLUEPRINT_BG)
        plt.close()
        
    def generate_architecture_layers(self, filename):
        """Generate layered architecture diagram"""
        fig, ax = plt.subplots(figsize=(12, 8))
        self.setup_blueprint_style(fig, ax)
        
        components = [
            ("Config Loader", 1, 8, 1.5, 0.8),
            ("SK\nSeparation\nKernel", 3, 8, 1.5, 0.8),
            ("PM\nPartition\nManager", 5, 8, 1.5, 0.8),
            ("APEX\nServices", 7, 8, 2, 0.8),
            ("I/O Manager", 2, 6.5, 2.5, 0.8),
            ("HM\nHealth\nMonitor", 5.5, 6.5, 2.5, 0.8)
        ]
        
        for name, x, y, w, h in components:
            box = FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.05",
                                edgecolor=BLUEPRINT_LINE,
                                facecolor=BLUEPRINT_HIGHLIGHT,
                                linewidth=2)
            ax.add_patch(box)
            ax.text(x + w/2, y + h/2, name, ha='center', va='center',
                   color=BLUEPRINT_FG, fontsize=9, weight='bold')
        
        # Trust boundary
        ax.plot([0.5, 9.5], [5.8, 5.8], '--', color=BLUEPRINT_ACCENT, linewidth=2)
        ax.text(9.7, 5.8, "Trust Boundary", ha='left', va='center',
               color=BLUEPRINT_ACCENT, fontsize=8, style='italic')
        
        # Control/data paths
        arrows = [
            ((3.75, 8), (3.75, 7.3)),
            ((5.75, 8), (5.75, 7.3)),
            ((2.5, 7.3), (2.5, 6.5)),
            ((6.5, 7.3), (6.5, 6.5))
        ]
        
        for start, end in arrows:
            arrow = FancyArrowPatch(start, end,
                                  arrowstyle='->', mutation_scale=15,
                                  color=BLUEPRINT_ACCENT, linewidth=1.5)
            ax.add_patch(arrow)
        
        plt.title("Layered Architecture", color=BLUEPRINT_FG, fontsize=14, pad=20)
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150, facecolor=BLUEPRINT_BG)
        plt.close()
        
    def generate_design_principles(self, filename):
        """Generate design principles tile grid"""
        fig, ax = plt.subplots(figsize=(12, 8))
        self.setup_blueprint_style(fig, ax)
        
        principles = [
            ("Minimal TCB", "Smallest trusted base"),
            ("Least Privilege", "Minimal permissions"),
            ("Determinism First", "No dynamic allocation"),
            ("Separation", "Kernel | Partitions | I/O"),
            ("Bounded Services", "All ops have limits"),
            ("Verifiable", "Requirements→Tests trace")
        ]
        
        cols = 3
        rows = 2
        tile_w = 2.5
        tile_h = 1.8
        margin = 0.8
        
        for i, (title, desc) in enumerate(principles):
            row = i // cols
            col = i % cols
            x = 1 + col * (tile_w + margin)
            y = 7 - row * (tile_h + margin)
            
            box = FancyBboxPatch((x, y), tile_w, tile_h,
                                boxstyle="round,pad=0.05",
                                edgecolor=BLUEPRINT_LINE,
                                facecolor=BLUEPRINT_HIGHLIGHT,
                                linewidth=2)
            ax.add_patch(box)
            
            # Title
            ax.text(x + tile_w/2, y + tile_h - 0.3, title,
                   ha='center', va='center',
                   color=BLUEPRINT_FG, fontsize=10, weight='bold')
            
            # Description
            ax.text(x + tile_w/2, y + 0.5, desc,
                   ha='center', va='center',
                   color=BLUEPRINT_ACCENT, fontsize=8)
        
        plt.title("Design Principles", color=BLUEPRINT_FG, fontsize=14, pad=20)
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150, facecolor=BLUEPRINT_BG)
        plt.close()
        
    def generate_timeline(self, filename):
        """Generate major/minor frame timeline"""
        fig, ax = plt.subplots(figsize=(12, 6))
        self.setup_blueprint_style(fig, ax)
        
        # Timeline
        timeline_y = 5
        ax.plot([1, 9], [timeline_y, timeline_y], color=BLUEPRINT_LINE, linewidth=2)
        
        # Windows
        windows = [
            ("FCC_A", 1, 2, BLUEPRINT_HIGHLIGHT),
            ("NAV", 2, 1.5, BLUEPRINT_ACCENT),
            ("DISPLAYS", 3.5, 2, BLUEPRINT_HIGHLIGHT),
            ("MAINT", 5.5, 1, BLUEPRINT_ACCENT),
            ("FCC_B", 6.5, 1.5, BLUEPRINT_HIGHLIGHT)
        ]
        
        for name, x, width, color in windows:
            box = Rectangle((x, timeline_y - 0.3), width, 0.6,
                          edgecolor=BLUEPRINT_LINE,
                          facecolor=color,
                          linewidth=2)
            ax.add_patch(box)
            ax.text(x + width/2, timeline_y, name,
                   ha='center', va='center',
                   color=BLUEPRINT_FG, fontsize=9, weight='bold')
            
            # Time markers
            ax.plot([x, x], [timeline_y - 0.5, timeline_y - 0.8], 
                   color=BLUEPRINT_ACCENT, linewidth=1)
            ax.text(x, timeline_y - 1, f"{int((x-1)*10)}ms",
                   ha='center', va='top',
                   color=BLUEPRINT_ACCENT, fontsize=7)
        
        # End marker
        ax.plot([8, 8], [timeline_y - 0.5, timeline_y - 0.8],
               color=BLUEPRINT_ACCENT, linewidth=1)
        ax.text(8, timeline_y - 1, "80ms",
               ha='center', va='top',
               color=BLUEPRINT_ACCENT, fontsize=7)
        
        # Jitter band
        ax.fill_between([1, 8], timeline_y - 0.25, timeline_y + 0.25,
                       alpha=0.1, color=BLUEPRINT_ACCENT)
        ax.text(8.5, timeline_y, "Jitter\nBand",
               ha='left', va='center',
               color=BLUEPRINT_ACCENT, fontsize=7, style='italic')
        
        # Major frame bracket
        ax.plot([1, 1, 8, 8], [timeline_y + 1, timeline_y + 1.2, timeline_y + 1.2, timeline_y + 1],
               color=BLUEPRINT_FG, linewidth=1.5)
        ax.text(4.5, timeline_y + 1.4, "Major Frame (80ms)",
               ha='center', va='bottom',
               color=BLUEPRINT_FG, fontsize=10)
        
        plt.title("Partition Scheduling Timeline", color=BLUEPRINT_FG, fontsize=14, pad=20)
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150, facecolor=BLUEPRINT_BG)
        plt.close()
        
    def generate_memory_map(self, filename):
        """Generate address space schematic"""
        fig, ax = plt.subplots(figsize=(10, 10))
        self.setup_blueprint_style(fig, ax)
        
        # Memory regions
        regions = [
            ("Partition C", 1, 8, 3, 1.5, "R/W"),
            ("Shared Memory", 5, 8, 3, 1, "R/W Policy"),
            ("Partition B", 1, 6, 3, 1.5, "R/W"),
            ("Partition A", 5, 5.5, 3, 2, "R/W"),
            ("Kernel Region", 1, 3.5, 7, 1.5, "Protected")
        ]
        
        for name, x, y, w, h, access in regions:
            is_kernel = "Kernel" in name
            color = BLUEPRINT_HIGHLIGHT if not is_kernel else BLUEPRINT_ACCENT
            
            box = FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.05",
                                edgecolor=BLUEPRINT_LINE,
                                facecolor=color,
                                linewidth=2)
            ax.add_patch(box)
            
            ax.text(x + w/2, y + h/2 + 0.2, name,
                   ha='center', va='center',
                   color=BLUEPRINT_FG, fontsize=10, weight='bold')
            ax.text(x + w/2, y + h/2 - 0.3, access,
                   ha='center', va='center',
                   color=BLUEPRINT_FG, fontsize=8, style='italic')
        
        # Deny arrows
        deny_positions = [
            ((2.5, 7.5), (6.5, 9)),  # A -> C
            ((6.5, 6.5), (2.5, 9))   # C -> B
        ]
        
        for start, end in deny_positions:
            ax.plot([start[0], end[0]], [start[1], end[1]],
                   'x--', color='#d62828', linewidth=2, markersize=10)
            mid_x = (start[0] + end[0]) / 2
            mid_y = (start[1] + end[1]) / 2
            ax.text(mid_x, mid_y, "DENY", ha='center', va='center',
                   color='#d62828', fontsize=8, weight='bold',
                   bbox=dict(boxstyle='round', facecolor=BLUEPRINT_BG,
                           edgecolor='#d62828', linewidth=1))
        
        # Address labels
        addresses = ["0x0000", "0x1000", "0x2000", "0x3000", "0x4000"]
        for i, addr in enumerate(addresses):
            y_pos = 9.5 - i * 1.5
            ax.text(0.5, y_pos, addr, ha='right', va='center',
                   color=BLUEPRINT_ACCENT, fontsize=7, family='monospace')
        
        plt.title("Address Space Partitioning", color=BLUEPRINT_FG, fontsize=14, pad=20)
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150, facecolor=BLUEPRINT_BG)
        plt.close()
        
    def generate_hm_concept(self, filename):
        """Generate HM concept view"""
        fig, ax = plt.subplots(figsize=(12, 6))
        self.setup_blueprint_style(fig, ax)
        
        # Flow boxes
        boxes = [
            ("Detectors", 1, 4.5, 1.5, 1),
            ("Classifier", 3.5, 4.5, 1.5, 1),
            ("Action\nSelector", 6, 4.5, 1.5, 1)
        ]
        
        for name, x, y, w, h in boxes:
            box = FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.05",
                                edgecolor=BLUEPRINT_LINE,
                                facecolor=BLUEPRINT_HIGHLIGHT,
                                linewidth=2)
            ax.add_patch(box)
            ax.text(x + w/2, y + h/2, name,
                   ha='center', va='center',
                   color=BLUEPRINT_FG, fontsize=10, weight='bold')
        
        # Arrows
        arrow1 = FancyArrowPatch((2.5, 5), (3.5, 5),
                                arrowstyle='->', mutation_scale=20,
                                color=BLUEPRINT_ACCENT, linewidth=2)
        arrow2 = FancyArrowPatch((5, 5), (6, 5),
                                arrowstyle='->', mutation_scale=20,
                                color=BLUEPRINT_ACCENT, linewidth=2)
        ax.add_patch(arrow1)
        ax.add_patch(arrow2)
        
        # Action outputs
        actions = ["LOG", "HOT", "WARM", "STOP", "SYS\nRECONFIG"]
        for i, action in enumerate(actions):
            y_pos = 7.5 - i * 0.8
            box = Rectangle((8, y_pos - 0.3), 1, 0.6,
                          edgecolor=BLUEPRINT_ACCENT,
                          facecolor=BLUEPRINT_BG,
                          linewidth=1.5)
            ax.add_patch(box)
            ax.text(8.5, y_pos, action,
                   ha='center', va='center',
                   color=BLUEPRINT_FG, fontsize=8)
            
            # Arrow to action
            arrow = FancyArrowPatch((7.5, 5), (8, y_pos),
                                  arrowstyle='->', mutation_scale=15,
                                  color=BLUEPRINT_ACCENT, linewidth=1,
                                  linestyle='--')
            ax.add_patch(arrow)
        
        # Telemetry to audit log
        ax.text(8.5, 2.5, "Audit Log", ha='center', va='center',
               color=BLUEPRINT_FG, fontsize=9,
               bbox=dict(boxstyle='round', facecolor=BLUEPRINT_HIGHLIGHT,
                        edgecolor=BLUEPRINT_LINE, linewidth=2))
        
        arrow_log = FancyArrowPatch((6.75, 4.5), (8.5, 3),
                                   arrowstyle='->', mutation_scale=15,
                                   color=BLUEPRINT_ACCENT, linewidth=1.5,
                                   linestyle='--')
        ax.add_patch(arrow_log)
        ax.text(7.5, 3.7, "Telemetry",
               ha='center', va='center',
               color=BLUEPRINT_ACCENT, fontsize=7, style='italic')
        
        plt.title("Health Monitoring Concept", color=BLUEPRINT_FG, fontsize=14, pad=20)
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150, facecolor=BLUEPRINT_BG)
        plt.close()
        
    def generate_simple_diagram(self, filename, title, description):
        """Generate a simple placeholder diagram with text"""
        fig, ax = plt.subplots(figsize=(12, 6))
        self.setup_blueprint_style(fig, ax)
        
        # Central box with wrapped text
        wrapped_desc = self.wrap_text(description, width=50)
        
        box = FancyBboxPatch((2, 3), 6, 4,
                            boxstyle="round,pad=0.1",
                            edgecolor=BLUEPRINT_LINE,
                            facecolor=BLUEPRINT_HIGHLIGHT,
                            linewidth=2)
        ax.add_patch(box)
        
        ax.text(5, 5, wrapped_desc,
               ha='center', va='center',
               color=BLUEPRINT_FG, fontsize=10)
        
        plt.title(title, color=BLUEPRINT_FG, fontsize=14, pad=20)
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150, facecolor=BLUEPRINT_BG)
        plt.close()


def parse_placeholders(md_file):
    """Extract figure placeholders from markdown file"""
    content = Path(md_file).read_text()
    pattern = r'\[FIGURE PLACEHOLDER: "(.*?)"\]'
    matches = re.finditer(pattern, content)
    
    placeholders = []
    for match in matches:
        placeholders.append({
            'full_match': match.group(0),
            'description': match.group(1),
            'line_num': content[:match.start()].count('\n') + 1
        })
    
    return placeholders


def generate_all_figures(md_file, output_dir):
    """Generate all figures for the markdown file"""
    placeholders = parse_placeholders(md_file)
    generator = FigureGenerator(output_dir)
    
    print(f"Found {len(placeholders)} figure placeholders")
    
    # Map specific generators to placeholders
    figure_map = {
        0: ('fig-01-platform-stack.png', generator.generate_platform_stack),
        1: ('fig-02-context-diagram.png', generator.generate_context_diagram),
        2: ('fig-03-architecture-layers.png', generator.generate_architecture_layers),
        3: ('fig-04-design-principles.png', generator.generate_design_principles),
        4: ('fig-05-scheduling-timeline.png', generator.generate_timeline),
        5: ('fig-06-memory-map.png', generator.generate_memory_map),
        6: ('fig-07-hm-concept.png', generator.generate_hm_concept),
    }
    
    generated_files = []
    
    for idx, placeholder in enumerate(placeholders):
        filename = f"fig-{idx+1:02d}.png"
        
        print(f"Generating figure {idx+1}/{len(placeholders)}: {filename}")
        
        if idx in figure_map:
            mapped_filename, generator_func = figure_map[idx]
            filename = mapped_filename
            generator_func(filename)
        else:
            # Generate simple placeholder for remaining figures
            title = f"Figure {idx+1}"
            generator.generate_simple_diagram(filename, title, placeholder['description'])
        
        generated_files.append((placeholder, filename))
    
    return generated_files


def update_markdown(md_file, generated_files, figures_rel_path):
    """Update markdown file with image references"""
    content = Path(md_file).read_text()
    
    for placeholder, filename in generated_files:
        # Replace placeholder with image markdown
        image_ref = f"![{placeholder['description'][:DESCRIPTION_TRUNCATE_LENGTH]}...]({figures_rel_path}/{filename})"
        content = content.replace(placeholder['full_match'], image_ref, 1)
    
    # Write updated content
    Path(md_file).write_text(content)
    print(f"Updated {md_file} with {len(generated_files)} image references")


def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python generate_publication_figures.py <markdown_file>")
        sys.exit(1)
    
    md_file = sys.argv[1]
    
    if not Path(md_file).exists():
        print(f"Error: File not found: {md_file}")
        sys.exit(1)
    
    # Create figures directory next to the markdown file
    md_path = Path(md_file)
    figures_dir = md_path.parent / "figures"
    
    print(f"Generating figures for: {md_file}")
    print(f"Output directory: {figures_dir}")
    
    # Generate all figures
    generated_files = generate_all_figures(md_file, figures_dir)
    
    # Update markdown file with image references
    figures_rel_path = "figures"
    update_markdown(md_file, generated_files, figures_rel_path)
    
    print(f"\nSuccess! Generated {len(generated_files)} figures")
    print(f"Figures saved to: {figures_dir}")


if __name__ == "__main__":
    main()
