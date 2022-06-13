'''
Scenario:
Your team just acquired another data source that, again, drops you daily files
in your desired Google Cloud Storage landing bucket.

Upon the initial data drop, you notice that the data the source provides contains PII (Personally Identifiable Information)
that your team, legally, can not consume. The file also contain data formatting issues that will lead to problems when you
ingest the files.

Instructions:
Using the csv file "data/pii_data.csv"
1. Write a method to exclude the PII data (card_number, cvv)
2. Change the date format from mm/dd/yyyy to yyyy-mm-dd
'''

import pandas as pd

# read data file into DataFrame
data = pd.read_csv("")

# add logic below to convert the click_rate column from float64 to int64