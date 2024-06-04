# load libraries
import pandas as pd
import csv
import os
import requests
from datetime import datetime

# setup working environment
project_path = os.getcwd()
data_path = './Files/'
output_path = './Files/'

if not os.path.exists(output_path):
    os.mkdir(output_path)

# setup Mainzelliste environment
mainzellisteApiKey = ''
mainzellisteURL = ''

mainzelliste_headers_json = {'mainzellisteApiKey': mainzellisteApiKey,
                             'ContentType': 'application/json',
                             'Accept': 'application/json'}

# check data path for csv files
files = os.listdir(data_path)
files

# loop through files (original datasets) to retrieve list of pids for pseudonymization
## function to read data from csv file and extract pids
def extract_ids(file):
    data = pd.read_csv(data_path + file, sep=';', encoding='utf-8', dtype='object', encoding_errors='replace')
    return data['PID'].tolist()

## loop through source files to create lists of orbis pids
pids = []
for filename in files:
    print("Reading file: " + data_path + filename)
    ids = extract_ids(filename)
    pids += ids

# create pseudonym dictionary for pids (orbisid -> osseid)
## function to create Mainzelliste session
def create_mzl_session():
    response = requests.post(mainzellisteURL + 'sessions/', headers=mainzelliste_headers_json)
    if response.status_code != 201:
        print('Could not create session - Mainzelliste returned status code ' + str(response.status_code))
        return None
    session = response.json()
    return session['uri']

## function to create readPatient token
def get_read_patients_token(session, search_id):
    token_data_json = {"type": "readPatients", "data": {"searchIds": search_id, "resultIds":["orbisid", "pid"]}}
    response = requests.post(session + 'tokens/', json=token_data_json, headers=mainzelliste_headers_json)
    if response.status_code != 201:
        print('Could not create token - Mainzelliste returned status code ' + str(response.status_code) + str(response.content))
        return None
    return response.json()['tokenId']

## create Mainzelliste session
session_url = create_mzl_session()

## create empty dictionary of pid pseudonyms
pid_dict = {}
## loop through dataset pids to fill dictionary of pid pseudonyms
for pid in list(set(pids)):
    # create Mainzelliste token for given pid
    token_id = get_read_patients_token(session_url, [{'idType': 'orbisid', 'idString': pid}])
    if token_id != None:
        # get ids from Mainzelliste using the generated token
        result = requests.get(mainzellisteURL + 'patients?tokenId=' + token_id, headers=mainzelliste_headers_json)
        # add pseudonym to dictionary of pid pseudonyms
        pid_dict.update({result.json()[0]['ids'][0]['idString']: result.json()[0]['ids'][1]['idString']})
    else:
        pid_dict.update({pid: 'Unknown'})

# create pseudonym dictionary for fallids (fallid -> episode_date)
## function to retrieve date in ISO 8601 format (YYYY-M<M-DD) from datetime (DD.MM.YYYY HH:MM)
def extract_date(original_datetime):
    original_date = datetime.strptime(original_datetime, '%d.%m.%Y %H:%M').date()
    iso_date = original_date.strftime('%Y-%m-%d')
    return iso_date
## create empty dictionary of fallid pseudonyms
fallid_dict = {}
## loop through encounter data to fill dictionary of fallid pseudonyms
fall_data = pd.read_csv(data_path + 'DIZ_KD_Fall_Encounter.csv', sep=';', encoding='utf-8', dtype='object', encoding_errors='replace')
for i in range(0,len(fall_data)):
    fallid_dict.update({fall_data['FALLNR'][i]: extract_date(fall_data['AUFNDAT'][i])})

# pseudonymize pid (orbisid -> osseid) and fallid (fallid -> episode) in datasets
## function to replace pid (orbisid) with pseudonym (osseid) and fallnr with episode_date from dictionaries of pseudonyms
## for values without valid pseudonym: Unknown
def replace_id(file):
    data = pd.read_csv(data_path + file, sep=';', encoding='utf-8', dtype='object', encoding_errors='replace')
    data.replace({'PID': pid_dict}, inplace=True)
    # data.replace({'FALLNR': fallid_dict}, inplace=True)
    data['FALLNR'] = data['FALLNR'].map(fallid_dict).fillna('Unknown')
    return data

## loop through source files and replace PID (orbisid) with OSSE ID (pid), save in new CSV file
for filename in files:
    print("Reading file: " + data_path + filename)
    output = replace_id(filename)
    output.to_csv(output_path + 'ps_' + filename, sep=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, index=False)
    print("Writing file: " + output_path + 'ps_' + filename)