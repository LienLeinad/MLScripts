import os
import pandas as pd

# takes the ids from the Description column to replace the
# User full name and Affected user columns in the file

print('Anonymization script START')

dir_files = os.listdir()

for i in dir_files:
    file_name = i

    if '.csv' in file_name:
        df = pd.read_csv(file_name, )
        
        desc_index = df.columns.get_loc("Description")
        # regex
        r_user = r'^(?:The user with id \')([0-9]+)'
        r_affected_user = r'(?:the user with id \')([0-9]+)'

        s = pd.Series(df.iloc[:,desc_index], dtype="string")
        df['User full name'] = s.str.extract(r_user)
        df['Affected user'] = s.str.extract(r_affected_user)

        print(file_name + ' ----- DONE')
        df.to_csv(file_name, index = False)

    else:
        print(file_name + ' ----- skipped')

print('Anonymization script END')
