"""
Rename every PDF in the current folder using the invoice number
extracted from the first page (pattern: 'Invoice #12345').
"""
import re, os
from pathlib import Path
from PyPDF2 import PdfReader     # pip install pypdf2

PATTERN = re.compile(r"Invoice\s*#\s*([A-Za-z0-9\-]+)", re.I)

def rename_invoice(pdf_path: Path):
    text = (PdfReader(pdf_path).pages[0].extract_text() or "")
    match = PATTERN.search(text)
    if match:
        new_name = f"invoice_{match.group(1)}.pdf"
        pdf_path.rename(pdf_path.with_name(new_name))
        print(f"{pdf_path.name} → {new_name}")
    else:
        print(f"No invoice # found in {pdf_path.name}")

if __name__ == "__main__":
    for pdf in Path(".").glob("*.pdf"):
        rename_invoice(pdf)
