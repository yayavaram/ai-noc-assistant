# AI NOC Assistant

An AI assistant for NOC operations: alert triage, runbook search, and guided remediation with human approval.
Built as the capstone project for Module 1 (Applied AI Engineering).

## Setup
1. Install Python 3.12 and uv
2. Copy `.env.example` to `.env` and add your API keys
3. Run `uv sync` to install dependencies
4. Run `uv run python src/noc_assistant/check_env.py` to verify setup