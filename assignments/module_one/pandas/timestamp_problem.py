'''
Scenario:
Your business just adopted a new data source that tracks what ads are being
displayed on certain sites, and how many impressions and clicks each ad generates per day.

At the end of the day, that data source sends those files to you via some upstream process
irrelevant to you. Your product manager takes a look at the files and immediately notices
that the data does not contain a timestamp. 

She asks if you, the data engineer, are capable of attaching a timestamp to each record 
in the files as soon as we receive them from source. She wants the newly generated timestamp 
column to be named "ingestion_time".

Instructions:
The data file you will be working with is titled "online_ads.csv". The objective is to add
a timestamp column to the file that contains the ingestion timestamp (current timestamp) for
each row.
'''

import pandas as pd

# read data file into DataFrame
data = pd.read_csv("")