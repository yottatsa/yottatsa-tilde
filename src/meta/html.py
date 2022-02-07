from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from xml.etree.ElementTree import SubElement

class HTMLProcessor(Treeprocessor):

    def setup(self):
        newroot = self.root.makeelement('div', {})
        self.html = SubElement(newroot, 'html') 
        self.head = SubElement(self.html, 'head') 
        self.body = SubElement(self.html, 'body') 
        self.root.tag = 'main'
        self.body.append(self.root)
        return newroot

    def get_title(self):
        h1 = self.root.find('h1')
        if h1 is not None:
            return h1.text

    def format_title(self, title):
        return title

    def run(self, root):
        self.root = root
        self.newroot = self.setup()

        title_text = self.get_title()
        if title_text:
            title = SubElement(self.head, 'title')
            title.text = self.format_title(title_text)

        return self.newroot


class HTML5(Extension):
    def extendMarkdown(self, md, *_):
        md.treeprocessors.register(HTMLProcessor(md), 'html5', 999)
