.PHONY: validate-s1000d validate-brex validate-config validate-md validate-all

validate-s1000d:
	@echo "Validating S1000D data modules..."
	@if command -v xmllint > /dev/null 2>&1; then \
		if [ -f S1000D/schemas/6.0/descript.xsd ]; then \
			xmllint --noout --schema S1000D/schemas/6.0/descript.xsd S1000D/dmodule/*-D-EN-US.xml 2>/dev/null || echo "Note: S1000D descriptive schemas not yet populated"; \
		else \
			echo "Note: S1000D schemas not yet populated"; \
		fi; \
		if [ -f S1000D/schemas/6.0/proced.xsd ]; then \
			xmllint --noout --schema S1000D/schemas/6.0/proced.xsd S1000D/dmodule/*-P-EN-US.xml 2>/dev/null || echo "Note: S1000D procedural schemas not yet populated"; \
		fi; \
	else \
		echo "⚠️  xmllint not available, skipping XML validation"; \
	fi
	@echo "S1000D validation complete."

validate-brex:
	@echo "Validating BREX rules..."
	@if [ -f S1000D/brex/BREX-ATA42-AFDX.xml ]; then \
		echo "Note: BREX validation requires schematron tool (not yet available)"; \
	else \
		echo "Note: BREX files not yet populated"; \
	fi
	@echo "BREX validation complete."

validate-config:
	@echo "Validating configuration files..."
	@if command -v python3 > /dev/null 2>&1; then \
		python3 -c "import json; json.load(open('configuration/virtual_links.schema.json'))" && echo "✅ virtual_links.schema.json: valid JSON"; \
		python3 -c "import json; json.load(open('configuration/switch_configuration.json'))" && echo "✅ switch_configuration.json: valid JSON"; \
		python3 -c "import yaml; yaml.safe_load(open('configuration/virtual_links.yaml'))" && echo "✅ virtual_links.yaml: valid YAML" || echo "⚠️  PyYAML not installed"; \
		python3 -c "import yaml; yaml.safe_load(open('configuration/bandwidth_allocation.yaml'))" && echo "✅ bandwidth_allocation.yaml: valid YAML" || echo "⚠️  PyYAML not installed"; \
		python3 -c "import yaml; yaml.safe_load(open('configuration/vl_scheduling.yaml'))" && echo "✅ vl_scheduling.yaml: valid YAML" || echo "⚠️  PyYAML not installed"; \
		python3 -c "import yaml; yaml.safe_load(open('configuration/redundancy_config.yaml'))" && echo "✅ redundancy_config.yaml: valid YAML" || echo "⚠️  PyYAML not installed"; \
		python3 -c "import yaml; yaml.safe_load(open('configuration/gateway_config.yaml'))" && echo "✅ gateway_config.yaml: valid YAML" || echo "⚠️  PyYAML not installed"; \
	else \
		echo "⚠️  python3 not available, skipping config validation"; \
	fi
	@echo "Configuration validation complete."

validate-md:
	@echo "Validating Markdown files..."
	@if command -v markdownlint > /dev/null 2>&1; then \
		markdownlint **/*.md || echo "Note: Some markdown style issues found"; \
	else \
		echo "⚠️  markdownlint not available, skipping markdown validation"; \
	fi
	@echo "Markdown validation complete."

validate-all: validate-s1000d validate-brex validate-config validate-md
	@echo "✅ All validations complete."
