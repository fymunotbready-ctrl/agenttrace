"""AgentTrace v0 — scripted tools, logged calls."""

import json
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Trace:
    calls: list = field(default_factory=list)

    def log(self, tool: str, args: dict, result):
        self.calls.append({"tool": tool, "args": args, "result": result})


class QuoteAgent:
    def __init__(self):
        self.devices = []
        self.trace = Trace()

    def add_device(self, name: str, watts: float, hours: float):
        row = {"name": name, "watts": watts, "hours": hours, "wh": watts * hours}
        self.devices.append(row)
        self.trace.log("add_device", row, "ok")
        return row

    def site_wh(self):
        total = sum(d["wh"] for d in self.devices)
        self.trace.log("site_wh", {}, total)
        return total

    def draft_email(self, who: str):
        total = self.site_wh()
        text = f"Hello {who}, estimated daily use is {total:.0f} Wh."
        self.trace.log("draft_email", {"who": who}, text)
        return text


def run_gold() -> dict:
    a = QuoteAgent()
    for _ in range(10):
        a.add_device("light", 10, 5)
    total = a.site_wh()
    mail = a.draft_email("Asha")
    passed = total == 500 and "500" in mail
    return {"pass": passed, "total": total, "calls": len(a.trace.calls), "email": mail}




def run_tasks(tasks_path: str = "tasks.json") -> dict:
    """Run tasks from JSON and return pass rate."""
    tasks = json.loads(Path(__file__).with_name(tasks_path).read_text())
    agent = QuoteAgent()
    passed = 0
    results = []
    for task in tasks:
        ok = False
        if task["action"] == "add_device":
            result = agent.add_device(**task["args"])
            ok = result["wh"] == task["expected_wh"]
        elif task["action"] == "site_wh":
            result = agent.site_wh()
            ok = result == task["expected_total"]
        elif task["action"] == "draft_email":
            result = agent.draft_email(**task["args"])
            ok = task["expected_in_email"] in result
        elif task["action"] == "trace_count":
            result = len(agent.trace.calls)
            ok = result == task["expected_count"]

        passed += int(ok)
        results.append({"id": task["id"], "action": task["action"], "pass": ok, "result": result})

    rate = passed / len(tasks) if tasks else 0
    return {"passed": passed, "total": len(tasks), "rate": rate, "results": results}


if __name__ == "__main__":
    print("Gold run:", run_gold())
    print()
    out = run_tasks()
    print(f"Tasks: {out['passed']}/{out['total']} passed ({out['rate']:.0%})")
