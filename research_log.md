# Research Log: AI Security PR Reviewer

## 📅 2026-03-09: GitHub Actions & Security APIs
*   **API Exploration:** Octokit is the standard for GitHub API interactions.
*   **Diff Parsing:** GitHub provides unified diffs. LLMs perform better when given the *file context* around the diff, not just the +/- lines.
*   **Competitor Analysis:** CodeRabbit uses a sophisticated state machine for "conversational" reviews; start with a simpler "Checklist" approach for the POC.

## 🗺️ Learning Resources & Links
1.  **CodeRabbit Docs:** [docs.coderabbit.ai](https://docs.coderabbit.ai/)
2.  **OWASP Top 10:** [owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)
3.  **GitHub Action Metadata:** [action.yml syntax](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions)

## 🛠️ Key Questions to Answer
- How to prevent the bot from commenting on every PR (noise management)?
- Which model is more cost-effective for large diffs (GPT-4o-mini vs Claude 3 Haiku)?
