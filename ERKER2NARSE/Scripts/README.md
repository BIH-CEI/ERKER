# ORBIS2OSSE

# Python-Skripte
1. mainzelliste-linkage.py
2. createDataLong.py
3. filterMapData.py
4. transformData.py
5. validateData.py
6. xsd_mapper.py
7. import.py
8. validate_xsd.py

## Record Linkage / Pseudonymisierung
### mainzelliste-linkage.py
* Input: Quelldaten aus ERKER (in `Files`)
* Output: pseudonymisierte ERKER-Daten (in `Files`)

## Datenbereinigung

### createDataLong.py
* Input: pseudonymisierte ERKER-Daten (in `Files`)
* Output: pseudonymisierte ERKER-Daten im Long-Format (`<date>_data_long.csv` in `Files`)

### loadMappingTables.py
* Input: Mapping-Tabelle (`<namespace>_mapping_orbis.xlsx`)
* Output: Mapping-Tabellen für Datenelemente (`<namespace>_mapping_dataelements.csv`) und permittedValues (`<namespace>_mapping_permitted_values.csv`)

### filterMapData.py
* Input: pseudonymisierte ERKER-Daten im Long-Format (`<date>_data_long.csv` in `Files`), Mapping-Tabellen für Datenelemente (`<namespace>_mapping_dataelements.csv`)
* Output: gemappte pseudonymisierte ERKER-Daten (`<date>_data_long_mapped` in `Files`), gefilterte pseudonymisierte ERKER-Daten (`<date>_data_long_mapped_filtered` in `4_mapping`)

## Transformation
### transformData.py
* Input: gefilterte pseudonymisierte ERKER-Daten (`<date>_data_long_mapped_filtered` in `Files`), Mapping-Tabellen für Datenelemente (`<namespace>_mapping_dataelements.csv`) und permittedValues (`<namespace>_mapping_permitted_values.csv`)
* Output: transformierte pseudonymisierte ERKER-Daten (`<date>_data_long_mapped_filtered_transformed` in `Files`)

## Datenvalidierung
### validateData.py
* Input: transformierte pseudonymisierte ERKER-Daten (`<date>_data_long_mapped_filtered_transformed` in `Files`), Mapping-Tabellen für Datenelemente (`<namespace>_mapping_dataelements.csv`) und permittedValues (`<namespace>_mapping_permitted_values.csv`)
* Output: validierte pseudonymisierte ERKER-Daten (`<date>_data_long_mapped_filtered_transformed_validated` in `Files`)

## Formatumwandlung
### xsd_mapper.py
* Input: -
* Output: Mapping der internen / externen Form-IDs `<namespace>_form_id_mapping.csv`

### import.py
* Input: validierte pseudonymisierte ERKER-Daten (`<date>_data_long_mapped_filtered_transformed_validated` in `Files`), Mapping der internen / externen Form-IDs `<namespace>_form_id_mapping.csv`, Mapping-Tabellen für Datenelemente (`<namespace>_mapping_dataelements.csv`) und permittedValues (`<namespace>_mapping_permitted_values.csv`), Python-Module (`helper.py`, `classes.py`)
* Output: XML-Datei für OSSE-Import (`<date>_import.xml` in `Files`)


## Formatvalidierung
### validate_xsd.py
* Input: XML-Datei für OSSE-Import (`<date>_import.xml` in `Files`)
* Output: -


# verwendete Python Bibliotheken
## Python 3.9.13 Standardbibliotheken
* csv
* datetime
* json
* os
* sys
* xml.dom
* xml.etree.ElementTree

## weitere Bibliotheken
* numpy, Version 1.21.5
* openpyxl, Version 3.0.10
* pandas Version, Version 1.4.4
* requests, Version 2.28.1
* xmlschema, Version 2.2.3