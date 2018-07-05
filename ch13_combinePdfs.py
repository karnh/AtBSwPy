#! python3
# combinePdf.py - Combines all PDFs in current working directory into a single
# PDF

import PyPDF2, os

# Get all files in current directory
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all files 
for filename in pdfFiles:
    pdfFileReader = PyPDF2.PdfFileReader(open(filename, 'rb'))

    # loop thorugh all pages (except first) and add them
    for pageNum in range(1, pdfFileReader.numPages):
        pdfWriter.addPage(pdfFileReader.getPage(pageNum))


# Save pdf to a file
pdfOutput = open('allMinutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()