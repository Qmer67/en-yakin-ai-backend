import json
from datetime import datetime

LOG_FILE = "click_logs.jsonl"

def log_click(features, selected: bool):
    record = {
        "features": features,
        "selected": int(selected),
        "timestamp": datetime.utcnow().isoformat()
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")
