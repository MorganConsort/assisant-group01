# AI Service — Interface Specification

> **Status:** Design only — no LLM call is implemented yet.

This document defines the public interface for the future AI service module
(`src/assistant/ai_service.py`). The module will handle questions that the
rule-based responder in [`rules.py`](../src/assistant/rules.py) cannot answer
(see [`ai-or-not.md`](ai-or-not.md) for the classification).

---

## How it fits into the existing flow

```
User question
     │
     ▼
rules.reply()
     │
     ├── match found ──► return rule-based answer
     │
     └── no match ──► ai_service.ask() ──► return AI answer or fallback
```

When `rules.reply()` would currently return *"I don't know that yet …"*, the
system will instead call `ai_service.ask()`.

---

## Function signature

```python
def ask(
    question: str,
    *,
    context: list[str] | None = None,
    timeout: float = 10.0,
) -> AiResponse:
    """Send a question to the LLM and return a structured response."""
    ...
```

---

## Inputs

| Parameter  | Type                    | Required | Description |
|------------|-------------------------|----------|-------------|
| `question` | `str`                   | Yes      | The user's question, already stripped of leading/trailing whitespace. Must be non-empty. |
| `context`  | `list[str] \| None`     | No       | Optional list of retrieved text chunks that give the LLM relevant background (e.g. CSV rows, doc snippets). Defaults to `None` (no extra context). |
| `timeout`  | `float`                 | No       | Maximum seconds to wait for the LLM response. Defaults to `10.0`. |

---

## Output

`ask()` returns an `AiResponse` dataclass:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class AiResponse:
    """Structured response from the AI service."""

    answer: str          # The generated answer text (always non-empty).
    sources: list[str]   # List of source references used (may be empty).
    is_fallback: bool    # True if the answer came from the fallback path
                         # instead of the LLM.
```

### Field details

| Field         | Type         | Description |
|---------------|--------------|-------------|
| `answer`      | `str`        | Human-readable answer to the question. Never empty. |
| `sources`     | `list[str]`  | Zero or more identifiers for data that informed the answer (e.g. `"offices.csv"`, a URL). Empty when no sources apply. |
| `is_fallback` | `bool`       | `True` when the LLM was unavailable or errored and the fallback message was returned instead. |

---

## Errors

The function **does not raise exceptions** to the caller under normal
circumstances. Errors are handled internally and result in a fallback response.

| Error condition | Internal handling | What the caller sees |
|-----------------|-------------------|----------------------|
| Empty or whitespace-only `question` | `ValueError` raised immediately | Caller must validate input before calling `ask()`. |
| LLM API key missing or invalid | Caught internally; logged as warning | `AiResponse` with `is_fallback=True` |
| LLM request times out (`timeout` exceeded) | Caught internally; logged as warning | `AiResponse` with `is_fallback=True` |
| LLM returns an empty or malformed response | Caught internally; logged as warning | `AiResponse` with `is_fallback=True` |
| Network / HTTP error | Caught internally; logged as warning | `AiResponse` with `is_fallback=True` |

---

## Fallback behaviour

When the LLM is unavailable or any runtime error occurs, `ask()` returns:

```python
AiResponse(
    answer="I'm not able to answer that right now. "
           "Try asking about a campus office instead.",
    sources=[],
    is_fallback=True,
)
```

This ensures the assistant **never crashes** and always gives the user a
helpful reply, even without a working LLM connection.

---

## Example usage (future)

```python
from assistant.ai_service import ask

response = ask(
    "Why is quicksort faster than bubble sort in practice?",
    context=["Algorithms textbook, Chapter 7"],
)

print(response.answer)
# → "Quicksort has O(n log n) average-case complexity and good
#    cache locality, whereas bubble sort is O(n²) …"

print(response.sources)
# → ["Algorithms textbook, Chapter 7"]

print(response.is_fallback)
# → False
```

---

## Configuration (planned)

| Environment variable      | Purpose                              | Default        |
|---------------------------|--------------------------------------|----------------|
| `ASSISTANT_LLM_API_KEY`   | API key for the LLM provider         | *(none — required when AI is enabled)* |
| `ASSISTANT_LLM_MODEL`     | Model identifier (e.g. `gpt-4o-mini`)| `gpt-4o-mini`  |
| `ASSISTANT_LLM_TIMEOUT`   | Default timeout in seconds           | `10`           |

Keys must **never** be committed to the repository. Use a `.env` file (already
listed in `.gitignore`) or system environment variables.
