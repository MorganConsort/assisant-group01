# Security & Secrets Audit Report

- **Date:** 2026-10-17
- **Auditor:** Nguyen Quoc Thinh (`thinh-nguyen-007`), QA & Security Lead
- **Target Repository:** `MorganConsort/assistant-group04`
- **Milestone:** Lab 2 — Security Audit (Issue #18)

---

## 1. Audit Scope & Objectives

The goal of this audit is to verify that no sensitive credentials, secrets, private keys, or personal identifiable information (PII) exist in the codebase or its git commit history, fulfilling the requirements for Lab 2 (Issue #18) and our Definition of Done (DoD).

The audit covered:
1. **Working Tree & Tracked Files:** All files currently tracked by Git (`git ls-files`).
2. **Git Commit History:** The complete commit log and diffs across all historical commits (`git log -p --all`).
3. **Environment & Ignore Configuration:** Verification of `.gitignore` and `.env.example`.
4. **Data Assets & Scripts:** Examination of data files (`data/offices.csv`, `eval/cases.csv`) and test fixtures.

---

## 2. Methodology & Detection Rules

### A. Automated Pattern Scan (Gitleaks Ruleset)
An automated scan script (`scripts/audit_secrets.py`) was executed against the entire git log and tracked files targeting:
- **Private Keys:** RSA, EC, DSA, OpenSSH, and PGP private keys (`-----BEGIN ... PRIVATE KEY-----`).
- **API Keys & Tokens:** Patterns matching `api_key`, `access_token`, `secret_key`, `auth_token` assignments.
- **Hard-coded Credentials:** Passwords, secret connection strings (`postgres://`, `mysql://`, `mongodb://`, `redis://`).
- **High-entropy Secrets:** Generic tokens and secret hashes.

### B. Personal Data (PII) Inspection
- Scanned commit diffs and dataset entries for personal phone numbers (e.g. `+84` / `03x/05x/07x/08x/09x` patterns).
- Verified that contact details in `data/offices.csv` contain only public university offices (e.g., Student Affairs Office, Library, Inspectorate Office).

### C. Configuration & Boundary Check
- Verified that `.env` is explicitly ignored by [.gitignore](file:///D:/00_APCS_K25/CS252/assistant-group04/.gitignore).
- Verified that only [.env.example](file:///D:/00_APCS_K25/CS252/assistant-group04/.env.example) is committed with dummy placeholders.

---

## 3. Findings & Results

| Check Item | Target | Tool / Method | Result | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Tracked Sensitive Files** | Repo tree | `git ls-files` | **PASS** | No `.env`, `.pem`, `.key`, or credentials committed |
| **API Keys & Tokens** | Git history | Regex pattern scan | **PASS** | No API keys or tokens in commit diffs |
| **Private Keys (SSH/RSA)** | Git history | Header pattern match | **PASS** | No private key blocks detected |
| **Hard-coded Passwords** | Source code | Static inspection | **PASS** | No passwords or connection strings found |
| **Personal Identifiable Info (PII)** | Data & commits | Regex phone scan | **PASS** | No personal phone numbers or private data found |
| **Gitignore Enforcement** | `.gitignore` | `git status --ignored` | **PASS** | `.env` and `.env.*` correctly ignored |
| **Environment Template** | Root | Manual check | **PASS** | `.env.example` contains only placeholder values |

---

## 4. Conclusion & Continuous Measures

- **Audit Status:** **CLEAN / PASSED** (0 security issues found).
- **Incident Response Plan:** As documented in [CONTRIBUTING.md](file:///D:/00_APCS_K25/CS252/assistant-group04/CONTRIBUTING.md), if any secret is inadvertently pushed, it must be immediately revoked at the service provider, reported to the QA & Security Lead, and purged using git history rewriting.
- **Pre-commit Recommendation:** Developers should keep `.env` excluded and verify `git diff --staged` before every commit.
