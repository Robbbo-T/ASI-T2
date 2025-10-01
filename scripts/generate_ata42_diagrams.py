#!/usr/bin/env python3
"""
Generate technical diagrams from COPILOT:IMAGE placeholders in ATA-42 README.
Creates blueprint-style technical diagrams for ATA-42 IMA documentation.
"""

import re
import os
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch, Circle, Polygon
from matplotlib.lines import Line2D
import textwrap

# Blueprint color palette
BLUEPRINT_BG = '#0d1b2a'
BLUEPRINT_FG = '#e0e1dd'
BLUEPRINT_ACCENT = '#778da9'
BLUEPRINT_HIGHLIGHT = '#415a77'
BLUEPRINT_LINE = '#778da9'

class ATA42DiagramGenerator:
    """Generate blueprint-style technical diagrams for ATA-42"""
    
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def setup_blueprint_style(self, fig, ax):
        """Apply blueprint styling to figure"""
        fig.patch.set_facecolor(BLUEPRINT_BG)
        ax.set_facecolor(BLUEPRINT_BG)
        ax.set_xlim(0, 16)
        ax.set_ylim(0, 9)
        ax.axis('off')
        
    def wrap_text(self, text, width=30):
        """Wrap text to specified width"""
        return '\n'.join(textwrap.wrap(text, width=width))
        
    def generate_ima_overview(self, filename):
        """Generate ATA-42 IMA Overview diagram"""
        fig, ax = plt.subplots(figsize=(16, 9))
        self.setup_blueprint_style(fig, ax)
        
        # Title
        ax.text(8, 8.5, "ATA-42 IMA Overview (IIS)", 
               ha='center', va='center',
               color=BLUEPRINT_FG, fontsize=16, weight='bold')
        
        # IMA Chassis
        chassis = FancyBboxPatch((1, 0.5), 14, 7,
                                boxstyle="round,pad=0.1",
                                edgecolor=BLUEPRINT_LINE,
                                facecolor='none',
                                linewidth=3)
        ax.add_patch(chassis)
        ax.text(8, 7.2, "IMA Chassis", ha='center', va='center',
               color=BLUEPRINT_ACCENT, fontsize=10, style='italic')
        
        # Partitions
        partitions = [
            ("IIS.SwarmCore", 2, 4.5, "Swarm coordination\nResilient consensus"),
            ("IIS.MAL-EEM", 5.5, 4.5, "Ethics Gate\nFail-closed\nDAL A"),
            ("IIS.MissionPlanner", 9, 4.5, "Planning & Tasking\nReplanning"),
            ("IIS.CMSAdapter", 12.5, 4.5, "Health/Telemetry\nExport to CMS")
        ]
        
        for name, x, y, desc in partitions:
            box = FancyBboxPatch((x-0.9, y-0.7), 2.5, 2,
                                boxstyle="round,pad=0.05",
                                edgecolor=BLUEPRINT_LINE,
                                facecolor=BLUEPRINT_HIGHLIGHT,
                                linewidth=2)
            ax.add_patch(box)
            ax.text(x+0.35, y+0.8, name, ha='center', va='top',
                   color=BLUEPRINT_FG, fontsize=9, weight='bold')
            ax.text(x+0.35, y-0.3, desc, ha='center', va='center',
                   color=BLUEPRINT_FG, fontsize=7)
        
        # APEX ports/queues layer
        apex_y = 2.5
        ax.text(8, apex_y+0.5, "APEX Ports & Queues", ha='center', va='center',
               color=BLUEPRINT_ACCENT, fontsize=9, weight='bold')
        
        port_names = ["c2.swarm.v1", "sync.state.v1", "eth.rules.v1", "eth.audit.v1", 
                     "sens.bus.v1", "sens.task.v1", "cms.health.v1", "cms.export.v1"]
        
        for i, port in enumerate(port_names):
            x = 2 + (i % 4) * 3
            y = apex_y - 0.3 - (i // 4) * 0.4
            ax.text(x, y, port, ha='left', va='center',
                   color=BLUEPRINT_FG, fontsize=6,
                   bbox=dict(boxstyle='round,pad=0.2', facecolor=BLUEPRINT_BG,
                            edgecolor=BLUEPRINT_ACCENT, linewidth=0.5))
        
        # Health Manager
        hm_box = FancyBboxPatch((13, 1), 2, 1,
                               boxstyle="round,pad=0.05",
                               edgecolor=BLUEPRINT_ACCENT,
                               facecolor=BLUEPRINT_BG,
                               linewidth=2,
                               linestyle='--')
        ax.add_patch(hm_box)
        ax.text(14, 1.5, "Health\nManager", ha='center', va='center',
               color=BLUEPRINT_ACCENT, fontsize=7)
        
        # Bridges to other domains
        bridge_y = 0.8
        bridges = ["LCC", "EDI", "OOO"]
        for i, bridge in enumerate(bridges):
            x = 2 + i * 2
            ax.text(x, bridge_y, f"→{bridge}", ha='center', va='center',
                   color=BLUEPRINT_ACCENT, fontsize=8,
                   bbox=dict(boxstyle='round,pad=0.2', facecolor=BLUEPRINT_BG,
                            edgecolor=BLUEPRINT_ACCENT, linewidth=1))
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150, facecolor=BLUEPRINT_BG)
        plt.close()
        
    def generate_repo_layout(self, filename):
        """Generate ATA-42 Repo Layout diagram"""
        fig, ax = plt.subplots(figsize=(16, 9))
        self.setup_blueprint_style(fig, ax)
        
        # Title
        ax.text(8, 8.5, "ATA-42 Repository Layout", 
               ha='center', va='center',
               color=BLUEPRINT_FG, fontsize=16, weight='bold')
        
        # Root folder
        ax.text(2, 7.5, "domains/IIS/ata/ATA-42/", ha='left', va='center',
               color=BLUEPRINT_FG, fontsize=11, weight='bold',
               family='monospace')
        
        # Main folders
        folders = [
            ("README.md", 7.0, 0.3),
            ("governance/", 6.5, 0.3, "approvals, risks, baselines"),
            ("os/", 6.0, 0.5, [
                "S1000D/", 
                "configuration/",
                "  manifests/",
                "  a653/",
                "  rtos/",
                "testing/",
                "compliance/"
            ]),
            ("manufacturing/", 4.5, 0.3, "fixtures, test benches"),
            ("sustainment/", 4.0, 0.3, "service, diagnostics"),
            ("assets/", 3.5, 0.3, "diagrams, images"),
            ("scripts/", 3.0, 0.3, "validators, exporters"),
            ("docs/", 2.5, 0.3, "supplementary notes")
        ]
        
        y_pos = 7.0
        for item in folders:
            if len(item) == 3:
                name, y_pos, indent = item
                desc = None
            else:
                name, y_pos, indent, desc = item
            
            # Draw connector line
            ax.plot([2.8, 3.0 + indent], [y_pos, y_pos], 
                   color=BLUEPRINT_LINE, linewidth=1)
            
            if isinstance(desc, list):
                # Subfolder structure
                ax.text(3.2 + indent, y_pos, name, ha='left', va='center',
                       color=BLUEPRINT_FG, fontsize=10, weight='bold',
                       family='monospace')
                sub_y = y_pos - 0.3
                for sub in desc:
                    ax.text(4.0 + indent, sub_y, sub, ha='left', va='center',
                           color=BLUEPRINT_ACCENT, fontsize=8,
                           family='monospace')
                    sub_y -= 0.25
            else:
                # Single folder
                ax.text(3.2 + indent, y_pos, name, ha='left', va='center',
                       color=BLUEPRINT_FG, fontsize=10, weight='bold',
                       family='monospace')
                if desc:
                    ax.text(7.0, y_pos, f"# {desc}", ha='left', va='center',
                           color=BLUEPRINT_ACCENT, fontsize=8, style='italic')
        
        # Add key annotations box
        key_box = FancyBboxPatch((11, 5), 4, 2.5,
                                boxstyle="round,pad=0.1",
                                edgecolor=BLUEPRINT_ACCENT,
                                facecolor=BLUEPRINT_BG,
                                linewidth=2)
        ax.add_patch(key_box)
        ax.text(13, 7.2, "Key Artefacts", ha='center', va='top',
               color=BLUEPRINT_FG, fontsize=10, weight='bold')
        ax.text(11.5, 6.5, "• partition.xml\n• schedule.xml\n• manifest.yaml\n• S1000D data modules", 
               ha='left', va='top',
               color=BLUEPRINT_ACCENT, fontsize=8, family='monospace')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150, facecolor=BLUEPRINT_BG)
        plt.close()
        
    def generate_apex_port_map(self, filename):
        """Generate APEX Port Map diagram"""
        fig, ax = plt.subplots(figsize=(16, 9))
        self.setup_blueprint_style(fig, ax)
        
        # Title
        ax.text(8, 8.5, "APEX Port Map — ATA-42 / IIS", 
               ha='center', va='center',
               color=BLUEPRINT_FG, fontsize=16, weight='bold')
        
        # Column headers
        headers = ["Partition", "APEX Port", "Direction", "Type"]
        x_positions = [1, 5, 10, 13]
        for i, (header, x) in enumerate(zip(headers, x_positions)):
            ax.text(x, 7.5, header, ha='left', va='center',
                   color=BLUEPRINT_ACCENT, fontsize=10, weight='bold')
        
        # Port mappings
        ports = [
            ("IIS.SwarmCore", "c2.swarm.v1", "SRC", "Queue"),
            ("IIS.SwarmCore", "sync.state.v1", "DST", "Sampling"),
            ("IIS.MAL-EEM", "eth.rules.v1", "DST", "Sampling"),
            ("IIS.MAL-EEM", "eth.audit.v1", "SRC", "Queue"),
            ("IIS.MissionPlanner", "sens.bus.v1", "DST", "Sampling"),
            ("IIS.MissionPlanner", "sens.task.v1", "SRC", "Queue"),
            ("IIS.CMSAdapter", "cms.health.v1", "SRC", "Queue"),
            ("IIS.CMSAdapter", "cms.export.v1", "SRC", "Queue"),
        ]
        
        y_start = 7.0
        for i, (partition, port, direction, ptype) in enumerate(ports):
            y = y_start - i * 0.6
            
            # Draw row background
            if i % 2 == 0:
                row_bg = Rectangle((0.5, y-0.25), 15, 0.5,
                                  facecolor=BLUEPRINT_HIGHLIGHT,
                                  edgecolor='none',
                                  alpha=0.3)
                ax.add_patch(row_bg)
            
            # Draw cells
            ax.text(x_positions[0], y, partition, ha='left', va='center',
                   color=BLUEPRINT_FG, fontsize=8, family='monospace')
            ax.text(x_positions[1], y, port, ha='left', va='center',
                   color=BLUEPRINT_FG, fontsize=8, family='monospace')
            
            # Direction with arrow
            dir_color = BLUEPRINT_ACCENT if direction == "SRC" else BLUEPRINT_FG
            ax.text(x_positions[2], y, direction, ha='left', va='center',
                   color=dir_color, fontsize=8, weight='bold')
            
            # Type with color coding
            type_color = '#90be6d' if ptype == "Queue" else '#f9c74f'
            ax.text(x_positions[3], y, ptype, ha='left', va='center',
                   color=type_color, fontsize=8, weight='bold')
        
        # Legend
        legend_y = 2.5
        ax.text(1, legend_y, "Legend:", ha='left', va='center',
               color=BLUEPRINT_ACCENT, fontsize=9, weight='bold')
        ax.text(1, legend_y-0.5, "SRC = Source | DST = Destination", ha='left', va='center',
               color=BLUEPRINT_FG, fontsize=8)
        ax.text(1, legend_y-1.0, "ARINC-653 Port Types:", ha='left', va='center',
               color=BLUEPRINT_FG, fontsize=8)
        ax.text(1.5, legend_y-1.4, "• Sampling (periodic)", ha='left', va='center',
               color='#f9c74f', fontsize=7)
        ax.text(1.5, legend_y-1.8, "• Queueing (event-driven)", ha='left', va='center',
               color='#90be6d', fontsize=7)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150, facecolor=BLUEPRINT_BG)
        plt.close()
        
    def generate_a653_schedule(self, filename):
        """Generate ARINC-653 Schedule diagram"""
        fig, ax = plt.subplots(figsize=(16, 9))
        self.setup_blueprint_style(fig, ax)
        
        # Title
        ax.text(8, 8.5, "ARINC-653 Schedule — ATA-42", 
               ha='center', va='center',
               color=BLUEPRINT_FG, fontsize=16, weight='bold')
        
        # Timeline base
        timeline_y = 5
        timeline_start_x = 2
        timeline_end_x = 14
        timeline_length = timeline_end_x - timeline_start_x
        
        # Draw timeline
        ax.plot([timeline_start_x, timeline_end_x], [timeline_y, timeline_y],
               color=BLUEPRINT_LINE, linewidth=3)
        
        # Major frame annotation
        ax.text(8, 7.5, "Major Frame: 100 ms", ha='center', va='center',
               color=BLUEPRINT_ACCENT, fontsize=12, weight='bold')
        
        # Windows
        windows = [
            ("W1: IIS.MAL-EEM", 0, 20, '#e63946'),
            ("W2: IIS.SwarmCore", 20, 40, '#2a9d8f'),
            ("W3: IIS.MissionPlanner", 60, 40, '#e9c46a'),
        ]
        
        for name, start, duration, color in windows:
            # Calculate x positions
            x_start = timeline_start_x + (start / 100.0) * timeline_length
            width = (duration / 100.0) * timeline_length
            
            # Draw window box
            window_box = Rectangle((x_start, timeline_y - 0.5), width, 1.5,
                                   facecolor=color,
                                   edgecolor=BLUEPRINT_LINE,
                                   linewidth=2,
                                   alpha=0.6)
            ax.add_patch(window_box)
            
            # Window label
            ax.text(x_start + width/2, timeline_y + 0.25, name,
                   ha='center', va='center',
                   color=BLUEPRINT_FG, fontsize=9, weight='bold')
            
            # Time markers
            ax.text(x_start, timeline_y - 0.8, f"{start}ms",
                   ha='center', va='top',
                   color=BLUEPRINT_ACCENT, fontsize=8)
            ax.plot([x_start, x_start], [timeline_y - 0.5, timeline_y - 0.7],
                   color=BLUEPRINT_LINE, linewidth=1)
        
        # End marker
        ax.text(timeline_end_x, timeline_y - 0.8, "100ms",
               ha='center', va='top',
               color=BLUEPRINT_ACCENT, fontsize=8)
        ax.plot([timeline_end_x, timeline_end_x], [timeline_y - 0.5, timeline_y - 0.7],
               color=BLUEPRINT_LINE, linewidth=1)
        
        # Resource budgets table
        table_y = 3
        ax.text(8, table_y + 0.5, "Resource Budgets (Initial)", ha='center', va='center',
               color=BLUEPRINT_ACCENT, fontsize=11, weight='bold')
        
        budgets = [
            ("IIS.SwarmCore", "CPU 5%", "Mem 5120 KB"),
            ("IIS.MAL-EEM", "CPU 3%", "Mem 4096 KB"),
            ("IIS.MissionPlanner", "CPU 4%", "Mem 4096 KB"),
            ("IIS.CMSAdapter", "CPU 2%", "Mem 2048 KB"),
        ]
        
        y = table_y - 0.3
        for partition, cpu, mem in budgets:
            y -= 0.5
            ax.text(4, y, partition, ha='left', va='center',
                   color=BLUEPRINT_FG, fontsize=8, family='monospace')
            ax.text(9, y, cpu, ha='left', va='center',
                   color=BLUEPRINT_ACCENT, fontsize=8)
            ax.text(11, y, mem, ha='left', va='center',
                   color=BLUEPRINT_ACCENT, fontsize=8)
        
        # Health manager note
        hm_note = FancyBboxPatch((1, 6.5), 4, 1,
                                boxstyle="round,pad=0.1",
                                edgecolor=BLUEPRINT_ACCENT,
                                facecolor=BLUEPRINT_BG,
                                linewidth=2,
                                linestyle='--')
        ax.add_patch(hm_note)
        ax.text(3, 7, "Health Manager:", ha='center', va='center',
               color=BLUEPRINT_ACCENT, fontsize=8, weight='bold')
        ax.text(3, 6.7, "Async execution\nin platform context", ha='center', va='center',
               color=BLUEPRINT_FG, fontsize=7)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150, facecolor=BLUEPRINT_BG)
        plt.close()
        
    def generate_compliance_matrix(self, filename):
        """Generate Compliance Matrix diagram"""
        fig, ax = plt.subplots(figsize=(16, 9))
        self.setup_blueprint_style(fig, ax)
        
        # Title
        ax.text(8, 8.5, "Compliance Matrix — ATA-42", 
               ha='center', va='center',
               color=BLUEPRINT_FG, fontsize=16, weight='bold')
        
        # Column headers
        headers = ["Artefact", "DO-178C/DO-297", "DO-326A/356A"]
        x_positions = [1, 7, 12]
        for header, x in zip(headers, x_positions):
            ax.text(x, 7.5, header, ha='left', va='center',
                   color=BLUEPRINT_ACCENT, fontsize=10, weight='bold')
        
        # Compliance mappings
        mappings = [
            ("partition.xml", "SW Config Item", "Security Risk Assessment"),
            ("schedule.xml", "SW Config Item", "Partition Security Obj."),
            ("manifest.yaml", "Configuration Mgmt", "SBOM & Integrity"),
            ("Test Plans", "Verification Standards", "Security Test Objectives"),
            ("Test Reports", "Verification Results", "Security Test Evidence"),
            ("Coverage Reports", "Structural Coverage", "Code Security Analysis"),
            ("APEX Interface Spec", "SW Requirements", "Interface Security Spec"),
            ("Health Monitoring", "Error Detection", "Fault Containment"),
        ]
        
        y_start = 7.0
        for i, (artefact, do178, do326) in enumerate(mappings):
            y = y_start - i * 0.65
            
            # Draw row background
            if i % 2 == 0:
                row_bg = Rectangle((0.5, y-0.27), 15, 0.55,
                                  facecolor=BLUEPRINT_HIGHLIGHT,
                                  edgecolor='none',
                                  alpha=0.3)
                ax.add_patch(row_bg)
            
            # Artefact name
            ax.text(x_positions[0], y, artefact, ha='left', va='center',
                   color=BLUEPRINT_FG, fontsize=9, weight='bold',
                   family='monospace')
            
            # DO-178C/DO-297 objective
            ax.text(x_positions[1], y, do178, ha='left', va='center',
                   color=BLUEPRINT_FG, fontsize=8)
            
            # DO-326A/356A objective
            ax.text(x_positions[2], y, do326, ha='left', va='center',
                   color=BLUEPRINT_FG, fontsize=8)
            
            # Compliance indicators (checkmarks)
            ax.text(x_positions[1] - 0.5, y, "✓", ha='center', va='center',
                   color='#90be6d', fontsize=10, weight='bold')
            ax.text(x_positions[2] - 0.5, y, "✓", ha='center', va='center',
                   color='#90be6d', fontsize=10, weight='bold')
        
        # Legend/Notes box
        notes_box = FancyBboxPatch((1, 0.5), 14, 1.2,
                                  boxstyle="round,pad=0.1",
                                  edgecolor=BLUEPRINT_ACCENT,
                                  facecolor=BLUEPRINT_BG,
                                  linewidth=2)
        ax.add_patch(notes_box)
        ax.text(8, 1.5, "Compliance Notes:", ha='center', va='center',
               color=BLUEPRINT_ACCENT, fontsize=9, weight='bold')
        ax.text(8, 1.0, "All artefacts maintained under Configuration Management per DO-178C/DO-297 | "
                       "Security objectives traced to DO-326A/356A requirements",
               ha='center', va='center',
               color=BLUEPRINT_FG, fontsize=7)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150, facecolor=BLUEPRINT_BG)
        plt.close()


def parse_copilot_image_placeholders(md_file):
    """Extract COPILOT:IMAGE placeholders from markdown file"""
    content = Path(md_file).read_text()
    lines = content.splitlines()

    placeholders = []
    in_block = False
    block_lines = []
    block_start_line = 0

    for idx, line in enumerate(lines):
        if not in_block and line.strip().startswith("<!-- COPILOT:IMAGE"):
            in_block = True
            block_lines = [line]
            block_start_line = idx + 1  # 1-based line number
        elif in_block:
            block_lines.append(line)
            if line.strip().endswith("-->"):
                # Parse the block
                block_text = "\n".join(block_lines)
                # Extract fields using simple regexes or string search
                import re
                def extract_field(field, text):
                    m = re.search(rf'{field}:\s*"([^"]+)"', text)
                    return m.group(1) if m else None
                title = extract_field("title", block_text)
                save_to = extract_field("save_to", block_text)
                prompt = extract_field("prompt", block_text)
                notes = extract_field("notes", block_text)
                placeholders.append({
                    'title': title,
                    'save_to': save_to,
                    'prompt': prompt,
                    'notes': notes,
                    'line_num': block_start_line
                })
                in_block = False
                block_lines = []
    return placeholders


def generate_ata42_diagrams(md_file):
    """Generate all diagrams for ATA-42 README"""
    placeholders = parse_copilot_image_placeholders(md_file)
    
    print(f"Found {len(placeholders)} COPILOT:IMAGE placeholders")
    
    if not placeholders:
        print("No placeholders found!")
        return
    
    # Determine output directory relative to the markdown file
    md_path = Path(md_file)
    base_dir = md_path.parent
    
    # Create generator for each placeholder
    generated_files = []
    
    for placeholder in placeholders:
        # Construct full output path
        save_path = base_dir / placeholder['save_to']
        output_dir = save_path.parent
        filename = save_path.name
        
        print(f"\nGenerating: {placeholder['title']}")
        print(f"  Output: {save_path}")
        
        # Create generator for this specific output directory
        generator = ATA42DiagramGenerator(output_dir)
        
        # Generate appropriate diagram based on filename
        if 'ima_overview' in filename:
            generator.generate_ima_overview(filename)
        elif 'repo_layout' in filename:
            generator.generate_repo_layout(filename)
        elif 'apex_port_map' in filename:
            generator.generate_apex_port_map(filename)
        elif 'a653_schedule' in filename:
            generator.generate_a653_schedule(filename)
        elif 'compliance_matrix' in filename:
            generator.generate_compliance_matrix(filename)
        else:
            print(f"  Warning: No generator found for {filename}")
            continue
        
        generated_files.append(save_path)
        print(f"  ✓ Generated successfully")
    
    return generated_files


def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python generate_ata42_diagrams.py <markdown_file>")
        sys.exit(1)
    
    md_file = sys.argv[1]
    
    if not Path(md_file).exists():
        print(f"Error: File not found: {md_file}")
        sys.exit(1)
    
    print(f"Generating ATA-42 diagrams for: {md_file}")
    
    generated_files = generate_ata42_diagrams(md_file)
    
    print(f"\n{'='*60}")
    print(f"Success! Generated {len(generated_files)} diagrams:")
    for filepath in generated_files:
        print(f"  • {filepath}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
