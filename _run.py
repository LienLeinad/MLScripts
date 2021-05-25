# runs the scripts

# imports
import os
import pandas as pd
import numpy as np
import time
from tqdm import tqdm
from extract_users_from_logs import get_list
from extract_data_based_on_users import get_user_data
from extract_dropped_student_data import get_retained_student

# makes the folder to story the files in afterwards
dir_files = os.listdir()
dir_files_range = len(dir_files)
dir_path_folder = os.getcwd() + '\\user separate data'
# print(dir_files)
if not os.path.exists(dir_path_folder):
    os.makedirs(dir_path_folder)

# call all functions here
get_list(dir_files, dir_path_folder, pd, np, tqdm, time)
get_user_data(dir_files, dir_path_folder, pd, np, tqdm, time)
get_retained_student(dir_files,dir_path_folder,pd,np,tqdm,time)
option = input("Press any key to continue")
