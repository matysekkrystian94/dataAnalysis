import pandas as pd
from DataSource import DataSource


excelFile = DataSource("C:\\Users\\krystian\\Desktop\\x.csv")
print(excelFile)
print(excelFile.printColumnNames())