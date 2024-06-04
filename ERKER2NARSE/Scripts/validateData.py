# load libraries
from datetime import datetime
from datetime import date
import pandas as pd
import numpy as np
import csv
import os

# setup OSSE environment
namespace = 'osse-46'
mdr_base = 'https://mdr.test.osse-register.de/rest/api/mdr/'

# setup working environment
project_path = os.getcwd()
mapping_path = './Files/'
data_path = './Files/'
output_path = './Files/'

if not os.path.exists(output_path):
    os.mkdir(output_path)

# read data
## read dataelement mapping
dataelement_mapping = pd.read_csv(mapping_path + namespace + '_mapping_dataelements.csv', sep=';', encoding='utf-8', dtype='object')
dataelement_mapping.head()
print("read datelement mapping")
## read permitted values mapping
permitted_value_mapping = pd.read_csv(mapping_path + namespace + '_mapping_permitted_values.csv', sep=';', encoding='utf-8', dtype='object', keep_default_na=False)
permitted_value_mapping.head()
print("read permitted value mapping")
## read orbis data
data_transformed = pd.read_csv(data_path + 'orbis_long_mapped_filtered_transformed.csv', sep=';', encoding='utf-8', dtype='object', encoding_errors='replace')
data_transformed.head()
print("read transformed ORBIS data")

## function to validate data (basic validations, in the future using information from MDR)
def validate_data(source_id, source_value, data_type, dataelement_id):
    validation = False
    if data_type == 'DATE':
        if date.fromisoformat(source_value):
            validation = True
        else:
            print(source_value + ' (' + source_id + ') does not match expected date format for ' + dataelement_id)
            validation = False

    if data_type == 'STRING':    
        validation = True

    if data_type == 'INTEGER':
        try:
            int(source_value)
            validation = True
        except ValueError:
            print(source_value + ' (' + source_id + ') does not match expected INTEGER format for ' + dataelement_id)
            validation = False

    if data_type == 'FLOAT':
        try:
            float(source_value)
            validation = True
        except ValueError:
            print(source_value + ' (' + source_id + ') does not match expected FLOAT format for ' + dataelement_id)
            validation = False

    if data_type == 'enumerated':
        if  source_value != None:
            validation = True
        else:
            print('Mapping failed for source value ' + source_value + ' (' + source_id + ') to data element' + dataelement_id)
            validation = False

    return validation

data_validated = data_transformed
data_validated.shape
data_validated['validation'] = data_validated.apply(lambda x: validate_data(x['source_id'],x['source_value'],x['data_type'],x['dataelement_id']), axis=1)
data_validated = data_validated[data_validated['validation']]
data_validated.shape
data_validated.to_csv(output_path + 'orbis_long_mapped_filtered_transformed_validated.csv', sep=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, index=False)
