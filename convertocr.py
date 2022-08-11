#find . -name '*.pdf' -print0  | xargs -0 -n1 -P9 python3 convertocr.py
import sys
import os

inputfile = sys.argv[1]
outputfile = '/home/erpnext/covenantTrackingOcr/'
#inputfile = inputfile.replace(' ','\ ')
#print(os.path.basename(inputfile))
os.system("mkdir -p '"+os.path.dirname(outputfile+inputfile.replace("./",""))+"'")
try:
    os.system("ocrmypdf --skip-text '"+inputfile+"' '"+outputfile+inputfile.replace("./","")+"'")
except:
    with open('/home/erpnext/covenantTrackingOcr/resultocrfailed.csv', 'a',newline='') as csvfile:
        fieldnames = ['filesList']
        writer = csv.DictWriter(csvfile,fieldnames)
        value['filesList'] = inputfile
        writer.writerow(value)
        csvfile.close()
    copyfile(inputfile,outputfile+inputfile.replace("./",""))
