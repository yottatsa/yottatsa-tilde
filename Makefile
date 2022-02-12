src:
	make -C src/meta/pretty
	make -C src

publish: .git src
	git archive --format=tar HEAD | tar x -C ~/public_html

.PHONY: src publish
