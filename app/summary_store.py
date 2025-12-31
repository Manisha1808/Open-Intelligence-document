import json
from pathlib import Path

SUMMARY_PATH = Path("data/summaries.json")

def load_summaries():
    if SUMMARY_PATH.exists():
        return json.loads(SUMMARY_PATH.read_text())
    return {}

def save_summaries(summaries):
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summaries, indent=2))
