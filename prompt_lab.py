"""Deterministic prompt-template regression testing."""
from dataclasses import dataclass
from typing import Callable, Iterable
import re

@dataclass(frozen=True)
class Case:
    name: str
    variables: dict[str, str]
    required: tuple[str, ...] = ()
    forbidden: tuple[str, ...] = ()

def render(template: str, variables: dict[str, str]) -> str:
    try:
        return template.format_map(variables)
    except KeyError as exc:
        raise ValueError(f"Missing template variable: {exc.args[0]}") from exc

def evaluate(template: str, cases: Iterable[Case]) -> list[dict]:
    results = []
    for case in cases:
        try:
            output = render(template, case.variables)
            missing = [s for s in case.required if s.casefold() not in output.casefold()]
            present = [s for s in case.forbidden if s.casefold() in output.casefold()]
            results.append({"name": case.name, "passed": not missing and not present,
                            "missing": missing, "forbidden_found": present, "output": output})
        except ValueError as exc:
            results.append({"name": case.name, "passed": False, "error": str(exc)})
    return results

def score(results: list[dict]) -> float:
    return round(100 * sum(r["passed"] for r in results) / len(results), 2) if results else 0.0

if __name__ == "__main__":
    template = "You are a helpful assistant. Summarize: {text}"
    cases = [Case("basic", {"text": "A short report"}, ("Summarize",)),
             Case("empty", {"text": ""}, ("Summarize",))]
    report = evaluate(template, cases)
    print(f"Score: {score(report)}%")
    for row in report:
        print(("PASS" if row["passed"] else "FAIL"), row["name"])
