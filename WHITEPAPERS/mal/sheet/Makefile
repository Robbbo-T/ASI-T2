.PHONY: help validate-schemas validate-utcs validate-all clean

help:
	@echo "MAL Build & Validation Targets"
	@echo "================================"
	@echo "make validate-schemas  - Validate all JSON schemas"
	@echo "make validate-utcs     - Validate UTCS bundle integrity"
	@echo "make validate-all      - Run all validations"
	@echo "make clean             - Remove generated files"

validate-schemas:
	@echo "Validating MAL JSON schemas..."
	@if command -v python3 >/dev/null 2>&1; then \
		for schema in ../../schemas/mal/*.json; do \
			echo "  Validating $$(basename $$schema)..."; \
			python3 -c "import json; json.load(open('$$schema'))" && echo "    ✅ Valid" || echo "    ❌ Invalid"; \
		done; \
	else \
		echo "⚠️  python3 not found, skipping JSON validation"; \
	fi
	@echo "✅ Schema validation complete."

validate-utcs:
	@echo "Validating UTCS bundle structure..."
	@echo "  Checking manifest..."
	@if [ -f "../utcs/manifest.yaml" ]; then \
		echo "    ✅ manifest.yaml exists"; \
	else \
		echo "    ❌ manifest.yaml missing"; \
	fi
	@echo "  Checking schemas..."
	@if [ -d "../../schemas/mal" ] && [ -n "$$(find ../../schemas/mal -name '*.json' 2>/dev/null)" ]; then \
		echo "    ✅ Schemas directory exists with content"; \
	else \
		echo "    ❌ Schemas directory missing or empty"; \
	fi
	@echo "  Checking documentation..."
	@if [ -f "../docs/topic_grammar.md" ] && [ -f "../docs/security_model.md" ]; then \
		echo "    ✅ Core documentation exists"; \
	else \
		echo "    ❌ Core documentation missing"; \
	fi
	@echo "  Checking style files..."
	@if [ -f "../style/mal.csl" ]; then \
		echo "    ✅ Style files exist"; \
	else \
		echo "    ⚠️  Style files missing"; \
	fi
	@echo "✅ UTCS validation complete."

validate-all: validate-schemas validate-utcs
	@echo ""
	@echo "================================"
	@echo "✅ All MAL validations complete."
	@echo "================================"

clean:
	@echo "Cleaning generated files..."
	@find .. -name "*.pyc" -delete 2>/dev/null || true
	@find .. -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@echo "✅ Clean complete."
