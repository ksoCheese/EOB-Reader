import PyPDF2
import re
import openpyxl

# create function to accept file path as argument and return data
#pdf_path = '/Users/kso/downloads/HusainEOB.pdf'
def extract_data_from_pdf(pdf_path):
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
            contains = ['overpayment', 'recovery', 'future', 'forwarding', 'balance', 'identifier', 'adjustment']
            if any([x in text.lower() for x in contains]):

            # Split the text into lines
                lines = text.split('\n')

            # Get the insurance name
                insurance = lines[0].strip()

            # Loop through each line to find the keywords
                for line_num in range(len(lines)):
                    line = lines[line_num]#.lower()

                    matches = ["overpayment", "recovery", "future", "forwarding", "balance", "identifier", "adjustment"]
                    # WORK ON THIS CODE BELOW, NOT ABLE TO SEPARATE PHRASE FROM AMOUNT INTO PROPER COLUMNS
                    if line.startswith("PROV ADJ CODE"):
                        # Get the phrase containing the keyword and the amount
                        phrase = line

                        # Search for the decimal amount at the end of the line
                        amount_pattern = r"AMT:\s*(-?[\d,]+\.\d{2})"
                        amount_match = re.search(amount_pattern, phrase)

                        if amount_match:
                            amount = amount_match.group(1)
                        else:
                            amount = "Not found"

                        # Add the result to the list
                        results.append({'insurance': insurance, 'phrase': phrase, 'amount': amount})
    return results

#create function to save results to spreadsheet

def save_results(results, output_file):
    # Write the results to an excel spreadsheet
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.append(['Insurance', 'Phrase', 'Amount'])
    for result in results:
        worksheet.append([result['insurance'], result['phrase'], result['amount']])
    workbook.save(output_file)
