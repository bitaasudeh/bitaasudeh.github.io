import sys
import os

try:
    import PyPDF2
except ImportError:
    print("Installing PyPDF2...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2", "-q"])
    import PyPDF2

pdf_path = "CV_Bita (3).pdf"

try:
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        # Write to a text file for easier reading
        with open("cv_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        
        print("PDF text extracted successfully to cv_text.txt")
        print("\n--- Extracted Text ---")
        print(text[:2000])  # Print first 2000 chars
        
except Exception as e:
    print(f"Error: {e}")
    # Try alternative method
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text() + "\n"
        doc.close()
        
        with open("cv_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        
        print("PDF text extracted successfully using PyMuPDF")
        print("\n--- Extracted Text ---")
        print(text[:2000])
    except Exception as e2:
        print(f"Alternative method also failed: {e2}")





