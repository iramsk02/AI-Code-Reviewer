# AI Security PR Reviewer

## 📋 About the Project
An automated **GitHub Action** that acts as a first-pass security auditor for Mifos repositories. It identifies potential vulnerabilities in Pull Requests before they are reviewed by core maintainers.

Part of the **AI for Developer Productivity** GSoC 2026 track.

---

## 📂 Project Navigation
- **[Implementation Plan](implementation_plan.md):** 14-week roadmap for developing the reviewer.
- **[Research Log](research_log.md):** Security patterns and GitHub API documentation.

---

## 🚀 Key Features
1.  **Diff Analysis**: Scans incoming code changes for security flaws.
2.  **Smarter Comments**: Injects actionable advice directly into the PR's line-by-line view.
3.  **Severity Tagging**: Flags critical issues (e.g., SQLi) differently from style warnings.

---

## 🛠️ Installation
1.  Add `.github/workflows/ai-security-reviewer.yml` to your repo.
2.  Set `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` in GitHub Secrets.
3.  Customize rules in the `reviewer_config.json`.
