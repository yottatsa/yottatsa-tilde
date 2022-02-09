src:
	make -C src

publish: .git
	git archive --format=tar HEAD | tar x -C ~/public_html

.PHONY: src publish
