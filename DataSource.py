import pandas as pd

class DataSource:

    def __init__(self, dataSourceLink):
        self.datasource = pd.read_csv(dataSourceLink)

    def printColumnNames(self):
        return list(self.datasource.keys())



