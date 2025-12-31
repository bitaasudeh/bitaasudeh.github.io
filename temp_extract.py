import sys
try:
    import PyPDF2
    with open('CV_Bita (3).pdf', 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
        with open('cv_extracted.txt', 'w', encoding='utf-8') as out:
            out.write(text)
        print('SUCCESS')
except Exception as e:
    print(f'ERROR: {e}')
