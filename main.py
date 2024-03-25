import pandas as pd
from DataSource import DataSource


excelFile = DataSource("/home/krystian/Downloads/x.csv")
print(excelFile)
print(excelFile.printColumnNames())