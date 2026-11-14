#!/bin/sh
# The tests gate: the whole suite, with the standard library's unittest.
set -eu
cd "$(dirname "$0")/../.."
exec python3 -m unittest discover -v -p 'test_*.py'
