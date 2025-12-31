# Try to extract PDF text using available methods

$pdfPath = "CV_Bita (3).pdf"
$outputPath = "cv_extracted.txt"

# Method 1: Try using ExtractPDFData module
try {
    if (-not (Get-Module -ListAvailable -Name ExtractPDFData)) {
        Write-Host "Installing ExtractPDFData module..."
        Install-Module -Name ExtractPDFData -Scope CurrentUser -Force -ErrorAction SilentlyContinue
    }
    
    if (Get-Module -ListAvailable -Name ExtractPDFData) {
        Import-Module ExtractPDFData -ErrorAction SilentlyContinue
        Export-PDFDataTextWithLayout -Path $pdfPath -OutputPath $outputPath -ErrorAction SilentlyContinue
        if (Test-Path $outputPath) {
            Write-Host "Successfully extracted PDF text using ExtractPDFData"
            Get-Content $outputPath
            exit 0
        }
    }
} catch {
    Write-Host "ExtractPDFData method failed: $_"
}

# Method 2: Try Python with PyPDF2
$pythonPath = "C:\Users\Bita Asudeh\AppData\Local\Microsoft\WindowsApps\python.exe"
if (Test-Path $pythonPath) {
    $script = @"
import sys
try:
    import PyPDF2
    with open('$pdfPath', 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
        with open('$outputPath', 'w', encoding='utf-8') as out:
            out.write(text)
        print('SUCCESS')
except Exception as e:
    print(f'ERROR: {e}')
"@
    $script | Out-File -FilePath "temp_extract.py" -Encoding utf8
    $result = & $pythonPath "temp_extract.py" 2>&1
    if ($result -match "SUCCESS" -and (Test-Path $outputPath)) {
        Write-Host "Successfully extracted using Python"
        Get-Content $outputPath
        Remove-Item "temp_extract.py" -ErrorAction SilentlyContinue
        exit 0
    }
}

Write-Host "Could not extract PDF text automatically. Please provide the CV content manually."





