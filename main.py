from dataAnalysis.DataSkecht.DataSource import DataSource


excelFile = DataSource("/home/krystian/Downloads/x.csv")
excelFile.printHead()
print(excelFile.printColumnNames())