from pathlib import Path
from pylatex import Document, Figure
from pylatex.figure import SubFigure

class ExportPdf:
    def __init__(self):
        images = self.separate_by_image(list(map(lambda x: str(x), Path("Output").rglob("*.png"))))
        doc = Document('Output')

        for group in images:
            with doc.create(Figure(position='h')) as image_grouper:
                for image in group:
                    with image_grouper.create(SubFigure()) as card_image:
                        card_image.add_image(image, width='120px')

        doc.generate_pdf(clean_tex=True)

    def separate_by_image(self, images):
        ans = []
        tmp = []

        for image in images:
            if(len(tmp) == 3):
                ans.append(tmp)
                tmp = []
            tmp.append(image)

        if(len(tmp) != 0):
            ans.append(tmp)

        return ans