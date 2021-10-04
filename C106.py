import plotly.express as px
import csv
import numpy as np
def getDataSource(data):
    size_of_tv = []
    Average_time_spent = []
    with open(data) as csv_file:
     df = csv.DictReader(csv_file)

     for row in df:
         size_of_tv.append(float(row["Size of TV"]))
         Average_time_spent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return {"x":size_of_tv,"y":Average_time_spent}
def findCorr(dataSource):
    Corr = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between size of TV and Time spent watchign TV",Corr[0,1])

def setUp():
    data = "tv.csv"
    dataSource = getDataSource(data)
    findCorr(dataSource)
setUp()     