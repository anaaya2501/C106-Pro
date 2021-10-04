import plotly.express as px
import csv
import numpy as np
def getDataSource(data):
    marks_in_percentage = []
    days_present = []
    with open(data) as csv_file:
     df = csv.DictReader(csv_file)

     for row in df:
         marks_in_percentage.append(float(row["Marks In Percentage"]))
         days_present.append(float(row["Days Present"]))
    return {"x":marks_in_percentage,"y":days_present}
def findCorr(dataSource):
    Corr = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between marks and days present",Corr[0,1])

def setUp():
    data = "collegeMarks.csv"
    dataSource = getDataSource(data)
    findCorr(dataSource)
setUp()     