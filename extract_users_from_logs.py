# this script collects the unique IDs in each csv log file
# the IDs are then put into a separate csv file for easy access
# afterwards, for each unique ID, all logs are collected from each day
# each unique user will have their own csv file

def get_list(dir_files, dir_path_folder, pd, np, tqdm, time):
    # global variable
    unique_users = []

    with tqdm(total = len(dir_files)) as pbar:
        # go through each log csv file and collect unique ID numbers excluding NaNs
        for file_name in dir_files:
            if '.csv' in file_name:
                df = pd.read_csv(file_name)

                # get the index of User full name col
                user_index = df.columns.get_loc("User full name")

                # remove NaN data from the file
                df['User full name'].replace('', np.nan, inplace=True)
                df.dropna(subset=['User full name'], inplace=True)

                # get the data from col User full name
                user_ids = df.iloc[:,user_index]

                for i in user_ids:
                    if i not in unique_users:
                        unique_users.append(int(i))
            time.sleep(0.1)
            pbar.update(1)

    # create the data frame for the unique user list and sort
    data = {'ID':unique_users}
    df_users = pd.DataFrame(data)
    df_users = df_users.sort_values(by=['ID'])

    # put list of unique users in a file
    print("Total unique user IDs: " + str(len(unique_users)) + "\n")
    df_users.to_csv(dir_path_folder + '/unique user list.csv', index = False)
