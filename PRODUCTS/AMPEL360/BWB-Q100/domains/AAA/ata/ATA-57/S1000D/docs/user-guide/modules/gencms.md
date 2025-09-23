# GenCMS - Generative Content Management System

GenCMS provides AI-assisted content generation with built-in S1000D compliance guardrails and BREX rules enforcement.

## Overview

The Generative Content Management System (GenCMS) integrates directly into the IETP interface, providing authors with intelligent content generation capabilities while ensuring compliance with S1000D Issue 6.0 standards and BWQ1 project requirements.

## Interface Overview

![GenCMS interface — context-aware prefill and guarded generation](multimedia/photos/gencms-interface-screenshot.png)

### Interface Elements

1. **📋 Auto-fill from context** - Automatically populates form fields based on the current data module context
2. **Objective** - What the data module should cover (scope and purpose)
3. **Constraints** - Standards, scope limits, and compliance requirements
4. **Seed outline** - Optional structure outline to guide content generation
5. **Safety focus** - Specific safety considerations (H₂, ESD, lock-out/tag-out, etc.)
6. **Generate** - Creates draft content using the specified parameters
7. **Refine** - Iteratively improves generated content
8. **Promote to CSDB** - Moves validated draft to appropriate data module bucket

## Context-Aware Prefill

### Automatic Field Population
The prefill feature analyzes the current data module context and populates form fields with intelligent defaults:

- **Information Code Analysis**: Determines appropriate content structure based on IC (040, 500, 345, etc.)
- **Subsystem Context**: Incorporates ATA-57 subsystem-specific requirements
- **Safety Considerations**: Suggests relevant safety focus areas based on component type
- **Cross-Reference Detection**: Identifies related modules for proper linking

### How Prefill Works
```javascript
// Triggered when user clicks "📋 Auto-fill from context"
1. Analyze current DM key (e.g., DMC-BWQ1-A-57-10-10-00-00A-034A-D-EN-US)
2. Extract subsystem (57-10), information code (034), and other metadata
3. Query BREX rules and CSDB requirements for context
4. Populate form fields with intelligent defaults
5. Present pre-filled form for user review and modification
```

## LLM Providers

### Supported Providers
GenCMS supports multiple LLM providers for content generation:

- **OpenAI**: Production-ready with GPT-4 models
- **Azure OpenAI**: Enterprise deployment option
- **Mock Provider**: Testing and development environment

### Environment Configuration
```bash
# OpenAI Configuration
export GENCMS_PROVIDER=openai
export OPENAI_API_KEY=sk-your-key-here
export GENCMS_OPENAI_MODEL=gpt-4o-mini
export GENCMS_TEMPERATURE=0.2

# Azure OpenAI Configuration
export GENCMS_PROVIDER=openai
export OPENAI_BASE=https://your-resource.openai.azure.com/
export OPENAI_API_KEY=your-azure-key

# Mock Provider (Testing)
export GENCMS_PROVIDER=mock
```

## BREX and CSDB Rules Integration

### Automatic Rule Injection
GenCMS automatically incorporates project-specific rules during content generation:

#### BREX Rules Source
```xml
<!-- From data_modules/descriptive/*-022A-*.xml -->
<businessRulesEx>
  <title>BWQ1 Project Business Rules</title>
  <content>
    <description>
      <para>Classification string must use en-dash: INTERNAL–EVIDENCE-REQUIRED</para>
      <para>Enterprise name must be consistent: AMPEL360</para>
      <para>Hydrogen safety considerations mandatory for fuel system procedures</para>
    </description>
  </content>
</businessRulesEx>
```

#### CSDB Rules Integration
```xml
<!-- From metadata/csdb_rules.xml -->
<csdbRules>
  <namingConvention>DMC-BWQ1-A-{system}-{subsystem}-{assembly}-{infoCode}-{variant}-EN-US</namingConvention>
  <classification>INTERNAL–EVIDENCE-REQUIRED</classification>
  <enterpriseName>AMPEL360</enterpriseName>
</csdbRules>
```

### CIR Terminology Integration
GenCMS incorporates common terminology from the CIR:

```xml
<!-- From common_information/terminology/CIR-BWQ1-00001.xml -->
<commonInfoRepository>
  <title>BWQ1 Terminology</title>
  <content>
    <definitionList>
      <definitionListItem>
        <listItemTerm>BWB-Q100</listItemTerm>
        <listItemDefinition>Blended Wing Body aircraft with hydrogen propulsion</listItemDefinition>
      </definitionListItem>
    </definitionList>
  </content>
</commonInfoRepository>
```

## Content Generation Process

### Generation Workflow
1. **Context Analysis**: Analyze current DM metadata and content requirements
2. **Rule Compilation**: Gather applicable BREX rules, CSDB requirements, and CIR terminology
3. **Prompt Construction**: Build comprehensive prompt with context, constraints, and guidelines
4. **LLM Generation**: Generate content using selected provider with appropriate temperature
5. **Guardrail Validation**: Apply post-generation validation and compliance checks
6. **Content Insertion**: Insert generated content into S1000D template structure

### Schema-Appropriate Content
GenCMS generates content appropriate for the information code family:

| IC Family | Content Type | Schema | Characteristics |
|-----------|--------------|---------|----------------|
| 040, 042, 034 | Descriptive | descript.xsd | System descriptions, technical data |
| 345, 350 | Test procedures | descript.xsd | Acceptance criteria, test steps |
| 5xx, 7xx | Procedural | proced.xsd | Safety warnings, step-by-step procedures |
| 420, 421-428 | Fault isolation | descript.xsd | Decision trees, troubleshooting |
| 900, 910 | IPD content | ipd.xsd | Parts lists, illustrations |

## Draft Management

### Draft Storage Location
```
gen_cms/drafts/
├── DMC-BWQ1-A-57-10-10-00-00A-034A-D-EN-US.xml
├── DMC-BWQ1-A-57-20-30-00-00A-350A-D-EN-US.xml
└── ...
```

### Promote to CSDB Flow
1. **Draft Validation**: Verify generated content passes schema validation
2. **BREX Compliance**: Check business rules adherence
3. **Classification Verification**: Ensure en-dash usage in classification string
4. **Bucket Assignment**: Determine target directory based on IC family
5. **File Movement**: Move from drafts to appropriate data_modules subdirectory
6. **Index Update**: Regenerate indices to include new content

```javascript
// Promotion workflow
POST /promote
{
  "draft_path": "gen_cms/drafts/DMC-BWQ1-A-57-10-10-00-00A-034A-D-EN-US.xml",
  "target_bucket": "descriptive",
  "validation_required": true
}
```

## Safety Guardrails

### Content Validation
- **Schema Compliance**: All generated content must validate against appropriate XSD
- **Classification Security**: Automatic en-dash insertion in classification strings
- **Enterprise Consistency**: Automatic AMPEL360 enterprise name usage
- **Safety Requirement**: Mandatory safety warnings for hydrogen system procedures

### Prohibited Content
GenCMS prevents generation of:
- Non-compliant S1000D markup
- Safety procedures without appropriate warnings
- Content violating BREX business rules
- Inconsistent terminology not aligned with CIR

## Usage Guidelines

### When to Use GenCMS
✅ **Appropriate Use Cases**:
- Creating initial draft content for new data modules
- Standardizing terminology across related modules
- Generating safety-compliant procedural content
- Rapid prototyping of module structure

❌ **Inappropriate Use Cases**:
- Generating final content without expert review
- Creating safety-critical procedures without validation
- Replacing subject matter expert knowledge
- Bypassing required approval processes

### Best Practices

#### Form Field Completion
- **Objective**: Be specific about scope and technical depth
- **Constraints**: Include all applicable standards and limitations
- **Seed Outline**: Provide logical structure for complex procedures
- **Safety Focus**: Specify relevant hazards and safety considerations

#### Content Review Process
1. **Technical Accuracy**: Verify all technical details against engineering data
2. **Safety Compliance**: Ensure all safety warnings are appropriate and complete
3. **Cross-Reference Validity**: Check that all referenced modules exist and are current
4. **Terminology Consistency**: Verify alignment with CIR definitions

## Troubleshooting

### Common Issues

#### Generation Fails
- **Symptom**: "Generation failed" error message
- **Causes**: Invalid API key, network issues, malformed input
- **Solutions**: Check environment variables, verify network connectivity, simplify input

#### Content Non-Compliant
- **Symptom**: Schema validation fails after generation
- **Causes**: LLM generated invalid S1000D markup
- **Solutions**: Use "Refine" function, adjust constraints, manual post-processing

#### Missing Safety Warnings
- **Symptom**: Procedural content lacks required safety elements
- **Causes**: Insufficient safety focus specification
- **Solutions**: Re-generate with explicit safety requirements, manual safety review

## Checklist

### Before Generation
- [ ] Current data module context is appropriate
- [ ] BREX rules have been reviewed for module type
- [ ] Safety requirements identified for content type
- [ ] Related modules identified for cross-referencing

### Form Completion
- [ ] Objective clearly defines scope and technical depth
- [ ] Constraints include all applicable standards
- [ ] Seed outline provides logical structure
- [ ] Safety focus specifies relevant hazards
- [ ] Prefill used to populate context-aware defaults

### After Generation
- [ ] Generated content reviewed for technical accuracy
- [ ] Schema validation passes
- [ ] BREX compliance verified
- [ ] Safety warnings appropriate and complete
- [ ] Cross-references valid and current
- [ ] Ready for promotion to CSDB

## Common Mistakes

❌ **Insufficient Context**: Using GenCMS without proper objective definition  
✅ **Correct**: Provide detailed, specific objectives with clear scope boundaries

❌ **Ignoring Safety Focus**: Generating H₂ procedures without safety considerations  
✅ **Correct**: Always specify hydrogen-specific safety requirements for fuel system content

❌ **Skipping Review**: Promoting generated content without expert validation  
✅ **Correct**: Always review generated content for technical accuracy and safety compliance

❌ **Overriding Guardrails**: Attempting to bypass BREX or CSDB rule enforcement  
✅ **Correct**: Work within established guardrails and escalate rule change requests appropriately

---

**Last Updated**: 2025-01-21  
**S1000D Version**: 6.0