# IETP - Interactive Electronic Technical Publication

The Interactive Electronic Technical Publication (IETP) provides a modern web-based interface for browsing, searching, and managing S1000D content.

## IETP Overview

### Purpose
The IETP transforms static S1000D XML into an intuitive, interactive web interface that enables:
- Efficient navigation through technical content
- Real-time search and filtering capabilities
- Integration with authoring tools (GenCMS)
- Visual content management and status tracking

### Architecture
- **Static Site Generator**: Python-based build system (`build_ietp.py`)
- **Client-Side Enhancement**: JavaScript for filtering and search (`ietp.js`)
- **Responsive Design**: Works on desktop and mobile devices
- **Dark Theme**: Professional appearance matching technical documentation standards

## Building the IETP

### Build Process
```bash
# Navigate to IETP directory
cd PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/ATA-57/S1000D/ietp

# Build the static site
python3 build_ietp.py
```

### Build Output
```
ietp/site/
├── index.html              # Main landing page
├── subsystem/              # Subsystem pages
│   ├── 57-10.html          # Wing Structure
│   ├── 57-20.html          # Fuel Interfaces  
│   ├── 57-30.html          # Control Surfaces
│   ├── 57-40.html          # High-Lift
│   └── 57-50.html          # Equipment Integration
├── dm/                     # Individual data module pages
│   ├── DMC-BWQ1-A-57-10-00-00-00A-040A-D-EN-US.html
│   └── ...
├── assets/                 # CSS, JavaScript, and other assets
│   ├── css/
│   ├── js/
│   └── images/
└── site_index.json         # Search index for client-side search
```

### Data Sources
The IETP build process reads from:
- **DMRL**: `publication_modules/DML-BWQ1-ATA57-00_EN-US.xml`
- **DM Index**: `indices/dm_index.xml`
- **Data Modules**: `data_modules/` (for content rendering)

## Navigation Features

### Landing Page
The main index page displays ATA-57 subsystems as interactive cards:

```html
<div class="subsystem-cards">
  <a href="subsystem/57-10.html" class="subsystem-card">
    <div class="card-header">57-10 Wing Structure</div>
    <div class="card-info">10 modules</div>
  </a>
  <!-- Additional subsystem cards -->
</div>
```

### Subsystem Pages
Each subsystem page organizes content by information code buckets:

#### Information Code Categories
- **DESCRIPTION**: IC 040, 042, 034, 050–056
- **TESTS**: IC 310, 345, 350  
- **REMOVAL (5xx)**: IC 500-599
- **INSTALL/RIG (7xx)**: IC 700-799
- **SERVICING (6xx)**: IC 600-699
- **FI-GENERAL**: IC 420
- **FI-SPECIFIC**: IC 421–428
- **IPD/PARTS**: IC 900, 910

### Data Module Pages
Individual DM pages display:
- Module metadata (DMC, information code, category)
- Rendered content from XML (when available)
- Links to related modules
- GenCMS integration button
- Source file information

## Interactive Features

### Category Filtering
Click category buttons to filter content by information code type:

```javascript
// Category filter implementation
function filterByCategory(category) {
  const modules = document.querySelectorAll('.module-entry');
  modules.forEach(module => {
    const moduleCategory = module.dataset.category;
    module.style.display = (category === 'all' || moduleCategory === category) ? 'block' : 'none';
  });
}
```

### Quick Search
Real-time search across titles and DM keys:

```javascript
// Search implementation
function performSearch(searchTerm) {
  const modules = document.querySelectorAll('.module-entry');
  const term = searchTerm.toLowerCase();
  
  modules.forEach(module => {
    const title = module.querySelector('.module-title').textContent.toLowerCase();
    const dmKey = module.querySelector('.dm-key').textContent.toLowerCase();
    const matches = title.includes(term) || dmKey.includes(term);
    module.style.display = matches ? 'block' : 'none';
  });
}
```

### Status Indicators
Visual indicators show module authoring status:
- **🟢 authored**: Module has been written and contains actual content
- **🟡 pending**: Module structure exists but needs content development
- **🔴 missing**: Required by DMRL but not yet created

## Content Rendering

### Authored Modules
For authored modules, IETP extracts and renders:
- Module title and description
- Structured paragraphs and lists
- Cross-references to other modules
- Multimedia object references

```python
# Content extraction example
def extract_content(dm_xml):
    content = []
    
    # Extract description paragraphs
    for para in dm_xml.findall('.//para'):
        content.append(f"<p>{para.text}</p>")
    
    # Extract lists
    for list_item in dm_xml.findall('.//listItem'):
        content.append(f"<li>{list_item.text}</li>")
    
    return '\n'.join(content)
```

### Pending/Missing Modules
For modules not yet authored:
- Show placeholder indicating development status
- Display DMRL requirements
- Provide GenCMS button for content creation

## GenCMS Integration

### GenCMS Button
The "✳︎ Generate draft with GenCMS" button appears on all DM pages:

```html
<div class="topbar">
  <a href="../index.html">BWB-H₂ Q100 IETP</a>
  <a href="../subsystem/57-10.html">← 57-10 Wing Structure</a>
  <button id="gencms-btn" class="chip">✳︎ Generate draft with GenCMS</button>
</div>
```

### Automatic Context Detection
GenCMS automatically detects:
- Current data module code and metadata
- Information code category for appropriate content structure
- Related modules for cross-referencing
- Applicable BREX rules and safety requirements

### Integration Workflow
1. **Context Analysis**: Extract DM metadata from current page
2. **GenCMS Panel**: Display generation form with prefilled context
3. **Content Generation**: Create S1000D-compliant content
4. **Preview**: Show generated XML in IETP interface
5. **Promotion**: Move approved content to CSDB

## IPC Viewer for IPD Modules

### Interactive Parts Catalog
For IC 900/910 modules, IETP includes an enhanced IPC viewer:

#### Features
- **Interactive Illustrations**: Click parts to highlight in parts list
- **Part Search**: Search by part number or description  
- **Assembly Navigation**: Drill down from assemblies to components
- **Effectivity Filtering**: Show parts for specific configurations

#### Generate Illustration Button
Special functionality for IPD modules:

```javascript
// Generate Illustration feature
document.getElementById('generate-illustration').onclick = async () => {
  const partsList = extractPartsList();
  const prompt = createIllustrationPrompt(partsList);
  const illustration = await generateIllustration(prompt);
  updateModuleWithIllustration(illustration);
};
```

### IPC Display Structure
```html
<div class="ipc-viewer">
  <div class="ipc-illustration">
    <img src="../../multimedia/graphics/ICN-BWQ1-A-571010-A-001-01.svg" 
         alt="Wing box assembly" usemap="#partsMap">
    <map name="partsMap">
      <area shape="circle" coords="100,150,20" data-callout="1">
      <area shape="circle" coords="200,180,20" data-callout="2">
    </map>
  </div>
  
  <div class="ipc-parts-list">
    <table class="parts-table">
      <thead>
        <tr>
          <th>Item</th>
          <th>Part Number</th>
          <th>Description</th>
          <th>Qty</th>
        </tr>
      </thead>
      <tbody>
        <tr data-callout="1">
          <td>1</td>
          <td>BWQ1-57-1001-001</td>
          <td>Wing box assembly</td>
          <td>1</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

## Responsive Design

### Mobile Optimization
- **Collapsible Navigation**: Touch-friendly menu system
- **Optimized Typography**: Readable text on small screens
- **Touch Interactions**: Appropriate button sizing for touch interfaces
- **Progressive Enhancement**: Core functionality works without JavaScript

### Desktop Features
- **Multi-Column Layout**: Efficient use of screen real estate
- **Keyboard Navigation**: Full keyboard accessibility
- **Advanced Search**: Complex filtering and search capabilities
- **Multi-Tab Support**: Open multiple modules simultaneously

## Deployment and Hosting

### Static Hosting
IETP generates pure HTML/CSS/JS that can be hosted on any web server:
- **Local Development**: `python3 -m http.server 8080`
- **CI/CD Integration**: Automatic builds on content updates
- **CDN Distribution**: Optimized for global content delivery

### CI Integration Example
```yaml
# .github/workflows/build-ietp.yml
- name: Build IETP
  working-directory: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/ATA-57/S1000D/ietp
  run: python3 build_ietp.py

- name: Upload IETP Artifact
  uses: actions/upload-artifact@v4
  with:
    name: IETP-ATA57
    path: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/ATA-57/S1000D/ietp/site
```

## Performance Optimization

### Build Time Optimization
- **Incremental Builds**: Only regenerate changed modules
- **Parallel Processing**: Multi-threaded content processing
- **Template Caching**: Reuse generated templates
- **Asset Optimization**: Minified CSS and JavaScript

### Runtime Optimization
- **Client-Side Search Index**: Pre-built search index for fast queries
- **Lazy Loading**: Load content on demand for large publications
- **Caching Strategy**: Appropriate cache headers for static content
- **Progressive Loading**: Load critical content first

## Customization and Extension

### Theme Customization
Modify `assets/css/ietp.css` for visual customization:
- Color scheme adjustments
- Typography modifications
- Layout variations
- Brand-specific styling

### Functionality Extension
Extend `assets/js/ietp.js` for additional features:
- Advanced search capabilities
- Custom filtering options
- Integration with external systems
- Enhanced interactivity

### Template Modification
Customize HTML templates in `build_ietp.py`:
- Page layout changes
- Additional metadata display
- Custom navigation elements
- Integration hooks

## Checklist

### IETP Setup
- [ ] Python 3.9+ available for build process
- [ ] All data sources accessible (DMRL, indices, data modules)
- [ ] Output directory writable
- [ ] Required dependencies available (defusedxml optional)

### Content Integration
- [ ] DMRL entries properly structured
- [ ] DM index current and accurate
- [ ] Multimedia objects accessible
- [ ] Cross-references validated
- [ ] GenCMS integration functional

### Quality Assurance
- [ ] All links functional in generated site
- [ ] Search functionality working correctly
- [ ] Mobile responsiveness verified
- [ ] Browser compatibility tested
- [ ] Performance benchmarks met

### Deployment
- [ ] Build process integrated into CI/CD
- [ ] Hosting infrastructure configured
- [ ] Update procedures documented
- [ ] Backup and recovery procedures established

## Common Mistakes

❌ **Outdated Indices**: Building IETP with stale index data  
✅ **Correct**: Regenerate indices before IETP build to ensure current content

❌ **Missing Cross-References**: IETP shows broken links between modules  
✅ **Correct**: Validate all cross-references during build process

❌ **Poor Mobile Experience**: Site not optimized for mobile devices  
✅ **Correct**: Test thoroughly on mobile devices and optimize touch interactions

❌ **Slow Search Performance**: Client-side search too slow for large datasets  
✅ **Correct**: Optimize search index and implement progressive search features

❌ **GenCMS Integration Failure**: GenCMS button not working on DM pages  
✅ **Correct**: Ensure GenCMS assets are properly included and API endpoints accessible

---

**Last Updated**: 2025-01-21  
**S1000D Version**: 6.0