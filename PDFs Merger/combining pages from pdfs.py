#Combining all pdfs in a folder excluding front page for others except first pdf
import PyPDF2, os

#Store all pdf filenames in pdfFiles
pdfFiles = []
for filename in os.listdir("."):
    if filename.endswith(".pdf"):
        pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

# Loop for all pdfs to be added
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader  = PyPDF2.PdfFileReader(pdfFileObj)

    #Append all pages from 1 to it's length in a loop
    for pagenum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pagenum)
        pdfWriter.addPage(pageObj)

pdfOutput = open("allminutes.pdf", 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

