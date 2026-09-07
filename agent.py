"""AgentTrace v0 — scripted tools, logged calls."""

from dataclasses import dataclass, field


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
    a.add_device("light", 10, 5)
    a.add_device("light", 10, 5)
    a.add_device("light", 10, 5)
    a.add_device("light", 10, 5)
    a.add_device("light", 10, 5)
    a.add_device("light", 10, 5)
    a.add_device("light", 10, 5)
    a.add_device("light", 10, 5)
    a.add_device("light", 10, 5)
    a.add_device("light", 10, 5)
    total = a.site_wh()
    mail = a.draft_email("Asha")
    passed = total == 500 and "500" in mail
    return {"pass": passed, "total": total, "calls": len(a.trace.calls), "email": mail}


if __name__ == "__main__":
    print(run_gold())
