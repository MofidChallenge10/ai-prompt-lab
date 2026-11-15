# AI Prompt Lab
Deterministic regression checks for prompt templates. No model/API key is needed for the included evaluator.

## Quick start
```bash
python prompt_lab.py
python -m unittest discover -s tests -v
```

## Library
Create `Case(name, variables, required, forbidden)` fixtures, then call `evaluate(template, cases)`. Each result includes a pass flag and diagnostics; `score(results)` returns the pass percentage.

## Scope
This checks rendered prompt text and deterministic expectations. It does not claim to measure model quality; connect a model adapter and human-reviewed rubric for semantic evaluation.
