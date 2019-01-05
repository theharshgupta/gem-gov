import pdfplumber
import csv

with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # In my Data.csv, the 7th column is the file name so that is why
        number = row[8]
        if number != '':
            file = 'C:\\Users\\harsh\\Downloads\\gem\\GeM-Bidding-' + number + '.pdf'
            # print(file) #this is the file name
            print(file)
            data = []
            # normal opening the PDF
            pdf = pdfplumber.open(file)
            # Setting the page number to '0'
            page = pdf.pages[0]
            # Extracting all the tables on the page selected (i.e 0)
            tables = page.extract_tables()
            # checking if the extra table exists or not on the first Page
            if len(tables) > 2:
                tmain = tables[2]
            else:
                tmain = tables[1]
            # Doing this so that the PDFs that are not correctly formatted are excluded from the iteration
            if tmain[1][1]=='Mode of Buying':
                mode = tmain[1][2]
                size1 = tmain[2][2]
                size2 = tmain[2][3]
                core1 = tmain[3][2]
                core2 = tmain[3][3]
                # Appending directly to the row that I read from the main CSV
                row.append(size1)
                row.append(size2)
                row.append(core1)
                row.append(core2)
                # Appending that row to a new output CSV file
                with open('gemDataFile.csv', 'a', newline='') as f:
                    # Initialising the CSV writer
                    writer = csv.writer(f)
                    # writing a single row (in form of Python list)
                    writer.writerow(row)




