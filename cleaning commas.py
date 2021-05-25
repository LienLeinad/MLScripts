import os
import pandas as pd
import numpy as np
import time
from tqdm import tqdm

dir_files = os.listdir()


for file_name in dir_files:
    if '.csv' in file_name:
        df = pd.read_csv(file_name)
       
        # cleaning the data
        # splitting the date and time from the Time column

        df['new_date'] = pd.to_datetime(df['Time']).dt.date
        df['new_time'] = pd.to_datetime(df['Time']).dt.time
        df = df.drop(['Time'], axis = 1)

        # Event context commas

        event_context_index = df.columns.get_loc("Event context")
        event_contexts = df.iloc[:,event_context_index]
        item_index = 0

        for i in event_contexts:
            if ',' in i:
                i = i.replace(',', ' ')
                df.iloc[item_index,event_context_index] = i
            item_index = item_index + 1

        df.to_csv(file_name, index = False)

        # Description

        description_index = df.columns.get_loc("Description")
        descriptions = df.iloc[:,description_index]
        item_index = 0

        for j in descriptions:
            if ',' in j:
                j = j.replace(',', ' ')
                df.iloc[item_index,description_index] = j
            item_index = item_index + 1

        df.to_csv(file_name, index = False)

option = input("Press any key to continue")
