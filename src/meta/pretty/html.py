from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from xml.etree.ElementTree import SubElement


class HTMLProcessor(Treeprocessor):
    def setup(self):
        newroot = self.root.makeelement("div", {})
        self.html = SubElement(newroot, "html")
        self.head = SubElement(self.html, "head")
        self.head.text = "\n"
        self.body = SubElement(self.html, "body")
        self.root.tag = "main"
        self.root.tail = ""
        self.body.append(self.root)
        return newroot

    def get_title(self):
        h1 = self.root.find("h1")
        if h1 is not None:
            return h1.text

    @staticmethod
    def format_title(title):
        return title

    def make_header(self):
        header = self.newroot.makeelement("header", {})
        self.body.insert(0, header)
        SubElement(header, "a", href="index.html").text = "index"

    def meta(self, elm, **kwargs):
        link = SubElement(self.head, elm)
        link.attrib.update(kwargs)
        link.tail = "\n"

    def run(self, root):
        self.root = root
        self.newroot = self.setup()
        self.html.attrib["lang"] = "en"
        self.meta(
            "meta",
            **{"content": "text/html;charset=UTF-8", "http-equiv": "Content-type"}
        )

        title_text = self.get_title()
        if title_text:
            title = SubElement(self.head, "title")
            title.text = self.format_title(title_text)
            title.tail = "\n"

        self.meta("link", rel="stylesheet", href="../assets/style.css")

        self.make_header()

        return self.newroot


class HTML5(Extension):
    def extendMarkdown(self, md, *_):
        md.treeprocessors.register(HTMLProcessor(md), "html5", 1)
