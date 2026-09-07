import unittest
from src.agent import run_gold, QuoteAgent, run_tasks


class AgentTests(unittest.TestCase):
    def test_gold_ten_lights(self):
        out = run_gold()
        self.assertTrue(out["pass"])
        self.assertEqual(out["total"], 500)

    def test_trace_grows(self):
        a = QuoteAgent()
        a.add_device("fan", 60, 1)
        self.assertEqual(len(a.trace.calls), 1)

    def test_tasks_pass_rate(self):
        out = run_tasks()
        self.assertEqual(out["passed"], out["total"])
        self.assertEqual(out["rate"], 1.0)


if __name__ == "__main__":
    unittest.main()
