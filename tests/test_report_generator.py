import tempfile
import os
from pathlib import Path
import shutil
from tools.report_generator import generate_report

def test_generate_report_creates_file(tmp_path, monkeypatch):
    # Create fake workspace
    base = Path("/tmp/workflow_ws_test")
    if base.exists():
        shutil.rmtree(base)
    ws = base / "tester-0001"
    ws.mkdir(parents=True)
    # monkeypatch report module to point to test base
    monkeypatch.setenv("USER", "tester")
    # temporarily monkeypatch find_latest_workspace to use our test base
    from tools import report_generator as rg
    orig_find = rg.find_latest_workspace
    rg.find_latest_workspace = lambda base_dir="/tmp/workflow_ws": Path(ws)
    try:
        cfg = tmp_path / "cfg.yml"
        cfg.write_text("""
project_name: "T"
author: "A"
items: { a: 1 }
""")
        rp = generate_report(str(cfg))
        assert rp.exists()
        text = rp.read_text()
        assert "Project: T" in text
    finally:
        rg.find_latest_workspace = orig_find
        shutil.rmtree(base, ignore_errors=True)
