from reportlab.pdfgen import canvas
import webbrowser
import os
import sys


def gen_pdf():
    pdf_name = os.path.join("docs", "hello.pdf")
    c = canvas.Canvas(pdf_name)
    c.drawString(100, 100, "Hello World")
    c.showPage()
    c.save()
    base = os.path.dirname(os.path.realpath(__file__))
    if sys.platform.startswith("win32"):
        os.startfile(os.path.join(base, pdf_name))
    else:
        webbrowser.open_new(os.path.join(base, pdf_name))


if __name__ == "__main__":
    gen_pdf()
