#!/bin/sh
# The lint gate: every Python file compiles, and the last commit adds no whitespace errors.
set -eu
cd "$(dirname "$0")/../.."
python3 -m compileall -q -x '(^|/)\.' .
if git rev-parse --verify -q HEAD~1 >/dev/null; then
    git diff --check HEAD~1 HEAD
else
    git diff --check "$(git hash-object -t tree /dev/null)" HEAD
fi
