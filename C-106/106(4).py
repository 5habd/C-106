import csv
import numpy as np 
def getdatasource(data_path):
    sizeoftv=[]
    averagetimespend=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sizeoftv.append(float(row["coffee in ml"]))
            averagetimespend.append(float(row["no. of sleep hours"]))
    return{"x": sizeoftv,"y":averagetimespend}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between coffee in ml and no. of sleep hours: ",correlation[0,1])
def setup():
    data_path="./data4.csv"
    datasource=getdatasource(data_path)
    findcorrelation(datasource)
setup()