# wrangle.py

import pandas as pd

class Wrangle():

    def __init__(self, df, col_list=None, col_name=None):

        self.df = df
        self.col_list = col_list
        self.col_name = col_name

    def column_adder(self):

        """
        Takes in pandas dataframe and adds a new column determined by a
        inputted list.

        Parameters
        ----------
        df : pandas DataFrame
            Base dataframe to be added to
        col_list : list
            List to be used as new column
        col_name : str
            String to be used as name of new column

        Returns
        -------
        pandas DataFrame
            Dataframe with new column
        """

        self.df[self.col_name] = pd.Series(self.col_list)
        return self.df

    def null_checker(self):

        """
        Takes in pandas dataframe, checks it for null values, and
        prints out a string with the number of null values.

        Parameters
        ----------
        df : pandas DataFrame
            Dataframe to be used to check for null values

        Returns
        -------
        str
            One line exclaiming number of null values in dataframe
        """

        num_nulls = self.df.isnull().sum().sum()

        print(f"There are {num_nulls} null values in this data frame.")
