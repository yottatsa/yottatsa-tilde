UPDATES = ../site/index.html
ALL = $(shell find -name '*.md' ! -name 'meta_*' ! -name 'tmp_*' | sed 's,^\./,../site/,; s,\.md$$,.html,') $(UPDATES)
LINKS = $(shell find -name 'meta_links.md')
CONFIG = meta/config.yaml
MARKDOWN_PY = PYTHONPATH=`pwd` markdown_py -c $(CONFIG) -x meta.pretty:HTML5 -x meta.pretty:Img -x meta.yafg:YafgExtension -x md_in_html -o html

all: $(ALL)

clean:
	rm -f $(ALL)
	rm -f $(shell ls tmp_*.md)

tmp_links.md: $(LINKS)
	(cat $(LINKS); meta/links.sh) > $@

tmp_index.md:
	meta/updates.sh > $@

../site/%.html:	%.md tmp_links.md
	cat $^ | $(MARKDOWN_PY) -f $@

../site/index.html: meta_index.md tmp_index.md tmp_links.md
	cat $^ | $(MARKDOWN_PY) -f $@

.PHONY: all clean 
