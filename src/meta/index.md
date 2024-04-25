# `meta/`

`meta/` is a highly-opinionated [collection of tools][meta_src] to build those notes.
Previous iteration, [`render.py`][render_py], was designed as a monolitic Python program, which made it non-reusable. The goal of `meta/` to give exmaples of how to apply Unix ideas of text-processing and single-purposeness to support purpose-built, lightweight, semantic website.
It uses:

* GNU Make for automation;
* Git for versioning;
* [Python-Markdown] for DOM generation;
* [ElementTree] for mangling with DOM tree.

In this iteration:

* dynamic pages generation is triggered from Makefiles, allowing separation of code;
* writing is less cluttered, as the sources are stores separatelu from the website like in [Oscean];
* metadata is inferred from both Git and markdown files, rather then filesystem attributes.

## Todo

* print out unresolved links
* add history and meta for pages
* add footer
* build [`gmi`][gemini] out of Markdown
