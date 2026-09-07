

![Tests](https://github.com/fymunotbready-ctrl/agenttrace/actions/workflows/test.yml/badge.svg)




![Python](https://img.shields.io/badge/python-3.10%2B-blue)




![License](https://img.shields.io/badge/license-MIT-green)



# AgentTrace

A tiny agent with tools. Every run leaves a trace you can score.

**Internship signal:** tool use + recovery + pass rate, not a chat screenshot.
**Business link:** this is how CloseLoop stays honest when you add "send email."

## v1
Tools: `add_device`, `site_wh`, `draft_email`
15 tasks in `tasks.json` (start with 6).
Print pass rate.

## Not v1
Autonomous company-running agent.

## Project Structure

.
├── src/            # source code
├── tests/          # unit tests
├── .github/workflows/test.yml   # CI: runs tests on every push
├── LICENSE
└── README.md

## Running

python3 -m unittest discover -s tests -t .
