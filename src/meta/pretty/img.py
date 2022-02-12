import os

from PIL import Image, ImageOps

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


class ImgProcessor(Treeprocessor):
    WIDTH = 640

    @staticmethod
    def get_dimensions(imagefile):
        try:
            image = Image.open(imagefile)
            w, h = image.size
        finally:
            image.close()

        ar = h / w

        if w > ImgProcessor.WIDTH:
            w = ImgProcessor.WIDTH
            h = int(w * ar)

        return w, h

    def run(self, root):
        for img in root.iter("img"):
            src = img.attrib.get("src", None)
            if not src or not os.path.exists(src):
                continue
            w, h = self.get_dimensions(src)
            img.attrib.update(
                {
                    "height": str(h),
                    "width": str(w),
                }
            )


class Img(Extension):
    def extendMarkdown(self, md, *_):
        md.treeprocessors.register(ImgProcessor(md), "img", 2)
