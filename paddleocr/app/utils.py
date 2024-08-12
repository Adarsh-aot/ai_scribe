# app/utils.py
import fitz  # PyMuPDF
from PIL import Image

def pdf_to_images(pdf_file):
    pdf_document = fitz.open(stream=pdf_file, filetype="pdf")
    images = []
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)
    return images