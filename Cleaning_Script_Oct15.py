import os
import pandas as pd
import time
from tqdm import tqdm

# Removes the Origin and IP Address Column
# Removes login errors

print('Starting cleaning...')
time.sleep(2)

#get the directory files and new path to save the files
dir_files = os.listdir()
dir_files_range = len(dir_files)
dir_path_folder = os.getcwd() + '\\cleaned files'

# create a folder
print('Creating new folder...')
time.sleep(2)
if not os.path.exists(dir_path_folder):
    print('No new folder found')
    time.sleep(3)
    print('Creating folder')
    os.makedirs(dir_path_folder)
    time.sleep(3)
    print('Folder created\n')
    time.sleep(3)
else:   
    print('New folder already exists\n')
    time.sleep(3)

# go through the files
print('Cleaning Files...')
time.sleep(1)
with tqdm(total=dir_files_range, desc="Running...") as pbar:
    n = 1
    for i in dir_files:
        file_name = i

        if '.csv' in file_name:
            df = pd.read_csv(file_name, )

            # Remove Origin and IP Address Cols
            df = df.drop(columns = ['Origin', 'IP address'])
            
            # Remove Log in Errors
            df = df[df['Event name'] != 'User login failed']
            
            # Remove Change of Password (Remove all user id = 0 since this is moodle admin) 
            df = df[df['User full name'] != 0]
            
            # Remove Updating of Password
            df = df[df['Event name'] != 'User password updated']
            
            # Remove 'Web service token created'
            df = df[df['Event name'] != 'Web service token created']
            
            # Remove 'Web service token sent'
            df = df[df['Event name'] != 'Web service token sent']
            
            # Remove 'Web service function called'
            df = df[df['Event name'] != 'Web service function called']
            
            # Remove 'Web service login failed'
            df = df[df['Event name'] != 'Web service login failed']
            
            #print(file_name + ' ----- DONE')
            df.to_csv(dir_path_folder + '/' + file_name, index = False)

        #else:
            #print(file_name + ' ----- skipped')
        time.sleep(0.3)
        pbar.update(n)

print('\nCleaning script END\n')
input('Press ENTER to close the script')
