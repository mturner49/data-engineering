'''
Scenario:
For the new data source your business acquired, your product manager simply wants
their data files to be imported into an already existing table that contains ad metrics
because the existing table and the new data files contain the exact same columns.

However, since nothing is ever perfect in this world of data, there is one caveat.
The new data files contain a click_rate column but the datatype is float64, and the
existing table you will be apending these files to only takes in int64 values.

Your product manager does not want you to create an entirely new table for this new
data source, so she creates a task for you to convert the click_rate column from
float64 to int64, so that you can load those data files.

Instructions:
In the data/online_ads.csv file, you need to write a function to convert the click_rate
column from float64 to int64.
'''

import pandas as pd

# read data file into DataFrame
data = pd.read_csv("")

# add logic below to convert the click_rate column from float64 to int64