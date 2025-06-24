# PDF Invoice Renamer – Python Script

This script automatically renames PDF invoice files in the current folder using the invoice number found in the first page.

### How it works:
- Scans all `.pdf` files in the current folder
- Reads the first page of each file using PyPDF2
- Looks for patterns like `Invoice #12345`
- Renames the file to `invoice_12345.pdf`

### Example:
Before:
- `doc1.pdf`
- `invoice_mar.pdf`

After running:
- `invoice_12345.pdf`
- `invoice_54321.pdf`

### Requirements:
- Python 3.7+
- `pip install pypdf2`

### Run it:
```bash
python invoice_renamer.py
