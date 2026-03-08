# Mifos AI PR Reviewer (GitHub Action)

This is an AI-driven security and code quality reviewer designed specifically for the Mifos ecosystem. It automatically analyzes Pull Requests and flags security vulnerabilities, performance issues, and bugs using the Groq (Llama 3.3) LLM.

## 🚀 Features
- **Security First**: Performs an automated first-pass security review (OWASP Top 10 focus).
- **GitHub Native**: Runs entirely within GitHub Actions—no hosting required.
- **Fast Feedback**: Provides actionable comments directly on the PR in seconds.

## 🛠️ Setup

### 1. Store your AI Reviewer on GitHub
Push this folder to a new public repository (e.g., `your-username/my-ai-code-reviewer`).

### 2. Configure the Target Repository
In the repository you want to review:
1. Go to **Settings > Secrets and variables > Actions**.
2. Add a new Secret: `GROQ_API_KEY` (Your Groq API key).

### 3. Add the Workflow
Create `.github/workflows/ai-review.yml` in your target repository:

```yaml
name: AI PR Reviewer
on:
  pull_request:
    types: [opened, reopened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: your-username/my-ai-code-reviewer@main
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GROQ_API_KEY: ${{ secrets.GROQ_API_KEY }}
```
