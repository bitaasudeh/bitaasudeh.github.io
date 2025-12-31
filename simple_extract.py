#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

pdf_path = "CV_Bita (3).pdf"
output_path = "cv_text.txt"

# Try PyPDF2 first
try:
    import PyPDF2
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Extracted with PyPDF2")
    print(text[:1000])
    sys.exit(0)
except ImportError:
    pass
except Exception as e:
    print(f"PyPDF2 error: {e}")

# Try pypdf
try:
    import pypdf
    with open(pdf_path, 'rb') as f:
        reader = pypdf.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Extracted with pypdf")
    print(text[:1000])
    sys.exit(0)
except ImportError:
    pass
except Exception as e:
    print(f"pypdf error: {e}")

# Try pdfplumber
try:
    import pdfplumber
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Extracted with pdfplumber")
    print(text[:1000])
    sys.exit(0)
except ImportError:
    pass
except Exception as e:
    print(f"pdfplumber error: {e}")

print("ERROR: No PDF library available")





