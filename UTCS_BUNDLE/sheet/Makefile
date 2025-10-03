# UTCS Bundle Makefile
# Build, validate, and bundle operations for UTCS v5.0

.PHONY: all validate bundle clean sbom check help

BUNDLE_ID := utcs-bundle-bwb-q100-2025-10-03
MANIFEST := manifest.utcs.yaml
PYTHON := python3

all: validate

help:
	@echo "UTCS v5.0 Bundle Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  validate       - Validate manifest and bundle structure"
	@echo "  validate-full  - Full validation including crosswalk checks"
	@echo "  bundle         - Create bundle archive"
	@echo "  sbom           - Generate SBOM (requires syft)"
	@echo "  check          - Run all checks"
	@echo "  clean          - Remove generated files"
	@echo "  help           - Show this help message"

validate:
	@echo "==> Validating UTCS bundle..."
	$(PYTHON) sheet/ci/validate_utcs.py --manifest $(MANIFEST)

validate-full: validate
	@echo "==> Running full validation with crosswalk checks..."
	$(PYTHON) sheet/ci/validate_utcs.py --manifest $(MANIFEST) --check-crosswalk

sbom:
	@echo "==> Generating SBOM..."
	@if command -v syft > /dev/null 2>&1; then \
		syft dir:. -o spdx-json > attestations/sbom.spdx.json; \
		echo "SBOM generated: attestations/sbom.spdx.json"; \
	else \
		echo "WARNING: syft not found. Creating placeholder SBOM..."; \
		$(PYTHON) sheet/ci/generate_placeholder_sbom.py; \
	fi

check: validate-full
	@echo "==> Checking schemas..."
	@for schema in content/schemas/*.json; do \
		echo "Validating: $$schema"; \
		jq '.' "$$schema" > /dev/null || exit 1; \
	done
	@echo "==> All checks passed!"

bundle: validate-full
	@echo "==> Creating bundle archive..."
	@mkdir -p ../bundles
	tar -czf ../bundles/$(BUNDLE_ID).tar.gz \
		--exclude='.git' \
		--exclude='*.pyc' \
		--exclude='__pycache__' \
		.
	@echo "Bundle created: ../bundles/$(BUNDLE_ID).tar.gz"
	@sha256sum ../bundles/$(BUNDLE_ID).tar.gz | tee ../bundles/$(BUNDLE_ID).sha256

clean:
	@echo "==> Cleaning generated files..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@rm -f ../bundles/$(BUNDLE_ID).tar.gz
	@rm -f ../bundles/$(BUNDLE_ID).sha256
	@echo "Clean complete."

.DEFAULT_GOAL := help
