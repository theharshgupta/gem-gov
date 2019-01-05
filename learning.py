import pdfplumber
import csv

if 'j' in 'i j i':
    print("YAS")
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
            for i in range(len(tables)):
                for j in range(len(tables[i])):
                    for k in range(len(tables[i][j])):
                        if 'Number of cores' in str(tables[i][j][k]):
                            print(i)
                            print(j)
                            print(k)
                            print(tables[i][j][k+1])