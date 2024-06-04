# load libraries
import pandas as pd
import csv
import os

# setup OSSE environment
namespace = 'osse-55'

# setup working environment
project_path = os.getcwd()
mapping_path = './Files/'
mapping_file = mapping_path + 'Mapping_ERKER_NARSE.xlsx'

# create data element mapping table
## read provided mapping information for dataelements from Excel file
mapping_dataelements = pd.read_excel(mapping_file, sheet_name = 'dataelements', dtype='object')
## filter for dataelements with mapping
mapping_dataelements = mapping_dataelements[mapping_dataelements['type'] == 'ORBIS']
## select required columns 
mapping_dataelements = mapping_dataelements[['source_id', 'form_name', 'form_id', 'dataelement_designation', 'dataelement_id', 'record_designation', 'record_id', 'data_type', 'data_format', 'unitOfMeasure', 'repeatable', 'mapping_comment']]
mapping_dataelements.head()
## write to csv file
mapping_dataelements.to_csv(mapping_path + namespace + '_mapping_dataelements.csv', sep=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, index=False)

# create permitted value mapping table
## read provided mapping information for dataelements from Excel file
mapping_permittedvalues = pd.read_excel(mapping_file, sheet_name = 'permittedValues', dtype='object')
mapping_permittedvalues.head()
## write to csv file
mapping_permittedvalues.to_csv(mapping_path + namespace + '_mapping_permitted_values.csv', sep=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, index=False)