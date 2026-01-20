#!/bin/bash
set -euo pipefail

# Only run in remote/cloud environment
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Install Python dependencies for neuro-plans build pipeline
pip install mkdocs-material pyyaml

echo "Session start hook completed - dependencies installed"
