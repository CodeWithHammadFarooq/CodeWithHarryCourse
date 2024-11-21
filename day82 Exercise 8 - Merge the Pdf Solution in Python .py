# Exercise 8 - Merge the Pdf Solution in Python

from PyPDF2 import PdfWriter
import os

merge = PdfWriter()
files = [file for file in os.listdir() if files.endswith(".pdf")]

for pdf in files:
    merge.append(pdf)

merge.write("merged-pdf.pdf")
merge.close()