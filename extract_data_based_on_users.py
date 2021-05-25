# this script gets the unique student IDs from the file unique user list.csv
# outputs a prompt on which user to select the data from
# from the selected user, the script will go through the logs and get the data
# a new file will be created for that specific user and so forth

def get_user_data(dir_files, dir_path_folder, pd, np, tqdm, time):
    # get the user data (assuming there is an existing foler that contains this)
    df_users = pd.read_csv(dir_path_folder + '/unique user list.csv')

    # prompts to pick a range of data from the user data set
    clear = True
    start_index = 0
    end_index = 0

    while clear:
        print("Which range of users would you want to extract? ")
        print("Total unique users: " + str(df_users.size) + " where index is from 0 to " + str(df_users.size - 1))
        
        ranges = input().split('-')
        start_index = int(ranges[0])
        end_index = int(ranges[1])

        if start_index > end_index:
            print("Please input a valid range")
        else:
            print("Start: " + str(start_index) + " End: " + str(end_index) + "\nIs this correct? [Y/N]")
            choice = input()
            if choice.lower() == 'y':
                clear = False
            elif choice.lower() == 'n':
                print("Please input again")
            else:
                print("Restarting")

    # get number of csv files
    csv_len = 0
    for file_name in dir_files:
        if '.csv' in file_name:
            csv_len += 1
            
    new_start = 0
    if start_index == 0:
        new_start = 1

    with tqdm(total = (new_start + end_index)*csv_len) as pbar:    
        # goes through the list of users then goes through the list of files
        while start_index <= end_index:
            frames = [] # to be used later to concat the frames from different files
            user_id = df_users.iloc[start_index,0] # get the user id value
            
            for file_name in dir_files:
                if '.csv' in file_name:
                    df_log = pd.read_csv(file_name)

                    # check rows with the user_id and add the new frame to frames[]
                    df_new = df_log.loc[df_log['User full name'] == user_id]
                    frames.append(df_new)

                    time.sleep(0.1)
                    pbar.update(1)

            # after getting the data from the files, concat the frames into a new df
            # then make a new file
            user_df = pd.concat(frames)
            user_df.to_csv(dir_path_folder + '/' + str(user_id) + " data.csv", index = False)    
                        
            start_index += 1
