.PHONY: publish

publish: src .git
	make -C src
	git archive --format=tar HEAD | tar x -C ~/public_html
