# load libraries
import xml.etree.ElementTree as et
from xml.dom import minidom
import pandas as pd
import os
from numpy import unicode_
import logging
import numpy as np
from classes import BHImport, Patient, Location, Episode, Form, Record, Dateelement
import json

# setup OSSE environment
namespace = 'osse-46'
mdr_base = 'https://mdr.test.osse-register.de/rest/api/mdr'

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
## read form id mapping
form_id_mapping = pd.read_csv(mapping_path + namespace + '_form_id_mapping.csv', sep=',', encoding='utf-8', dtype='object')
form_id_mapping.head()
print("read form id mapping")
## read orbis data
data_validated = pd.read_csv(data_path + 'orbis_long_mapped_filtered_transformed_validated.csv', sep=';', encoding='utf-8', dtype='object', encoding_errors='replace')
data_validated.head()
print("read validated ORBIS data")

# create import object
importObject = BHImport('urn:' + namespace, mdr_base)

def process_value(source_id, type, source_value):
    if type=="INTEGER":
         return str(int(float(source_value)))
    if type=="FLOAT":
        return str(float(str(source_value).replace(",","."))) #find a general solution
    if type=="STRING":
        return str(source_value)
    if type=="DATE":
        return str(source_value)
    if type=="enumerated":
        return str(source_value)
    return source_value

def process_data_row(row):
    patient_id = str(row.PID)
    episode_id = str(row.FALLNR)
    repeatable_entry_id = row.IX

    #data from the dataelement mapping
    curr_dataelement_mapping = dataelement_mapping.loc[dataelement_mapping['source_id']==row.source_id]
    if curr_dataelement_mapping.empty:
         raise Exception(f"Error while mapping dataelement {row}, no mapping found")
    data_type = curr_dataelement_mapping.data_type.values[0]
    form_id = curr_dataelement_mapping.form_id.values[0].split(":")[0]
    form_version = curr_dataelement_mapping.form_id.values[0].split(":")[1]
    form_id_external = f"form_{form_id}_ver-{form_version}"
    form_id_import = form_id_mapping.loc[form_id_mapping['form_id_external']==form_id_external,"form_id"].values[0]
    record_id = curr_dataelement_mapping.record_id.values[0]
    dataelement_id = curr_dataelement_mapping.dataelement_id.values[0]
    datelementArray = dataelement_id.split(":")
    dataelement_designation = curr_dataelement_mapping.dataelement_designation.values[0]
    
    #actual processing
    patient = importObject.getPatient(patient_id)
    patient_location = patient.getLocation("#all#")
    curr_episode = patient_location.getEpisode(episode_id,"import")
    curr_form = curr_episode.getForm(form_id_import,form_id_external)
    if pd.isnull(row.source_value):
        return
    value = process_value(curr_dataelement_mapping.source_id.item(), data_type, row.source_value)
    if pd.isnull(record_id):
        curr_form.addDataelement(f"Dataelement_{datelementArray[3]}_{datelementArray[4]}",dataelement_designation,value)
    else:
        #print("its a record")
        recordArray = record_id.split(":")
        record_designation = curr_dataelement_mapping.record_designation.item()
        curr_record = curr_form.getRecord(f"Record_{recordArray[3]}_{recordArray[4]}",record_designation)
        if form_id_mapping[form_id_mapping['dataelement_id']==f"Dataelement_{datelementArray[3]}_{datelementArray[4]}"].repeatable.values[0] == True: #check if repeatable
            curr_record.addDataelementToRow(f"Dataelement_{datelementArray[3]}_{datelementArray[4]}",dataelement_designation,value,repeatable_entry_id)
        else:
            curr_record.addDataelement(f"Dataelement_{datelementArray[3]}_{datelementArray[4]}",dataelement_designation,value)

data_validated.apply(process_data_row,axis=1)

xml_string = importObject.toXML()
print(xml_string)

output = open(output_path + 'import.xml', 'w', encoding = 'utf-8')
output.write(xml_string)
output.close()

