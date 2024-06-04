# load libraries
from json.decoder import JSONDecodeError
import requests
import os
import json

# setup OSSE environment
namespace = 'osse-46'
mdr_base = 'https://mdr.test.osse-register.de/rest/api/mdr/'

# setup working environment
project_path = os.getcwd()
data_path = './Files/'

# create output txt files
output_permittedValues = open(data_path + namespace + '_mdr_permittedValues.csv','w', encoding = 'utf-8')
output_permittedValues.write('"dataelement_id","dataelement_version","dataelement_urn","dataelement_status","dataelement_designation","dataelement_definition","pv_value","pv_designation","pv_definition"\n')

output_dataElements = open (data_path + namespace + '_mdr_dataelements.csv', 'w', encoding = 'utf-8')
output_dataElements.write('"dataelement_id","dataelement_version","dataelement_urn","dataelement_status","dataelement_designation","dataelement_definition","dataelement_datatype"\n')

# function to read all dataelements via search API
def get_elements():
    dataelements = []
    search_url = mdr_base + 'namespaces/' + namespace + '/search?query='
    print(search_url)
    search_result = requests.get(search_url)
    for result in search_result.json()['results']:
        if result['type'] == 'DATAELEMENT':
            dataelements.append(result['identification']['urn'])
    print(dataelements)
    return dataelements


# function to add permitted values to output file for a dataelement
def add_values(element, id, version):
    permissible_values = element.json()['validation']['permissible_values']
    for item in permissible_values:
        output_permittedValues.write('"' + id + '","' + version + '","' + element.json()['identification']['urn'] + '","' + element.json()['identification']['status'] + '","')
        output_permittedValues.write(element.json()['designations'][0]['designation'] + '","' + element.json()['designations'][0]['definition'] + '","')
        output_permittedValues.write(str(item['value']) + '","' + item['meanings'][0]['designation'] + '","' + item['meanings'][0]['definition'] + '"\n')
    return

# function to get element information from MDR, print to file and initiate add_values function if list
def read_element(element_id, element_version):
    mdr = mdr_base + 'dataelements/urn:' + namespace + ':dataelement:' + element_id + ':' + element_version
    dataelement = requests.get(mdr)

    try:
        output_dataElements.write('"' + element_id + '","' + element_version + '","' + dataelement.json()['identification']['urn'] + '","' + dataelement.json()['identification']['status'] + '","')
        output_dataElements.write(dataelement.json()['designations'][0]['designation'] + '","' + dataelement.json()['designations'][0]['definition'] + '","')
        output_dataElements.write(dataelement.json()['validation']['datatype'] + '"\n')

        if dataelement.json()['validation']['datatype'] == 'enumerated':
            add_values(dataelement,element_id,element_version)
    except JSONDecodeError as e:
        return None

index = 0
for urn in get_elements():
    urn_parts = urn.split(':')
    id = urn_parts[-2]
    version = urn_parts[-1]
    read_element(id, version)
    index += 1
    print(index)

# close output file
output_permittedValues.close()
output_dataElements.close()
