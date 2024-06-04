# load libraries
import pandas as pd
import csv
import os
from datetime import date

# setup working environment
project_path = os.getcwd()
data_path = './Files/'
output_path = './Files/'

today = date.today()
today = today.strftime("%Y-%m-%d")
output_file = 'data_long.csv'

if not os.path.exists(output_path):
    os.mkdir(output_path)

# check data path for csv files
## files = os.listdir(data_path)
files = ['ERKER_v1.7_Testpat.csv']
files

# function to read data from csv file and convert to long format
def csv_to_long(file):
    prefix = file[3:-4]
    # read csv file into dataframe 
    data = pd.read_csv(data_path + file, sep=',', encoding='utf-8', dtype='object', encoding_errors='replace')
    print(data)

    # sort data by record_id / pseudonym
    data.sort_values(by=['record_id', 'sct_422549004'], inplace=True)
    data.head()

    # group by record_id / pseudonym to add index column IX to dataframe, corresponding to the sequence number within the group
    data['IX'] = data.groupby(['record_id', 'sct_422549004']).cumcount()+1
    data.head()

    # convert dataframe into long format using record_id / pseudonym / IX as id variables and column names (parameters) as variable names
    data_long = pd.melt(data, id_vars=['record_id', 'sct_422549004', 'IX'], var_name='source_id', value_name='source_value')
    data_long.sort_values(by=['record_id', 'sct_422549004'], inplace=True)
    data_long.rename(columns={'record_id': 'PID', 'sct_422549004': 'Source_PSN'}, inplace=True)
    data_long.head()

    return data_long

output = pd.DataFrame(columns = ['PID', 'Source_PSN', 'IX', 'source_id', 'source_value'])

for filename in files:
    print("Reading file: "+filename)
    output = pd.concat([output, csv_to_long(filename)], ignore_index=True)

output.shape
output.dropna(subset=['PID', 'Source_PSN', 'source_value'], how='all', inplace=True)
output.shape

# drop lines without source values
output.dropna(subset=['source_value'], inplace=True)
output.shape

# write output to csv file
output.to_csv(output_path + today + '_' + output_file, sep=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, index=False)
print("Data written to " + output_path + today + '_' + output_file)
