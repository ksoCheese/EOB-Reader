import os
import PyPDF2
import openpyxl

# Set the file path for the PDF
pdf_path = '/Users/kso/Desktop/HorizonEndoRecoup.pdf'

# Open the PDF file
with open(pdf_path, 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Get the number of pages in the PDF
    num_pages = pdf_reader.getNumPages()

    # Create a list to store the results
    results = []

    # Loop through each page in the PDF
    for page_num in range(num_pages):

        # Get the text from the page
        page = pdf_reader.getPage(page_num)
        text = page.extractText()

        # Check if the page contains the keywords
        if 'overpayment' in text.lower() or 'recovery' in text.lower() or 'future' in text.lower() or 'forwarding' in text.lower() or 'balance' in text.lower() or 'identifier' in text.lower():

            # Split the text into lines
            lines = text.split('\n')

            # Get the insurance name
            insurance = lines[0].strip()

            # Loop through each line to find the keywords
            for line_num in range(len(lines)):
                line = lines[line_num].lower()

                if 'overpayment' in line or 'recovery' in line or 'future' in line or 'forwarding' in line or 'balance' in line or 'identifier' in line:
                    # Get the phrase containing the keyword and the amount
                    phrase = lines[line_num:line_num + 2]
                    amount = phrase[-1].strip()
                    phrase = ' '.join(phrase).strip()

                    # Add the result to the list
                    results.append({'insurance': insurance, 'phrase': phrase, 'amount': amount})

# Write the results to an Excel spreadsheet
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.append(['Insurance', 'Phrase', 'Amount'])
for result in results:
    worksheet.append([result['insurance'], result['phrase'], result['amount']])
workbook.save('results.xlsx')
