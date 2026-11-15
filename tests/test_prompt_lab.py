import unittest
from prompt_lab import Case, evaluate, render, score

class PromptLabTests(unittest.TestCase):
    def test_render_and_score(self):
        rows = evaluate("Hello {name}", [Case("greet", {"name":"Ada"}, ("Hello Ada",))])
        self.assertTrue(rows[0]["passed"])
        self.assertEqual(score(rows), 100.0)
    def test_forbidden_text_fails(self):
        row = evaluate("safe output", [Case("policy", {}, (), ("safe",))])[0]
        self.assertFalse(row["passed"])
    def test_missing_variable_is_reported(self):
        self.assertIn("error", evaluate("{missing}", [Case("broken", {})])[0])

if __name__ == "__main__": unittest.main()
