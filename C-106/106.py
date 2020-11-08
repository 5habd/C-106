import csv
import numpy as np 
def getdatasource(data_path):
    sizeoftv=[]
    averagetimespend=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sizeoftv.append(float(row["size of tv"]))
            averagetimespend.append(float(row[" average time spent watching tv"]))
    return{"x": sizeoftv,"y":averagetimespend}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between size of tv and averge time sepnt watching tv: ",correlation[0,1])
def setup():
    data_path="./data2.csv"
    datasource=getdatasource(data_path)
    findcorrelation(datasource)
setup()