import csv
from pprint import pprint
import pdfplumber


def writeCSV(name, mode, rowdata):
    with open(name, mode, newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(rowdata)

with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            file = 'C:\\Users\\harsh\\Downloads\\gem\\GeM-Bidding-' + row[8] + '.pdf'
            # print(file) #this is the file name
            print(file)
            pdf = pdfplumber.open(file)
            page = pdf.pages[0]
            tables = page.extract_tables()
            maintable = tables[1]
            data = []
            mode = maintable[1][2]
            size1 = maintable[2][2]
            size2 = maintable[2][3]
            core1 = maintable[3][2]
            core2 = maintable[3][3]
            data.append(mode)
            data.append(size1)
            data.append(size2)
            data.append(core1)
            data.append(core2)
            print(data)
            writeCSV('out.csv', 'a', data)
            data.clear()

        except IndexError:
            print("_____ERROR______")
            writeCSV('out.csv','a',"")