#!/bin/sh

echo '# updates'
git log --no-relative --name-only --abbrev-commit --date=short --format="format:## %as %s%n%b" -- '**.md' | sed '/src\/.*meta_/d; s,src/\(.*\).md,* [\1](\1.html),; s,/index\],],;'
