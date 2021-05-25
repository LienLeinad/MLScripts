# this script will concat all logs into one csv file

# imports
import os
import pandas as pd

dir_files = os.listdir()
dir_files_range = len(dir_files)
dir_path_folder = os.getcwd() + '\\user separate data'

if not os.path.exists(dir_path_folder):
    os.makedirs(dir_path_folder)

everything = pd.DataFrame()

for file_name in dir_files:
    if '.csv' in file_name:
        df = pd.read_csv(file_name)

        everything = pd.concat([everything, df], ignore_index=True)

everything.to_csv(dir_path_folder + '/concat data.csv', index = False)
print(everything.head)
