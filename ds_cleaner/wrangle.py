# wrangle.py
import pandas as pd

class Wrangle():
    def __init__(self, df, col_list=None, col_name=None):
        self.df = df
        self.col_list = col_list
        self.col_name = col_name

    def column_adder(self):
        self.df[self.col_name] = pd.Series(self.col_list)
        return self.df

    def null_checker(self):
        num_nulls = self.df.isnull().sum().sum()

        print(f"There are {num_nulls} null values in this data frame.")
