# LICENSES

Multi-license framework for the IDEALE-EU Federation, providing domain-appropriate licensing for different artifact types.

## Overview

The IDEALE-EU Federation uses a **multi-license strategy** to balance openness with protection of intellectual property and ensure proper attribution across diverse artifact types (software, documentation, hardware, AI/ML models).

## License Files

| License | File | Applies To | Key Characteristics |
|---------|------|------------|---------------------|
| **Apache-2.0** | [CODE_LICENSE.txt](./CODE_LICENSE.txt) | Software, scripts, source code | Permissive with patent grant, contributor-friendly |
| **CC-BY-4.0** | [DOCS_LICENSE.txt](./DOCS_LICENSE.txt) | Documentation, technical publications | Attribution required, derivatives allowed |
| **CERN-OHL-S-2.0** | [HARDWARE_LICENSE.txt](./HARDWARE_LICENSE.txt) | Hardware designs, CAD models, schematics | Strong reciprocal (share-alike), prevents proprietization |
| **OpenRAIL** | [MODELS_LICENSE.txt](./MODELS_LICENSE.txt) | AI/ML models, trained weights | Responsible AI with use restrictions |

## Usage Guidelines

### Determining Which License Applies

When contributing or using artifacts from this repository:

1. **Software/Code**: Check for `LICENSE` header in source files or `licenses.code` field in `index.extracted.yaml`
2. **Documentation**: Check for license notice at end of document or `licenses.docs` field
3. **Hardware**: Check CAD file metadata or `licenses.hardware` field
4. **AI/ML Models**: Check model card or `licenses.models` field in manifest

### Default Assignments

In the absence of specific license declarations:

- **Code** (`.py`, `.js`, `.rs`, `.cpp`, etc.) → Apache-2.0
- **Documentation** (`.md`, `.rst`, `.tex`, etc.) → CC-BY-4.0
- **Hardware** (`.step`, `.iges`, `.kicad`, etc.) → CERN-OHL-S-2.0
- **Models** (`.onnx`, `.pt`, `.h5`, etc.) → OpenRAIL

### Mixed-License Projects

Some products may contain artifacts under different licenses. In such cases:

1. Each artifact type is governed by its specific license
2. The `index.extracted.yaml` manifest declares all applicable licenses
3. SBOM files include license information for all dependencies
4. Distribution packages must include all applicable license texts

## Compliance Requirements

### For Contributors

When contributing, you must:

1. ✅ Accept the [Contributor License Agreement (CLA)](../CONTRIBUTING.md#contributor-license-agreement)
2. ✅ Declare any third-party dependencies and their licenses
3. ✅ Ensure your contributions are compatible with the target license
4. ✅ Include proper license headers in source files
5. ✅ Update SBOM files when adding dependencies

### For Users/Adopters

When using artifacts from this repository:

1. ✅ Review and comply with the applicable license terms
2. ✅ Provide proper attribution (especially for CC-BY-4.0 docs)
3. ✅ Share modifications under the same license (for CERN-OHL-S-2.0 hardware)
4. ✅ Respect use restrictions (for OpenRAIL models)
5. ✅ Include license texts in distributions

## License Compatibility

### Inbound (Dependencies)

Compatible licenses for dependencies:

- **For Code**: MIT, BSD, Apache-2.0, LGPL (with dynamic linking)
- **For Docs**: CC0, CC-BY, Public Domain
- **For Hardware**: CERN-OHL-W, CERN-OHL-S, TAPR OHL
- **For Models**: OpenRAIL, BigScience RAIL, CreativeML OpenRAIL

⚠️ **Incompatible**: GPL (code), CC-BY-NC/ND (docs), proprietary licenses without permission

### Outbound (Derivatives)

When creating derivative works:

- **Apache-2.0**: Can relicense derivatives (but must preserve notices)
- **CC-BY-4.0**: Must use compatible license (CC-BY-4.0 or more permissive)
- **CERN-OHL-S-2.0**: Must use same license (strong copyleft)
- **OpenRAIL**: Must use compatible RAIL license

## Patent Grants

### Apache-2.0 (Code)

Includes **express patent grant** covering contributions:
- Contributors grant patent licenses for their contributions
- Patent retaliation clause (license terminates if you sue)
- Protects users from patent infringement claims

### CERN-OHL-S-2.0 (Hardware)

Includes **implicit patent grant** for licensed designs:
- Patent claims covering the design are licensed
- Modifications must be shared under same license
- Prevents patent ambush on open hardware

### CC-BY-4.0 (Documentation)

**No express patent grant** but:
- Sui generis database rights granted
- License survives patent claims
- Use at your own risk regarding patents

### OpenRAIL (Models)

**No patent grant** but includes:
- Use restrictions for responsible AI
- Downstream propagation requirements
- Attribution and source disclosure

## Special Considerations

### Export Control

Some artifacts may be subject to export control regulations (ITAR/EAR/EU Dual-Use) **in addition to** license terms. Check:

- [policies/EXPORT_CONTROL.md](../policies/EXPORT_CONTROL.md)
- `export_control` field in domain manifests
- Classification markings on artifacts

**Export-controlled artifacts cannot be distributed to certain countries/entities even if licensed openly.**

### Data Classification

Artifacts are classified as OPEN/SHARED/RESTRICTED/CONTROLLED. See:

- [policies/DATA_CLASSIFICATION.md](../policies/DATA_CLASSIFICATION.md)

**License terms apply only to OPEN artifacts. Other classifications have additional access restrictions.**

### Privacy & GDPR

When artifacts contain personal data:

- Follow [policies/PRIVACY.md](../policies/PRIVACY.md)
- Anonymize or pseudonymize data where possible
- Obtain consent for data collection/processing
- Respect data subject rights (access, deletion, portability)

## Resources

### License Texts

- Apache-2.0: https://www.apache.org/licenses/LICENSE-2.0
- CC-BY-4.0: https://creativecommons.org/licenses/by/4.0/
- CERN-OHL-S-2.0: https://ohwr.org/cern_ohl_s_v2.txt
- OpenRAIL: https://www.licenses.ai/blog/2022/8/18/naming-convention-of-responsible-ai-licenses

### Compatibility Matrices

- SPDX License List: https://spdx.org/licenses/
- Choose a License: https://choosealicense.com/
- OSI Approved Licenses: https://opensource.org/licenses/

### Federation Contacts

- **Licensing Questions**: legal@ideale-eu.example
- **CLA Support**: cla@ideale-eu.example
- **IP Issues**: ip@ideale-eu.example

---

**Version**: 1.0.0  
**Last Updated**: 2025-01-01  
**Maintained By**: IDEALE-EU Legal Working Group

For questions about licensing, open a [GitHub Discussion](https://github.com/Robbbo-T/ASI-T2/discussions) or contact legal@ideale-eu.example.
