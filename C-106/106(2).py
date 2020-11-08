import csv
import numpy as np 
def getdatasource(data_path):
    sizeoftv=[]
    averagetimespend=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sizeoftv.append(float(row["temprature"]))
            averagetimespend.append(float(row["sales in ice cream"]))
    return{"x": sizeoftv,"y":averagetimespend}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("relation between slaes of ice cream and increase in temprature: ",correlation[0,1])
def setup():
    data_path="./data.csv"
    datasource=getdatasource(data_path)
    findcorrelation(datasource)
setup()