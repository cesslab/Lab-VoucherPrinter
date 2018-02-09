import os
import sys
import webbrowser
import numpy as np

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def gen_pdf():
    pdf_name = os.path.join("docs", "hello.pdf")
    c = canvas.Canvas(pdf_name, pagesize=letter)
    c.setLineWidth(0.5)
    c.setFont("Helvetica", 6)
    for x in np.arange(0.5, 8.5, 0.5):
        for y in np.arange(0.5, 11.0, 0.5):
            c.circle(x*inch, y*inch, 1, stroke=1, fill=1)

    c.setFont("Helvetica-Bold", 10)
    for x in np.arange(0.5, 8.5, 0.5):
        c.drawCentredString(x*inch, 10.7*inch, "{}".format(x))
    for y in np.arange(0.5, 11.0, 0.5):
        c.drawCentredString(0.2*inch, y*inch - 0.03*inch, "{}".format(y))


    c.showPage()
    c.save()
    base = os.path.dirname(os.path.realpath(__file__))
    if sys.platform.startswith("win32"):
        os.startfile(os.path.join(base, pdf_name))
    else:
        webbrowser.open_new("file:" + os.path.join(base, pdf_name))


if __name__ == "__main__":
    gen_pdf()
