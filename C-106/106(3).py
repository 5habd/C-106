import csv
import numpy as np 
def getdatasource(data_path):
    sizeoftv=[]
    averagetimespend=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sizeoftv.append(float(row["no. of days school attended"]))
            averagetimespend.append(float(row[" marks in percentage"]))
    return{"x": sizeoftv,"y":averagetimespend}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation no. of days school attended and marks in percentage: ",correlation[0,1])
def setup():
    data_path="./data3.csv"
    datasource=getdatasource(data_path)
    findcorrelation(datasource)
setup()