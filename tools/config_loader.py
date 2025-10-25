"""
Simple config loader for YAML files.
"""

import yaml
from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class Config:
    project_name: str
    author: str
    items: Dict[str, Any]

def load_config(path: str) -> Config:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return Config(
        project_name=data.get("project_name", "workflow-project"),
        author=data.get("author", "unknown"),
        items=data.get("items", {}),
    )
