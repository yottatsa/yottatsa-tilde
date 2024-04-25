#!/bin/sh

git log --no-relative --name-status --abbrev-commit --date=short --format="format:## %as %s%n%b" -- '**.md' | sed '/^D\s*src/ d; /src\/.*meta_/ d; s,^.\s*src/\(.*\).md,* [\1],; s,/index\],],; /index/ d'
