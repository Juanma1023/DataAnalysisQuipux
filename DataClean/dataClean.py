import pandas as pd
import os

class Data:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.null_values = None
    
    def load_data(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("File %s not found" % self.file_path)
        self.df = pd.read_csv(self.file_path)
        print("Data loaded")

    def clean_data(self):
        self.df['date'] = pd.to_datetime(self.df[["year","month","day","hour"]])
        self.null_values = self.df[self.df["pm2.5"].isnull()].copy()
        self.df.drop(columns=["year","month","day","hour"], inplace= True)
        self.df["pm2.5"] = self.df["pm2.5"].interpolate(method='linear',limit_direction='both')
        self.df = pd.get_dummies(self.df, columns=['cbwd'], drop_first= True)
        print("Data cleaned")
        print(self.df)

    def get_data(self):
        if self.df is None:
            raise ValueError("Data not loaded")
        return self.df
    
    def null_values_data(self):
        return self.null_values
