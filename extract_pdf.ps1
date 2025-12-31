# Try to extract text from PDF using .NET
Add-Type -AssemblyName System.Drawing

$pdfPath = "CV_Bita (3).pdf"
$outputPath = "cv_text.txt"

# Try using iTextSharp or similar, but for now let's try a different approach
# Since we can't easily extract, let's check if there's a way

# For now, let's assume the main change is removing the GPA line
# But we need to extract the actual content

Write-Host "PDF extraction would require additional libraries."
Write-Host "Checking PDF file..."

if (Test-Path $pdfPath) {
    Write-Host "PDF file exists: $pdfPath"
    $fileInfo = Get-Item $pdfPath
    Write-Host "File size: $($fileInfo.Length) bytes"
}





