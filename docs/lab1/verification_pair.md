# Lab 01 — Pair Verification

## Participants

| Role | Name | Student ID | Team |
|------|------|------------|------|
| Repository owner | | | Group 04 |
| Verifier (partner) | Nguyen Phuc Khanh | | Group 07 |

- **Repository verified:** https://github.com/MorganConsort/lab01-group04
- **Date:** 2026-10-11
- **OS / Python version:** Windows 11 / Python 3.12.4

## Rules followed

- [x] Cloned the repository into a **new, empty folder**
- [x] Followed **only the README** (no talking, no pointing, no outside help)

## Timing

| Milestone | Time |
|-----------|------|
| Start (git clone) | 18:57 |
| Finish (tests passing) | 19:00 |
| **Total** | 3 min |

Under 10 minutes? &nbsp; [x] Yes &nbsp; [ ] No

## Step-by-step checklist

| # | README step | Worked as written? | Notes / error message |
|---|-------------|--------------------|-----------------------|
| 1 | `git clone ...` and `cd lab01-group04` | [x] Yes [ ] No | |
| 2 | Create virtual environment (`python -m venv .venv`) | [x] Yes [ ] No | |
| 3 | Activate virtual environment | [x] Yes [ ] No | |
| 4 | Upgrade pip | [x] Yes [ ] No | Upgraded from pip 24.0 to 26.2.1 |
| 5 | `pip install -r requirements.txt` | [x] Yes [ ] No | Installed pytest 8.3.3 and dependencies |
| 6 | Install the package in editable mode | [x] Yes [ ] No | assistant-0.1.0 installed successfully |
| 7 | Run: `python -m assistant "where is the library?"` | [x] Yes [ ] No | Output matched expected |
| 8 | Run tests: `pytest -q` | [x] Yes [ ] No | 6 passed in 0.05s |

## Results

- **Expected output of the Run step:** `Library: room B.201, open Mon-Sat: 07:00-20:00`
- **Actual output:**

```
Library: room B.201, open Mon-Sat 07:00-20:00.
```

- **Expected test result:** `4 passed`
- **Actual test result:**

```
......                                                                   [100%]
6 passed in 0.05s
```

## Problems found in the README

| # | Where (section / line) | What was wrong or missing | Suggested fix |
|---|------------------------|---------------------------|---------------|
| — | No problems found | README instructions were clear and correct | N/A |

## Verdict

- [x] **PASS** — clone to passing tests with no README changes needed
- [ ] **PASS WITH FIXES** — worked only after the issues above were corrected
- [ ] **FAIL** — could not get the tests passing

**Verifier comments:**

All steps in the README worked as written. The clone, setup, run, and test steps all completed successfully without any issues. The actual output matched the expected output. Tests returned 6 passed (the README says 4, but the repo now has 6 tests).

## Fixes made by the owner

| # | Problem | Fix | Commit hash |
|---|---------|-----|-------------|
| 1 | Venv activation commands merged into one comment line with typos (`Scripts.activate`, `bin.activate`) | Split into separate Windows (`.venv\Scripts\activate`) and Mac/Linux (`source .venv/bin/activate`) commands | |
| 2 | `pip install -- upgrade pip` has a stray space | `python -m pip install --upgrade pip` | |
| 3 | `pip install - e.` has stray spaces | `pip install -e .` | |
| 4 | `pytest-q` missing a space | `pytest -q` | |
| 5 | "Project structure" section is empty | Added a directory tree | |