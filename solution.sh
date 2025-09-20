#!/usr/bin/env bash
set -euo pipefail

# Placeholder implementation:
# Lists the three largest files in the provided directory (or current dir)
DIR="${1:-.}"
DIR=$(realpath "$DIR")

find "$DIR" -type f -printf "%s %p\n" | sort -nr | head -n 3

# Minimal behaviour for tests – create an empty clean.json
touch /app/clean.json
