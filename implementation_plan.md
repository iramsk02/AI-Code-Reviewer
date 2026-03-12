# Implementation Plan: AI Security PR Reviewer

## 🎯 Project Goal
Develop an automated GitHub Action that performs an AI-powered first-pass security review on Pull Requests, identifying vulnerabilities like SQL injection, improper auth, and hardcoded secrets.

---

## 🛠️ Phases & Roadmap

### Phase 1: GitHub Action Scaffolding (Weeks 1-2)
- **Workflow Setup**: Create a `.github/workflows` template that triggers on `pull_request` events.
- **Dumping Diffs**: Implement logic to extract code diffs from the GitHub API.
- **Benchmarking**: Compare CodeRabbit and Codium patterns.

### Phase 2: Security Prompt Engineering (Weeks 3-6)
- **Vulnerability Mapping**: Research common security pitfalls in Java/Spring (Mifos Backend) and Angular (Mifos Frontend).
- **Prompt Design**: Create system prompts for "Junior Security Auditor" persona.
- **Context Management**: Strategy for passing only relevant files to the LLM to save tokens.

### Phase 3: Bot Interaction & Reporting (Weeks 7-9)
- **Comment Injection**: Automate posting review comments directly on specific lines of the PR.
- **Severity Rating**: Add "Critical/Warning/Info" labels to findings.
- **False Positive Reduction**: Implement a feedback loop to ignore irrelevant flags.

### Phase 4: Integration & Advanced Scanning (Weeks 10-12)
- **Secret Scanning**: Integrate with traditional tools (Gitleaks) + AI for contextual verification.
- **Jira sync**: Optionally flag security issues in related Jira tickets.

### Phase 5: Polish & Deployment (Weeks 13-14)
- **Performance**: Optimize the Action runtime.
- **Best Practices**: Documentation for repo maintainers on how to customize review rules.

---

## 📚 Areas for Research & Learning

### 1. GitHub Actions API
- Using `octokit` to manipulate PR comments and reviews.
- Managing GitHub Secrets for API keys.

### 2. Security Patterns
- OWASP Top 10 for Web Applications.
- Common Java/Spring Boot security misconfigurations.

### 3. LLM Reasoning
- Chain-of-Thought for vulnerability detection.
- Multi-step verification: "Does this patch actually fix the issue described?"

---

## 📝 Next Steps
- [ ] Set up a dummy repository to test PR hooks.
- [ ] Draft the first "Security Reviewer" system prompt in a playground.
- [ ] Connect the Action to a basic OpenAI/Claude API call.
