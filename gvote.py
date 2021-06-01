#!/usr/bin/python3
#
import pandas as pd
import tools
import sys
#
file = '/mnt/chromeos/GoogleDrive/MyDrive/Voter/202012_VRDB_Extract.txt'
# Search term - search acroos all columns
search = sys.argv[1]
#
# Read chunks 10K each
# within each chunk search across all columns cor the search term
#
for chunk in pd.read_csv(file, sep='|', chunksize=10000, engine='python'):
    match = chunk[chunk.isin([search]).any(axis=1)]
    if not match.empty:
        # crerate a df with the specific columns only
        df = match[['LName', 'FName', 'Birthdate', 'Gender',
                    'RegStNum', 'RegStName', 'RegStType', 'RegCity', 'RegZipCode']]
        # create a list from the df
        data_line = df.values.tolist()
        # for each list element print the formatted data
        for lname, fname, birthdate, gender, regstnum, regstname, regsttype, regcity, regzipcode in data_line:
            print(
                f'{lname:15} {fname:10} {birthdate:10} {regstnum:6} {regstname:15} {regsttype:5} {regcity}')
