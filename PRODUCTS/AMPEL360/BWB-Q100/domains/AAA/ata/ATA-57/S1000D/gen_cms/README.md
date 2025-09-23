# GenCMS - Generative Content Management System for S1000D

GenCMS is a generative content management system that enables authors to draft S1000D-compliant Data Modules directly from the IETP (Interactive Electronic Technical Publication) interface.

## Features

- **AI-Powered Content Generation**: Uses LLM providers (OpenAI, Azure OpenAI, or local models) to generate S1000D-compliant XML content
- **BREX and CSDB Rules Integration**: Automatically incorporates project-specific BREX rules and CSDB requirements
- **IETP Integration**: Seamless UI panel that appears on any DM page in the IETP
- **Draft Management**: Generates drafts in staging area, allows review and promotion to CSDB
- **Guardrailed Content**: Ensures generated content follows S1000D Issue 6.0 standards and BWQ1 project requirements

## Architecture

### Backend API (`gen_cms/server/app.py`)
- **FastAPI-based REST API** with endpoints:
  - `GET /health` - Health check
  - `POST /generate` - Generate draft DM content
  - `POST /promote` - Promote draft to CSDB
- **LLM Provider abstraction** supporting:
  - OpenAI (set `GENCMS_PROVIDER=openai` and `OPENAI_API_KEY`)
  - Mock provider (set `GENCMS_PROVIDER=mock` for testing)
- **Automatic rule injection** from:
  - BREX DM content (`data_modules/descriptive/*-022A-*.xml`)
  - CSDB rules (`metadata/csdb_rules.xml`)
  - CIR terminology (`common_information/terminology/CIR-BWQ1-00001.xml`)

### Frontend UI
- **JavaScript panel** (`ietp/assets/js/gencms.js`) - Dynamic UI component
- **CSS styling** (`ietp/assets/css/gencms.css`) - Dark theme consistent with IETP
- **IETP integration** - Automatically appears on DM pages with generate button

## Installation and Usage

### 1. Install Dependencies
```bash
cd gen_cms/server
pip install fastapi uvicorn requests
```

### 2. Start the API Server
```bash
# For testing with mock provider (no API key required)
export GENCMS_PROVIDER=mock
python3 -c "
import uvicorn
from app import app
uvicorn.run(app, host='0.0.0.0', port=8000)
"

# For production with OpenAI
export GENCMS_PROVIDER=openai
export OPENAI_API_KEY=sk-your-key-here
export GENCMS_OPENAI_MODEL=gpt-4o-mini  # optional
python3 -c "
import uvicorn  
from app import app
uvicorn.run(app, host='0.0.0.0', port=8000)
"
```

### 3. Build IETP
The GenCMS assets are automatically included when building the IETP:
```bash
python3 ietp/build_ietp.py
```

### 4. Access GenCMS
1. Open any DM page in the IETP (e.g., `ietp/site/dm/DMC-BWQ1-A-57-10-00-00-00A-040A-D-EN-US.html`)
2. Click the "✳︎ Generate draft with GenCMS" button in the top bar
3. Fill in the form with:
   - **Objective**: What the DM should cover
   - **Constraints**: Standards, scope, limits
   - **Seed outline**: Optional structure outline
   - **Safety focus**: Relevant safety considerations
4. Click "Generate" to create draft content
5. Review the generated XML
6. Click "Promote to CSDB" to move the draft to the appropriate bucket in `data_modules/`

## Generated Content Structure

GenCMS generates complete S1000D-compliant DM files with:

- **Proper DMC structure** based on the source DM key
- **BREX reference** automatically included
- **Classification string** set to "INTERNAL–EVIDENCE-REQUIRED" (en dash)
- **Schema-appropriate content** based on IC family:
  - IC 040, 042, 034: Descriptive content
  - IC 345, 350: Test procedures with acceptance criteria
  - IC 5xx, 7xx: Procedural content with safety warnings
  - IC 420, 421-428: Fault isolation procedures
  - IC 900, 910: IPD content

## Configuration

### Environment Variables
- `GENCMS_PROVIDER` - LLM provider ("openai" or "mock")
- `OPENAI_API_KEY` - OpenAI API key (required for openai provider)
- `GENCMS_OPENAI_MODEL` - OpenAI model (default: "gpt-4o-mini")
- `GENCMS_TEMPERATURE` - Generation temperature (default: "0.2")
- `OPENAI_BASE` - Custom OpenAI base URL (for Azure OpenAI)

### Files Used
- **DMRL**: `publication_modules/DML-BWQ1-ATA57-00_EN-US.xml`
- **BREX**: `data_modules/descriptive/DMC-BWQ1-*-022A-*-EN-US.xml`
- **CSDB Rules**: `metadata/csdb_rules.xml`
- **CIR Terminology**: `common_information/terminology/CIR-BWQ1-00001.xml`
- **Draft Storage**: `gen_cms/drafts/`

## Integration with Validation Pipeline

GenCMS-generated content is designed to work with the existing validation pipeline:
- Files are promoted to the correct bucket (`descriptive`, `procedural`, `fault`, `ipd`)
- Schema references are automatically set based on IC family
- Classification strings use proper en-dashes
- BREX references are automatically included
- Index regeneration is triggered on promotion

## Extending GenCMS

### Adding New LLM Providers
Implement the `LLMProvider` interface in `app.py`:
```python
class MyProvider(LLMProvider):
    def complete(self, system: str, prompt: str) -> str:
        # Your implementation
        return generated_content
```

### Customizing Content Generation
Modify the `compose_prompt()` function to:
- Add new rule sources
- Customize IC-specific guidance
- Include additional context

### UI Customization
- Modify `gencms.js` for functionality changes
- Update `gencms.css` for styling changes
- The panel automatically appears on any page with `.dm-article .meta code`