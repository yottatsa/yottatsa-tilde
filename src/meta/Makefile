UPDATES = ../site/index.html
ALL = $(shell find -name '*.md' ! -name 'meta_*' | sed 's,^\./,../site/,; s,\.md$$,.html,') $(UPDATES)
LINKS = $(shell find -name 'meta_links.md')
CONFIG = meta/config.yaml
MARKDOWN_PY = PYTHONPATH=`pwd` markdown_py -c $(CONFIG) --noisy -x meta.pretty:HTML5 -x meta.pretty:Img -x meta.yafg:YafgExtension -o html

all: $(ALL)

clean:
	rm -f $(ALL)

../site/%.html:	%.md $(LINKS) $(CONFIG) meta/yafg/yafg.py
	mkdir -p $(shell dirname $@)
	cat $< $(LINKS) | $(MARKDOWN_PY) -f $@

../site/index.html: meta_index.md
	(cat meta_index.md; meta/updates.sh; cat $(LINKS)) | $(MARKDOWN_PY) -f $@

meta/yafg/yafg.py:
	git submodule update --init -- ../extensions/yafg


.PHONY: all clean ../site/index.html
