#!/usr/bin/env bash
# Simple static server for prototype
DIR="$(dirname "$0")/ui"
cd "$DIR" || exit 1
python3 -m http.server 8000

# Open http://localhost:8000 in your browser to view the prototype
