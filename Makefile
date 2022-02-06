.PHONY: publish

publish: all .git
	git archive --format=tar HEAD | tar x -C ../public_html

include meta/Makefile
