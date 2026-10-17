# Contributing Guidelines

Thank you for contributing to the Smart Virtual Assistant project. Please read these guidelines to ensure smooth collaboration and maintain project quality.

## Branching & Pull Requests Workflow

1. Always branch off the latest `main`:
   ```bash
   git switch main
   git pull origin main
   git switch -c <type>/<issue-number>-<short-description>
   ```
2. Keep branches small and focused on a single issue.
3. Open a Pull Request referencing the issue (e.g., `Closes #17`).
4. Ensure all CI checks and tests pass before requesting review.

---

## Secrets and Sensitive Data Policy

To protect project security and adhere to our Definition of Done (DoD):

### 1. Never Commit Secrets or Personal Data
- Never commit API keys, personal access tokens, passwords, database credentials, private URLs, or personally identifiable information (PII).
- Never hard-code credentials into source code, documentation, or commit messages.

### 2. Managing Environment Variables
- Local environment variables should be stored in a `.env` file at the root of the repository.
- A template file [`.env.example`](.env.example) is provided in the repository with non-sensitive placeholder values.
- To set up your local environment:
  ```bash
  cp .env.example .env
  ```
- Fill in your actual local configuration in `.env`.

### 3. Gitignore Enforcement
- `.env` and `.env.*` files are explicitly listed in [`.gitignore`](.gitignore) and must never be force-added (`git add -f`).
- Only `.env.example` is tracked in version control.

### 4. Incident Response: Accidental Secret Leak
If a secret or credential is inadvertently committed or pushed:
1. **Revoke immediately**: Treat the credential as compromised and invalidate/revoke it at the service provider immediately.
2. **Notify the team**: Alert the QA & Security Lead and Tech Lead.
3. **Purge git history**: Do not just remove the file in a new commit. The secret must be expunged from git history using `git-filter-repo` or repository history rewriting tools.
