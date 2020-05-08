import unittest
import pandas as pd 
import numpy as np 
from wrangle import Wrangle

class WrangleMethodTester(unittest.TestCase):

    def test_null_checker(self):

        """
        Defines predetermined dataframe, runs it through the Wrangle 
        class and the null_checker function, then tests its output 
        against a predetermined result.
        """

        df = pd.DataFrame({'a': [5, 1, np.nan, 4], 'b': [2, np.nan, 12, np.nan]})
        df = Wrangle(df)
        self.assertEqual(df.null_checker(), print("There are 3 null values in this data frame."))

    def test_column_adder(self):
        
        """
        Defines two predetermined dataframes and a list, runs the first
        dataframe through the Wrangle class with predetermined parameters
        which is then run through the column_adder() function, and its 
        result is tested against the second dataframe using pd.shape and
        pd.columns.
        """

        df = pd.DataFrame({'a': [5, 1, np.nan, 4], 'b': [2, np.nan, 12, np.nan]})
        df2 = pd.DataFrame({'a': [5, 1, np.nan, 4], 'b': [2, np.nan, 12, np.nan], 'c': [15, 42, 6, np.nan]})
        my_list = [15, 42, 6]
        df = Wrangle(df, col_list=my_list, col_name='c')
        self.assertTrue(df.column_adder().shape == df2.shape)
        self.assertTrue(df.column_adder().columns.tolist(), df2.columns.tolist())

        

if __name__ == "__main__":
    unittest.main()