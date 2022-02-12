#!/bin/sh

find ../src -name '*.md' ! -name 'meta_*' ! -name 'tmp_*' | sed 's,\.\./,,; /src\/.*meta_/d; s,src/\(.*\).md,[\1]: \1.html,;'

