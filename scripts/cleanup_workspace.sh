#!/usr/bin/env bash
# Safe cleanup: remove workspaces older than X days (default 1 day), or clean all with --all

set -euo pipefail

DAYS="${1:-1}"
WS_DIR="/tmp/workflow_ws"

if [[ "${1:-}" == "--all" ]]; then
  echo "Removing all workspaces under $WS_DIR"
  rm -rf "$WS_DIR"
  exit 0
fi

echo "Removing workspaces older than $DAYS day(s) under $WS_DIR"
find "$WS_DIR" -maxdepth 1 -type d -mtime +"$DAYS" -exec rm -rf {} +
echo "Cleanup complete"
