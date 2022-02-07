UPDATES = ../site/updates.html
ALL = $(shell find -name '*.md' ! -name 'meta_*' | sed 's,^\./,../site/,; s,\.md$$,.html,') $(UPDATES)
LINKS = $(shell find -name 'meta_links.md')
CONFIG = meta/config.yaml
MARKDOWN_PY = PYTHONPATH=`pwd` markdown_py -c $(CONFIG) -x meta.html:HTML5 -o html

all: $(ALL)

clean:
	rm -f $(ALL)

../site/%.html:	%.md $(LINKS) $(CONFIG)
	mkdir -p $(shell dirname $@)
	cat $< $(LINKS) | $(MARKDOWN_PY) -f $@

../site/updates.html: 
	(meta/updates.sh; cat $(LINKS)) | $(MARKDOWN_PY) -f $@

.PHONY: all clean ../site/updates.html
