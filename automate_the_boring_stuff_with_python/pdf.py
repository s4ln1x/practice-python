#!/usr/bin/env python3

import PyPDF2

# Read all the text from a PDF file
intel_one_pdf = open('1_INTEL.pdf', 'rb')
reader_one = PyPDF2.PdfFileReader(intel_one_pdf)

# Read the number of pages
print(f'number of pages of 1_INTEL.pdf file = {reader_one.numPages}')

# Create log with the extracted text
for page in range(reader_one.numPages):
    with open('intel_stuff.log', 'w') as fn_intel:
        fn_intel.write(reader_one.getPage(page).extractText())

# Mix two pdfs
intel_two_pdf = open('2_INTEL.pdf', 'rb')
reader_two = PyPDF2.PdfFileReader(intel_two_pdf)
writer = PyPDF2.PdfFileWriter()

# Add pages from file one
for page_num in range(reader_one.numPages):
    writer.addPage(reader_one.getPage(page_num))

# Add pages from file two
for page_num in range(reader_two.numPages):
    writer.addPage(reader_two.getPage(page_num))

# Write final file
mixed_file = open('3_INTEL.pdf', 'wb')
writer.write(mixed_file)

# Close files
mixed_file.close()
intel_two_pdf.close()
intel_one_pdf.close()
