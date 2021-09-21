from pathlib import Path
from pylatex import Document, Figure

class ExportPdf:
    def __init__(self):
        images = list(map(lambda x: str(x), Path("Output").rglob("*.png")))
        doc = Document('Output')

        for image in images:
            with doc.create(Figure(position='h')) as card_image:
                card_image.add_image(image, width='120px')

        doc.generate_pdf(clean_tex=True)