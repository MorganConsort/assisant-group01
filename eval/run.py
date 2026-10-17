"""Run benchmark evaluation against assistant rules."""
from __future__ import annotations

import csv
import sys
from pathlib import Path

# Add project root / src to sys.path so assistant can be imported
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from assistant.rules import reply


def run_benchmark(cases_file: Path | None = None) -> float:
    """Run benchmark evaluation and print accuracy report."""
    if cases_file is None:
        cases_file = ROOT_DIR / "eval" / "cases.csv"

    if not cases_file.exists():
        print(f"Error: test cases file not found at {cases_file}")
        sys.exit(1)

    with cases_file.open(encoding="utf-8", newline="") as f:
        cases = list(csv.DictReader(f))

    total = len(cases)
    passed = 0
    category_stats: dict[str, dict[str, int]] = {}

    print(f"Running benchmark on {total} test cases from {cases_file.name}...\n")
    print(f"{'#':<4} | {'Status':<6} | {'Category':<12} | {'Question'}")
    print("-" * 70)

    for idx, row in enumerate(cases, start=1):
        question = row["question"]
        expected = row["expected"].strip()
        category = row.get("category", "general")

        if category not in category_stats:
            category_stats[category] = {"total": 0, "passed": 0}
        category_stats[category]["total"] += 1

        actual = reply(question).strip()
        is_pass = actual == expected

        if is_pass:
            passed += 1
            category_stats[category]["passed"] += 1
            status = "PASS"
        else:
            status = "FAIL"

        # Truncate question for display if too long
        display_q = (question[:35] + "...") if len(question) > 38 else question
        print(f"{idx:<4} | {status:<6} | {category:<12} | {display_q}")

        if not is_pass:
            print(f"     Expected: {expected}")
            print(f"     Actual:   {actual}")

    accuracy = (passed / total) * 100 if total > 0 else 0.0

    print("-" * 70)
    print("\nCategory breakdown:")
    for cat, stats in category_stats.items():
        cat_pct = (stats["passed"] / stats["total"]) * 100 if stats["total"] > 0 else 0.0
        print(f" - {cat:<12}: {stats['passed']}/{stats['total']} ({cat_pct:.1f}%)")

    print(f"\nOverall accuracy: {passed}/{total} ({accuracy:.2f}%)")
    return accuracy


if __name__ == "__main__":
    accuracy = run_benchmark()
    sys.exit(0 if accuracy == 100.0 else 1)
