import pandas as pd
import numpy as np
from wrangle import Wrangle

# File to manually test Wrangle class

if __name__ == "__main__":
    
    ran_df = pd.DataFrame({"a": [1, 2, np.nan, 4], "b": [5, 6, 7, np.nan]})
    my_list = [3, 7, 1]

    nulls = Wrangle(df=ran_df) # Instantiate Wrangle class
    nulls.null_checker() # Run nulls through null_checker function

    print(ran_df) # Print dataframe prior to adding column

    # Instantiate Wrangle class with new parameters
    ran_df = Wrangle(ran_df, col_list=my_list, col_name='c')
    # Run dataframe through column_adder
    ran_df = ran_df.column_adder()

    print(ran_df) # Print dataframe after adding new column