# load libraries
from datetime import datetime
from datetime import date
import pandas as pd
import csv
import os

# setup OSSE environment
namespace = 'osse-46'
mdr_base = 'https://mdr.test.osse-register.de/rest/api/mdr/'

# setup working environment
project_path = os.getcwd()
data_path = './Files/'
mapping_path = './Files/'
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
data_filtered = pd.read_csv(data_path + 'orbis_long_mapped_filtered.csv', sep=';', encoding='utf-8', dtype='object', encoding_errors='replace')
data_filtered.head()
print("read filtered ORBIS data")

# function to retrieve date in ISO 8601 format (YYYY-MM-DD) from datetime (DD.MM.YYYY HH:MM)
def extract_date(original_datetime):
    original_date = datetime.strptime(original_datetime, '%d.%m.%Y %H:%M').date()
    iso_date = original_date.strftime('%Y-%m-%d')
    return iso_date

# function to check mapping for given value in enumerated items
def check_permitted_value(id, value):
    try:
        value = permitted_value_mapping.loc[(permitted_value_mapping['source_value']==value) & (permitted_value_mapping['source_id']==id),'pv_value'].item()
        return value
    except:
        return

# function to transform data (simple transformations in prototype e.g. date)
def transform_data(source_id, source_value, data_type, dataelement_id):
    value = source_value
    # transform datetime values to date in ISO 8601 format
    if data_type == 'DATE':
        value = extract_date(source_value)
        print(source_id + ': ' + source_value + ' transformed to ' + value + ' for ' + dataelement_id)
    # map and replace enumerated values with corresponding permitted value
    if data_type == 'enumerated':
        mapped_value = check_permitted_value(source_id, source_value)
        if  mapped_value != None:
            value = mapped_value
            print(source_id + ': ' + source_value + ' mapped to permitted value ' + value + ' for data element ' + dataelement_id)
        else:
            print(source_id + ': ' + source_value + ' mapping to permitted values for data element ' + dataelement_id + ' failed')
            value = None
    return value

data_transformed = data_filtered
data_transformed['source_value'] = data_transformed.apply(lambda x: transform_data(x['source_id'],x['source_value'],x['data_type'],x['dataelement_id']), axis=1)
data_transformed.to_csv(output_path + 'orbis_long_mapped_filtered_transformed.csv', sep=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, index=False)