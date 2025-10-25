#!/usr/bin/env python3
"""
Generate a simple text report in the latest workspace.
This is intentionally benign: it reads sample config and writes a short summary.
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from tools.config_loader import load_config

def find_latest_workspace(base="/tmp/workflow_ws"):
    if not os.path.isdir(base):
        raise FileNotFoundError(f"{base} does not exist. Run scripts/setup_workspace.sh first.")
    entries = sorted(Path(base).iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
    if not entries:
        raise FileNotFoundError("No workspace directories found.")
    return entries[0]

def generate_report(config_path: str):
    config = load_config(config_path)
    ws = find_latest_workspace()
    report_path = ws / "report.txt"
    content = [
        f"Project: {config.project_name}",
        f"Author: {config.author}",
        f"Generated: {datetime.utcnow().isoformat()}Z",
        "",
        "Items summary:",
    ]
    for k, v in config.items.items():
        content.append(f"- {k}: {v}")
    report_text = "\n".join(content)
    report_path.write_text(report_text, encoding="utf-8")
    print(f"Wrote report to {report_path}")
    return report_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/report_generator.py <config.yml>")
        sys.exit(2)
    generate_report(sys.argv[1])
