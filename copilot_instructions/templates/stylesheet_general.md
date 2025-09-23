**please use these templates where necessary and appropriated**

# Basic Styleguide Rules for All GitHub Repo Publications

## 0) Scope

Applies to anything public in the repo: READMEs, docs pages, issues, PRs, release notes, wikis, blog posts, and code comments.

---

## 1) Required top-level files

* `README.md` — what/why/how, quickstart, links.
* `LICENSE` — SPDX identifier at top (e.g., `MIT`), repo root copy.
* `CODE_OF_CONDUCT.md` — contributor behavior.
* `CONTRIBUTING.md` — how to file issues/PRs, coding rules, branch model.
* `SECURITY.md` — how to report vulnerabilities.
* `CHANGELOG.md` — human-readable release history.
* `.github/ISSUE_TEMPLATE/*` and `.github/PULL_REQUEST_TEMPLATE.md`.

---

## 2) Writing style (all publications)

* **Language:** English (en-US). Be concise, action-oriented, and inclusive.
* **Headings:** `#` H1 per doc; hierarchical levels after that.
* **Acronyms:** Expand on first use (e.g., “Computer-Aided Design (CAD)”).
* **Links:** Prefer **relative** links within repo; descriptive anchor text.
* **Lists & tables:** Use for steps and comparisons; no long paragraphs.
* **Code blocks:** Fenced with language tag (` ```bash`, ` ```yaml`).
* **Images:** Optimized PNG/SVG/WebP; always include **alt text**.
* **Dates:** ISO 8601 (`YYYY-MM-DD`).
* **Numbers & units:** SI units; space between value and unit (e.g., `5 kW`).

---

## 3) File & naming conventions

* **Directories & files:** `kebab-case` (lowercase, hyphens): `user-guide/quick-start.md`.
* **Docs assets:** `docs/assets/` for images/diagrams; include source (`.drawio`, `.puml`) next to exported file.
* **Examples & samples:** `examples/<purpose>/`.
* **Configuration:** `*.yaml` preferred over `*.yml` for consistency.

---

## 4) README minimum content

1. One-sentence **purpose**.
2. **Badges:** build, coverage, license.
3. **Quickstart:** 3–7 commands max.
4. **Docs map:** link to deeper pages.
5. **Contributing** and **Security** links.
6. **License** section with SPDX tag.

---

## 5) Commits, branches, and PRs

* **Commit format (Conventional Commits):**

  * `feat: add GPU scheduler`
  * `fix(api): null pointer on retry`
  * `docs(readme): clarify quickstart`
* **Branching:** feature branches `feat/<slug>`, fixes `fix/<slug>`, docs `docs/<slug>`.
* **PRs:**

  * Title uses Conventional Commit style.
  * Description includes **what/why**, screenshots (if UI), and **test notes**.
  * Link related issues: `Closes #123`.
  * Pass all checks; 1+ reviewer approval.

---

## 6) Releases & versioning

* **SemVer**: `MAJOR.MINOR.PATCH`.
* **Tags:** `v1.4.2`.
* **Release notes** (Keep a Changelog):

  * **Added / Changed / Fixed / Security / Docs / Deprecated / Removed**
* Attach artifacts (binaries, SBOM) where applicable.

---

## 7) Documentation rules

* Organize under `docs/` with clear index (`docs/README.md`).
* Each doc starts with 3–5 line **summary**.
* Cross-link related pages; avoid duplication.
* Include **“Last updated”** line at bottom.
* Use **mermaid**/PlantUML for simple diagrams; include editable source.

---

## 8) Code, linting, and tests

* Language-specific formatters/linters (e.g., Prettier, Black, golangci-lint) enforced in CI.
* Unit tests required for new code; add coverage badge if meaningful.
* Add **examples** or **smoke tests** for docs/tutorial code.

---

## 9) Security & compliance

* Never commit **secrets**; use `.gitignore` and secret scanning.
* Security disclosures via `SECURITY.md` only.
* Third-party license notices recorded in `THIRD_PARTY_NOTICES.md` (as needed).
* Optional but recommended: **SBOM** generation (e.g., Syft) and SAST.

---

## 10) Accessibility & UX

* Alt text on images; avoid text in images where possible.
* Color-independent meaning in charts (use patterns/labels).
* Keyboard-navigable examples; caption complex media.

---

## 11) Issue triage & labels

* Use a small, consistent set: `bug`, `feature`, `docs`, `good first issue`, `help wanted`, `security`, `discussion`.
* Apply **milestones** for releases; keep backlog tidy.

---

## 12) Publication checklist (pre-merge)

* [ ] README has purpose, quickstart, links, license.
* [ ] Links resolve; images have alt text.
* [ ] Spelling/grammar pass; acronyms expanded on first use.
* [ ] Lint & tests green; coverage unchanged or higher.
* [ ] SECURITY/CONTRIBUTING referenced.
* [ ] Changelog updated (if user-visible change).
* [ ] Release notes prepared (for tags).

---

## 13) Minimal PR template (drop-in)

```markdown
### What
Short summary of the change.

### Why
Problem statement / user impact.

### How
Key implementation points, alternatives considered.

### Tests
- [ ] Unit
- [ ] Integration
- [ ] Docs build

### Screenshots / Artifacts
(if applicable)

### Checklist
- [ ] Conventional Commit title
- [ ] Changelog updated
- [ ] Security review (if needed)
- [ ] Docs updated
Closes #<issue>
```

---

## 14) Minimal release notes template

```markdown
## vX.Y.Z — YYYY-MM-DD

### Added
-

### Changed
-

### Fixed
-

### Security
-

### Docs
-
```

Use this as the baseline for **all** public repo publications; extend with project-specific rules as needed.
