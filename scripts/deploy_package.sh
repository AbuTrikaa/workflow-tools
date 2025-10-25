#!/usr/bin/env bash
# Safe packaging: create a tarball of the supplied workspace (default: latest workspace)
# This is local-only and writes under /tmp

set -euo pipefail

WORKSPACES_DIR="/tmp/workflow_ws"
LATEST_WS=$(ls -dt "$WORKSPACES_DIR"/* 2>/dev/null | head -n1 || true)

if [[ -z "$LATEST_WS" ]]; then
  echo "No workspace found in $WORKSPACES_DIR. Run setup_workspace.sh first."
  exit 1
fi

OUT_DIR="/tmp/workflow_packages"
mkdir -p "$OUT_DIR"
OUT_FILE="$OUT_DIR/$(basename "$LATEST_WS").tar.gz"

tar -czf "$OUT_FILE" -C "$WORKSPACES_DIR" "$(basename "$LATEST_WS")"
echo "Packaged $LATEST_WS -> $OUT_FILE"