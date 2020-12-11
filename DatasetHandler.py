# How To Use this class : 

# from DatasetHandler import DataHandler
# dh = DataHandler("Data.xlsx")
# df = dh.get_dataframe()
# print(model.extract_keywords(df['Abstract'][0]))
# ------------------------------------------------------------------------

import pandas as pd
import pathlib


class DataHandler:
    def __init__(self, location):
        self.type = pathlib.Path(location).suffix
        self.dataset_location = location
        
#         Use the pandas dataframe to get columns 
        if self.type == '.csv':
            self.df = pd.read_csv(location)
        elif self.type == '.xlsx':
            self.df = pd.read_excel(location)

    def get_dataframe(self):
        return self.df

