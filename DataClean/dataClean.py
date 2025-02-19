import pandas as pd
import os

class Data:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.null_values = None
    
    def data_load(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("File %s not found" % self.file_path)
        self.df = pd.read_csv(self.file_path)
        print("Data loaded")

    def data_clean(self):
        self.df['date'] = pd.to_datetime(self.df[["year","month","day","hour"]])
        self.null_values = self.df[self.df["pm2.5"].isnull()].copy()
        self.df.drop(columns=["year","month","day","hour"], inplace= True)
        self.df['pm2.5'] = self.df["pm2.5"].interpolate(method='linear')
        self.df = pd.get_dummies(self.df, columns=['cbwd'], drop_first= True)
        print("Data cleaned")

    def data_get(self):
        if self.df is None:
            raise ValueError("Data not loaded")
        return self.df
    
    def data_null_values(self):
        return self.null_values
