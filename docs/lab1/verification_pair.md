# Lab 01 — Pair Verification

## Participants

| Role | Name | Student ID | Team |
|------|------|------------|------|
| Repository owner | | | Group 04 |
| Verifier (partner) | | | |

- **Repository verified:** https://github.com/MorganConsort/lab01-group04
- **Date:** YYYY-MM-DD
- **OS / Python version:** e.g. Windows 11 / Python 3.12

## Rules followed

- [ ] Cloned the repository into a **new, empty folder**
- [ ] Followed **only the README** (no talking, no pointing, no outside help)

## Timing

| Milestone | Time |
|-----------|------|
| Start (git clone) | |
| Finish (tests passing) | |
| **Total** | ___ min |

Under 10 minutes? &nbsp; [ ] Yes &nbsp; [ ] No

## Step-by-step checklist

| # | README step | Worked as written? | Notes / error message |
|---|-------------|--------------------|-----------------------|
| 1 | `git clone ...` and `cd lab01-group04` | [ ] Yes [ ] No | |
| 2 | Create virtual environment (`python -m venv .venv`) | [ ] Yes [ ] No | |
| 3 | Activate virtual environment | [ ] Yes [ ] No | |
| 4 | Upgrade pip | [ ] Yes [ ] No | |
| 5 | `pip install -r requirements.txt` | [ ] Yes [ ] No | |
| 6 | Install the package in editable mode | [ ] Yes [ ] No | |
| 7 | Run: `python -m assistant "where is the library?"` | [ ] Yes [ ] No | |
| 8 | Run tests: `pytest -q` | [ ] Yes [ ] No | |

## Results

- **Expected output of the Run step:** `Library: room B.201, open Mon-Sat: 07:00-20:00`
- **Actual output:**

```
(paste here)
```

- **Expected test result:** `4 passed`
- **Actual test result:**

```
(paste here)
```

## Problems found in the README

| # | Where (section / line) | What was wrong or missing | Suggested fix |
|---|------------------------|---------------------------|---------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Verdict

- [ ] **PASS** — clone to passing tests with no README changes needed
- [ ] **PASS WITH FIXES** — worked only after the issues above were corrected
- [ ] **FAIL** — could not get the tests passing

**Verifier comments:**

&nbsp;

## Fixes made by the owner

| # | Problem | Fix | Commit hash |
|---|---------|-----|-------------|
| 1 | Venv activation commands merged into one comment line with typos (`Scripts.activate`, `bin.activate`) | Split into separate Windows (`.venv\Scripts\activate`) and Mac/Linux (`source .venv/bin/activate`) commands | |
| 2 | `pip install -- upgrade pip` has a stray space | `python -m pip install --upgrade pip` | |
| 3 | `pip install - e.` has stray spaces | `pip install -e .` | |
| 4 | `pytest-q` missing a space | `pytest -q` | |
| 5 | "Project structure" section is empty | Added a directory tree | |