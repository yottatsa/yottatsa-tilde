# meta

Collection of [tools to build those notes][meta_src], notably

* GNU Make
* [Python-Markdown][markdown_py]
* git

The previous iteration, [`render.py`][render_py], which I used to publish "long-reads" from Markdown, is of them are based on mangling with DOM tree rather than templating as is. 
In this iteration 

* writing is less cluttered, as I use flat directory src/dist model as [Oscean];
* metadata inferred from both Git and markdown files, rather then filesystem attributes;
* ...

## todo

* print out unresolved links
