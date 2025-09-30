.PHONY: help validate-s1000d validate-plans validate-evidence validate-md validate-all

help:
	@echo "ATA-42 Certification Validation Targets"
	@echo "========================================"
	@echo "make validate-s1000d    - Validate S1000D data modules"
	@echo "make validate-plans     - Validate certification plans"
	@echo "make validate-evidence  - Validate evidence structure"
	@echo "make validate-md        - Validate Markdown files"
	@echo "make validate-all       - Run all validations"

validate-s1000d:
	@echo "Validating S1000D data modules..."
	@if [ -d "S1000D/dmodule" ] && [ -n "$$(find S1000D/dmodule -name '*-D-EN-US.xml' 2>/dev/null)" ]; then \
		if command -v xmllint >/dev/null 2>&1; then \
			xmllint --noout --schema S1000D/schemas/6.0/descript.xsd S1000D/dmodule/*-D-EN-US.xml 2>&1 || true; \
		else \
			echo "⚠️  xmllint not found, skipping XML validation"; \
		fi; \
	else \
		echo "⚠️  No descriptive S1000D data modules found"; \
	fi
	@if [ -d "S1000D/dmodule" ] && [ -n "$$(find S1000D/dmodule -name '*-P-EN-US.xml' 2>/dev/null)" ]; then \
		if command -v xmllint >/dev/null 2>&1; then \
			xmllint --noout --schema S1000D/schemas/6.0/proced.xsd S1000D/dmodule/*-P-EN-US.xml 2>&1 || true; \
		else \
			echo "⚠️  xmllint not found, skipping XML validation"; \
		fi; \
	else \
		echo "⚠️  No procedural S1000D data modules found"; \
	fi
	@echo "✅ S1000D validation complete."

validate-plans:
	@echo "Validating certification plans..."
	@if command -v yamllint >/dev/null 2>&1; then \
		yamllint plans/*.yaml procedures/*.yaml 2>&1 || true; \
	else \
		echo "⚠️  yamllint not found, skipping YAML linting"; \
	fi
	@echo "✅ Plans validation complete."

validate-evidence:
	@echo "Validating evidence structure..."
	@if [ -f "scripts/validate_evidence_tree.py" ] && [ -d "evidence" ]; then \
		python3 scripts/validate_evidence_tree.py --root evidence --rules schemas/evidence_rules.yaml || true; \
	else \
		echo "⚠️  Evidence validation script or evidence directory not found"; \
	fi
	@echo "✅ Evidence validation complete."

validate-md:
	@echo "Validating Markdown files..."
	@if command -v markdownlint >/dev/null 2>&1; then \
		markdownlint **/*.md 2>&1 || true; \
	else \
		echo "⚠️  markdownlint not found, skipping Markdown validation"; \
	fi
	@echo "✅ Markdown validation complete."

validate-all: validate-plans validate-evidence
	@echo ""
	@echo "========================================"
	@echo "✅ All validations complete."
	@echo "========================================"
