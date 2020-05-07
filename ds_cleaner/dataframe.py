import pandas as pd
import numpy as np
from lambdata_daniel_benson.wrangle import Wrangle

if __name__ == "__main__":

    ran_df = pd.DataFrame({"a": [1, 2, np.nan, 4], "b": [5, 6, 7, np.nan]})
    my_list = [3, 7, 1]

    nulls = Wrangle(df=ran_df)
    nulls.null_checker()

    print(ran_df)

    ran_df = Wrangle(ran_df, col_list=my_list, col_name='c')
    ran_df = ran_df.column_adder()

    print(ran_df)