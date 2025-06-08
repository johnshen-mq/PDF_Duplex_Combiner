import os
import sys
from unittest import mock
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import main


def create_dummy_pdf(path, numbers):
    c = canvas.Canvas(str(path))
    for num in numbers:
        c.setFont("Helvetica", 72)
        width, height = c._pagesize
        c.drawCentredString(width / 2, height / 2, str(num))
        c.showPage()
    c.save()


def test_duplex_merge(tmp_path):
    odd_pdf = tmp_path / "odd.pdf"
    even_pdf = tmp_path / "even.pdf"
    output_pdf = tmp_path / "merged.pdf"

    create_dummy_pdf(odd_pdf, [1, 3, 5])
    create_dummy_pdf(even_pdf, [6, 4, 2])

    inputs = [str(odd_pdf), str(even_pdf), str(output_pdf)]
    with mock.patch("builtins.input", side_effect=inputs):
        main.main()

    reader = PdfReader(str(output_pdf))
    extracted = [page.extract_text().strip() for page in reader.pages]
    assert extracted == ["1", "2", "3", "4", "5", "6"]
