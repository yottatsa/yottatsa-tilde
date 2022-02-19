import os
import re
import requests
import logging

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.postprocessors import Postprocessor


logger = logging.getLogger(__name__)


def invalid_link(href):
    if "://" in href:
        return
        logger.warning("Checking %s online", href)
        x = requests.head(href, allow_redirects=True)
        return not x.ok

    if href.endswith("html"):
        doc = href.replace(".html", ".md")
        if os.path.exists(doc):
            return

    if os.path.exists(os.path.join("..", "site", href)):
        return

    abspath = os.path.join("/var/www/html", href.lstrip("/"))
    if os.path.exists(abspath):
        return

    return True


class RedLinksProcessor(Treeprocessor):
    def run(self, root):
        links = {
            elm.attrib.get("href") for elm in root.iter("a") if "href" in elm.attrib
        }
        invalid_links = list(filter(invalid_link, links))
        for link in invalid_links:
            print(link)
        if invalid_links:
            raise RuntimeError


class MissingLinksPostprocessor(Postprocessor):
    RE_MD_LINKS = re.compile(r"\[[^\]]+\]")

    def run(self, text):
        linkblocks = set(MissingLinksPostprocessor.RE_MD_LINKS.findall(text))
        for linkblock in linkblocks:
            print(linkblock)
        # if linkblocks:
        #    raise RuntimeError
        return text


class Links(Extension):
    def extendMarkdown(self, md, *_):
        md.treeprocessors.register(RedLinksProcessor(md), "redlinks", 10)
        md.postprocessors.register(MissingLinksPostprocessor(md), "missinglinks", 1)
