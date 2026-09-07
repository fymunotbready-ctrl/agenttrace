import unittest
from agent import run_gold, QuoteAgent


class AgentTests(unittest.TestCase):
    def test_gold_ten_lights(self):
        out = run_gold()
        self.assertTrue(out["pass"])
        self.assertEqual(out["total"], 500)

    def test_trace_grows(self):
        a = QuoteAgent()
        a.add_device("fan", 60, 1)
        self.assertEqual(len(a.trace.calls), 1)


if __name__ == "__main__":
    unittest.main()
