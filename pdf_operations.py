from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from io import BytesIO

def create_blank_page():
    """Creates a single blank PDF page in memory."""
    packet = BytesIO()
    can = canvas.Canvas(packet)
    can.showPage()
    can.save()
    packet.seek(0)
    return PdfReader(packet).pages[0]

def add_blank_pages(writer, num_pages):
    """Adds the specified number of blank pages."""
    for _ in range(num_pages):
        writer.add_page(create_blank_page())

def merge_pdfs(readers, num_blank_pages=0):
    """Merge PDFs with optional blank pages between files."""
    writer = PdfWriter()
    for i, reader in enumerate(readers):
        for page in reader.pages:
            writer.add_page(page)
        if num_blank_pages > 0 and i < len(readers) - 1:
            add_blank_pages(writer, num_blank_pages)
    return writer
