#!/bin/sh

git log --no-relative --name-only --abbrev-commit --date=short --format="format:## %as %s%n%b" -- '**.md' | sed '/src\/.*meta_/d; s,src/\(.*\).md,* [\1],; s,/index\],],; /index/ d'
