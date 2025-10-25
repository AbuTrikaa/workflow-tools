#!/usr/bin/env bash
# Safe setup: create a per-user temporary workspace under /tmp/workflow_ws/<username>-<timestamp>

set -euo pipefail

USER_NAME="${USER:-$(whoami)}"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BASE_DIR="/tmp/workflow_ws"
WORKDIR="$BASE_DIR/${USER_NAME}-${TIMESTAMP}"

mkdir -p "$WORKDIR"
echo "workspace_dir=$WORKDIR" > "$WORKDIR/.workspace_meta"
echo "Created workspace at: $WORKDIR"
