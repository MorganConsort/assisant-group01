"""A tiny rule-based responder. No AI yet — that comes in Week 4."""
from __future__ import annotations

import csv
import re
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

GREETINGS = {"hi", "hello", "hey", "xin chao", "chao", "good morning", "chao buoi sang"}

HELP_COMMANDS = {"help", "cuu voi", "giup toi", "giup"}

# These words describe an organization rather than identify a particular office.
GENERIC_OFFICE_WORDS = {"faculty", "office"}


def load_offices(path: Path = DATA_DIR / "offices.csv") -> dict[str, dict[str, str]]:
    """Return {office_name_lower: row} from the offices CSV."""
    with path.open(encoding="utf-8", newline="") as f:
        return {row["name"].lower(): row for row in csv.DictReader(f)}


def _words(text: str) -> set[str]:
    """Return lowercase alphanumeric words from text."""
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def _find_office(
    text: str, offices: dict[str, dict[str, str]]
) -> dict[str, str] | None:
    """Find an office by its full name or a unique, meaningful name word."""
    for name, row in offices.items():
        if name.lower() in text:
            return row

    message_words = _words(text)
    matches = []
    for name, row in offices.items():
        name_words = {
            word
            for word in _words(name)
            if len(word) > 3 and word not in GENERIC_OFFICE_WORDS
        }
        if message_words & name_words:
            matches.append(row)

    return matches[0] if len(matches) == 1 else None


def reply(message: str, offices: dict[str, dict[str, str]] | None = None) -> str:
    """Answer a message with simple rules."""
    text = message.strip().lower().rstrip("?!.")
    if not text:
        return "Please type a question."
    if text in GREETINGS:
        return "Hello!!! Ask me where an office is, or when it opens."
    if text in HELP_COMMANDS:
        return (
            "I can tell you where an office is and when it opens. "
            "Try 'Where is the Training Office?'"
        )
    offices = offices if offices is not None else load_offices()
    office = _find_office(text, offices)
    if office is not None:
        return f"{office['name']}: room {office['room']}, open {office['hours']}."
    return "I don't know that yet. Try asking about an office, e.g. 'training office'."
