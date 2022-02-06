ALL = $(shell find -name '*.md' ! -name 'meta_*' | sed 's,\.md$$,.html,')
LINKS = meta/meta_links.md
CONFIG = meta/config.yaml

all: $(ALL)

clean:
	rm -f $(ALL)

%.html:	%.md $(LINKS) $(CONFIG) Makefile
	cat $< $(LINKS) |\
	       PYTHONPATH=`pwd`	markdown_py -c $(CONFIG) -x meta.html:HTML5 -o html -f $@

.PHONY: all clean
