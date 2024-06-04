# load libraries
import pandas as pd
import numpy as np
import csv
import os

# setup OSSE environment
namespace = 'osse-46'

# setup working environment
project_path = os.getcwd()
mapping_path = './Files/'
data_path = './Output/'
output_path = './Output/'

if not os.path.exists(output_path):
    os.mkdir(output_path)

# read data
## read dataelement mapping
dataelement_mapping = pd.read_csv(mapping_path + namespace + '_mapping_dataelements.csv', sep=';', encoding='utf-8', dtype='object')
dataelement_mapping.head()
print("read datelement mapping")
## read orbis data
data = pd.read_csv(data_path + 'orbis_long.csv', sep=';', encoding='utf-8', dtype='object', encoding_errors='replace')
data.head()
print("read ORBIS data")

# data element mapping  
## map data to corresponding OSSE dataelements
data_mapped = data.merge(dataelement_mapping, how='left', on=['source_id'])
data_mapped.shape
data_mapped.to_csv(output_path + 'orbis_long_format_mapped.csv', sep=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, index=False)

## filter for data without corresponding data elements and write to csv
unmapped_data = data_mapped[data_mapped['dataelement_id'].isna()]
unmapped_data = pd.DataFrame(unmapped_data['source_id'].unique())
unmapped_data.to_csv(output_path + 'orbis_items_unmapped.csv', sep=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, index=False)

## filter for data with successful mapping and write to csv
data_filtered = data_mapped.dropna(subset=['dataelement_id'])
data_filtered.shape
data_filtered.to_csv(output_path + 'orbis_long_format_mapped_filtered.csv', sep=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, index=False)