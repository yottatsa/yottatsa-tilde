from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from xml.etree.ElementTree import SubElement


class HTMLProcessor(Treeprocessor):
    def setup(self):
        newroot = self.root.makeelement("div", {})
        self.html = SubElement(newroot, "html")
        self.html.text = "\n"
        self.head = SubElement(self.html, "head")
        self.head.tail = "\n"
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

    def make_link(self, **kwargs):
        link = SubElement(self.head, "link")
        link.attrib.update(kwargs)

    def run(self, root):
        self.root = root
        self.newroot = self.setup()

        title_text = self.get_title()
        if title_text:
            title = SubElement(self.head, "title")
            title.text = self.format_title(title_text)

        self.make_header()
        self.make_link(rel="stylesheet", href="../assets/style.css")

        return self.newroot


class HTML5(Extension):
    def extendMarkdown(self, md, *_):
        md.treeprocessors.register(HTMLProcessor(md), "html5", 1)
