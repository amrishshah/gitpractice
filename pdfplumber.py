import pdfplumber
import pytesseract
import pandas as pd
import sys
import os

inputfile = sys.argv[1]
outputfile = '/home/erpnext/covenantTrackingCVS/'
#inputfile = inputfile.replace(' ','\ ')
#print(os.path.basename(inputfile))
os.system("mkdir -p "+os.path.dirname(outputfile+inputfile.replace("./","")))


#pdf = pdfplumber.open("Term Sheet 3 - STFC.pdf")
pdf = pdfplumber.open(inputfile)
countpage=len(pdf.pages)
#p0 = pdf.pages[0]
flag = False
for page1 in range(0,countpage):
    p0 = pdf.pages[page1]
    table = p0.extract_table()
    #print(table)
    if(table is not None):
        flag = True
        #with open('2_new.csv', 'a',newline='') as csvfile:
        df=pd.DataFrame(table)
        df.to_csv(outputfile+inputfile.replace("./",""),encoding='utf-8', mode='a',header=None)
#if flag == False :
#    outputfile+inputfile.replace("./","")


#im = p0.to_image()

#print(table)
