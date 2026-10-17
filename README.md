# Study Assistant — starter

A starter repository for the CSC10014 Smart Virtual Assistant project (Group 04). It is a small command-line assistant that answers study-related questions, such as where the library is and when it is open.

## Prerequisites

- Python 3.10 or newer (check with `python --version`)
- Git (check with `git --version`)

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/MorganConsort/lab01-group04.git
cd lab01-group04
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate it** (the prompt should then start with `(.venv)`)

| OS / Shell            | Command                          |
| --------------------- | -------------------------------- |
| macOS / Linux         | `source .venv/bin/activate`      |
| Windows (PowerShell)  | `.venv\Scripts\Activate.ps1`     |
| Windows (cmd)         | `.venv\Scripts\activate.bat`     |

**4. Install dependencies**

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

## Run

```bash
python -m assistant "where is the library?"
```

Expected output:

```
Library: room B.201, open Mon-Sat: 07:00-20:00
```

Use the `help` command to see what the assistant can do:

```bash
python -m assistant "help"
```

Expected output:

```
I can tell you where an office is and when it opens. Try 'Where is the Training Office?'
```

## Test

```bash
pytest -q
```

Expected result:

```
4 passed
```

## Project structure

```
lab01-group04/
├── data/             # Data files the assistant answers from
├── docs/             # Project documentation and reports
├── scripts/          # Helper scripts
├── src/              # Source code (the `assistant` package)
├── tests/            # Automated tests, run with pytest
├── ui/               # User interface code
├── .gitignore        # Files Git should ignore (e.g. .venv)
├── pyproject.toml    # Package configuration (used by `pip install -e .`)
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Troubleshooting

- **`No module named assistant`**: you skipped `pip install -e .`, or the virtual environment is not active. Activate `.venv` and run `pip install -e .` again.
- **PowerShell blocks `Activate.ps1`**: run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then activate again.
- **`pytest: command not found`**: the virtual environment is not active, or `pytest` is missing from `requirements.txt`. Activate `.venv` and run `pip install pytest`.
- **`python` not found on macOS/Linux**: use `python3` in place of `python` for the commands above.
