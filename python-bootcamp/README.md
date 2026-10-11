# Python Bootcamp

This directory contains the three-week Python bootcamp for the CSC10014 team project. Each member completes the individual exercises in their own folder and submits the work through an issue, branch, pull request, and teammate review.

The purpose of this structure is to make every member's progress, testing, review activity, and contribution visible on GitHub.

## Team members

Replace the placeholders below with the team's GitHub usernames and agreed Python-safe folder names.

| Member | GitHub username | Folder name | Rotation reviewer |
|---|---|---|---|
| 1 | `<member_1_github_username>` | `<member_1_folder>` | `<reviewer_username>` |
| 2 | `<member_2_github_username>` | `<member_2_folder>` | `<reviewer_username>` |
| 3 | `<member_3_github_username>` | `<member_3_folder>` | `<reviewer_username>` |
| 4 | `<member_4_github_username>` | `<member_4_folder>` | `<reviewer_username>` |

Folder names must be valid Python identifiers. Replace hyphens in GitHub usernames with underscores.

Examples:

```text
minh-nv   -> minh_nv
hdang-207 -> hdang_207
```

Each member must write individual homework only inside their own folder.

## Directory structure

```text
python-bootcamp/
|-- README.md
|-- PROGRESS.md
|
|-- members/
|   |-- <member_1_folder>/
|   |   |-- w1/
|   |   |-- w2/
|   |   `-- w3/
|   |-- <member_2_folder>/
|   |   |-- w1/
|   |   |-- w2/
|   |   `-- w3/
|   |-- <member_3_folder>/
|   |   |-- w1/
|   |   |-- w2/
|   |   `-- w3/
|   `-- <member_4_folder>/
|       |-- w1/
|       |-- w2/
|       `-- w3/
|
|-- shared/
|   |-- contract.py
|   `-- study_planner/
|
`-- tests/
    |-- conftest.py
    |-- test_w1.py
    |-- test_w2.py
    `-- test_w3.py
```

The `shared/` directory is reserved for the team exercises in Weeks 2 and 3. The `tests/` directory contains instructor-provided tests and supporting fixtures.

## Prerequisites

- Python 3.10 or newer
- Git 2.30 or newer
- Access to the team GitHub repository
- A local Python virtual environment

Check the installed tools:

```powershell
python --version
git --version
```

On Windows, `py --version` may be used if `python` is not available.

## Local setup

Run these commands from the repository root.

### 1. Clone the repository

```powershell
git clone git@github.com:MorganConsort/assisant-group01.git
cd assisant-group01
```

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

### 3. Activate the environment

PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Git Bash:

```bash
source .venv/Scripts/activate
```

macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install the required tools

If the root project dependencies have not been installed:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

Install the bootcamp testing and linting tools if they are not already listed in `requirements.txt`:

```powershell
python -m pip install pytest ruff
```

## Week 1 exercises

Every member creates the following files inside:

```text
python-bootcamp/members/<member_folder>/w1/
```

### W1-1: Grade summary

File: `grades.py`

Implement:

```python
def summary(scores: list[float]) -> dict:
    ...
```

The returned dictionary must contain `min`, `max`, `mean`, and `median`. Round the mean and median to two decimal places. An empty list must raise `ValueError`.

### W1-2: Word counter

File: `text_tools.py`

Implement:

```python
def word_count(text: str) -> dict[str, int]:
    ...


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    ...
```

Convert words to lowercase and ignore the punctuation characters `. , ! ? ; :`. Sort `top_k` results by descending count and then alphabetically.

### W1-3: Thesis eligibility

File: `rules.py`

Implement:

```python
def can_register_thesis(credits: int, gpa: float) -> bool:
    ...


def missing(credits: int, gpa: float) -> list[str]:
    ...
```

A student can register when they have at least 120 credits and a GPA of at least 2.0. `missing` returns clear human-readable reasons when a requirement is not met.

### W1-4: Translate C++ to Python

File: `translate.py`

Each member implements a different variant:

| Member | Required translation |
|---|---|
| 1 | Binary search on a sorted list; return the index or `-1` |
| 2 | In-place insertion sort; return the sorted list |
| 3 | Transpose a matrix represented as a list of lists |
| 4 | Sieve of Eratosthenes; return primes up to `n` |

Keep the behavior of the supplied C++ function, write idiomatic Python, and include a docstring explaining at least one difference from the C++ implementation.

### W1-5: Group the timetable

File: `timetable.py`

Implement:

```python
def by_day(items: list[tuple[str, str]]) -> dict[str, list[str]]:
    ...
```

Return a dictionary mapping each day to an alphabetically sorted list of course codes. Use a comprehension or `dict.setdefault` as requested by the exercise.

## Running the Week 1 tests

Run the tests from the repository root:

```powershell
pytest -q python-bootcamp/tests/test_w1.py `
  --member <member_folder> `
  --variant <member_number>
```

Example only:

```powershell
pytest -q python-bootcamp/tests/test_w1.py `
  --member minh_nv `
  --variant 1
```

The `--member` value must exactly match the folder name under `members/`. The `--variant` value is the member number from 1 to 4.

Run Ruff against the bootcamp:

```powershell
ruff check python-bootcamp
```

Do not modify, remove, skip, or weaken instructor tests simply to make an incorrect implementation pass.

## GitHub workflow for each member

### 1. Create the weekly issue

Create one issue for W1 and:

- Assign it to yourself.
- Add labels `python-hw` and `w1`.
- Add milestone `PY-W1`.
- Identify your rotation reviewer.
- Add checkboxes for W1-1 through W1-5.
- Record estimated and actual hours.

### 2. Create your branch

```powershell
git switch main
git pull
git switch -c py/w1-<github-username>
```

### 3. Commit one exercise at a time

Make at least five meaningful commits during Week 1.

Examples:

```text
feat(py-w1): W1-1 grade summary
feat(py-w1): W1-2 word counter
feat(py-w1): W1-3 thesis eligibility
feat(py-w1): W1-4 translate member variant
feat(py-w1): W1-5 group timetable by day
```

### 4. Push the branch

```powershell
git push -u origin py/w1-<github-username>
```

Push regularly instead of waiting until all exercises are finished.

### 5. Open the pull request

Use the title:

```text
py-w1: <github-username>
```

The PR description must:

- Explain what was completed.
- Link the W1 issue with `Closes #<issue-number>`.
- Include the local pytest and Ruff results.
- Request the assigned rotation reviewer.

Do not merge until CI is green and the reviewer has approved the PR.

### 6. Review a teammate's work

Every member must review their assigned teammate's PR. A reviewer should confirm that:

- The code is in the correct member folder.
- All five exercises are present.
- The implementation is understandable and follows the specifications.
- Edge cases are handled.
- Instructor tests and CI pass.
- The author did not modify another member's folder or weaken the tests.

Request changes when necessary. Approve only after understanding the submitted code.

### 7. Update progress

Update the member's row in `PROGRESS.md` with the issue number, PR number, reviewer, test result, and actual hours. This may be included in the homework PR or submitted in a small follow-up PR.

## Contribution rules

1. Work only in your assigned member folder for individual exercises.
2. Do not commit directly to `main`.
3. Do not rewrite another member's individual solution.
4. Do not commit `.venv/`, caches, secrets, or generated files.
5. Make small commits with meaningful messages.
6. Push regularly so progress is visible.
7. Use pull requests and teammate reviews for all homework submissions.
8. Do not merge a failing PR.
9. Record honest work hours in `PROGRESS.md`.
10. Disclose AI assistance according to the course policy and verify all generated code yourself.

## Week 1 completion criteria

Week 1 is complete when:

- [ ] Every member has a W1 issue.
- [ ] Every member has completed W1-1 through W1-5 in their own folder.
- [ ] Every member has made at least five meaningful commits.
- [ ] Four individual PRs titled `py-w1: <github-username>` have been merged.
- [ ] Every individual PR received approval from the assigned rotation reviewer.
- [ ] Ruff and pytest pass in CI.
- [ ] `PROGRESS.md` contains one complete W1 row for each member.
- [ ] Member 1 has created and pushed the `py-w1-done` tag.

## Troubleshooting

### `pytest` is not recognized

Activate `.venv` and install the dependencies:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install pytest
```

### `ModuleNotFoundError` for a member folder

Confirm that:

- The folder name passed to `--member` exactly matches the directory name.
- Hyphens were replaced with underscores.
- The command is being run from the repository root.
- The instructor-provided `conftest.py` is present.

### PowerShell blocks `Activate.ps1`

Run this once for the current Windows user:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate the virtual environment again.

### CI passes the root tests but not the bootcamp tests

Confirm that `.github/workflows/ci.yml` includes commands equivalent to:

```bash
ruff check python-bootcamp
pytest -q python-bootcamp
```

## Future weeks

Week 2 work goes into each member's `w2/` folder. Week 3 work goes into `w3/`. Team integration code belongs in `shared/`, following the instructions for T-W2 and T-W3.
