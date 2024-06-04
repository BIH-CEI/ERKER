# load libraries
import xmlschema
import pandas as pd

# setup OSSE environment
registry_namespace = 'osse-46'
registry_url = ''

# setup working environment
project_path = os.getcwd()
mapping_path = './Files/'

# retrieve XML schema via registry URL
schema = xmlschema.XMLSchema(registry_url + 'schemata/import_v1.xsd')
print(schema.findall('BHImport/BHPatient/*'))

base_forms = schema.findall('BHImport/BHPatient/Locations/Location/BasicData/*',{'': 'http://registry.samply.de/schemata/import_v1'})
episode_forms = schema.findall('BHImport/BHPatient/Locations/Location/Episodes/Episode/LogitudinalData/*',{'': 'http://registry.samply.de/schemata/import_v1'})
form_collection = {"base_form":base_forms,"episode_form":episode_forms}
result_frame = pd.DataFrame()
result = {"form_type":[],"form_id":[],"form_id_external":[],"record_id":[] , "dataelement_id":[],"repeatable":[]}
for form_type, forms in form_collection.items():
    for form in forms:
        dataelements = form.findall('*[contains(name(),"Data")]',{'': 'http://registry.samply.de/schemata/import_v1'})
        form_id_external = form.attributes.get("name").value_constraint
        for dataelement in dataelements:
            result["form_type"].append(form_type)
            result["form_id"].append(form.prefixed_name)
            result["form_id_external"].append(form_id_external)
            result["dataelement_id"].append(dataelement.prefixed_name)
            result["record_id"].append("")
            result["repeatable"].append(False)

        records = form.findall('*[contains(name(),"Record")]',{'': 'http://registry.samply.de/schemata/import_v1'})
        for record in records:
            nested_dataelements = record.findall('*[contains(name(),"Data")]',{'': 'http://registry.samply.de/schemata/import_v1'})
            for dataelement in nested_dataelements:
                result["form_type"].append(form_type)
                result["form_id"].append(form.prefixed_name)
                result["form_id_external"].append(form_id_external)
                result["dataelement_id"].append(dataelement.prefixed_name)
                result["record_id"].append(record.prefixed_name)
                result["repeatable"].append(False)
            nested__repeatable_dataelements = record.findall('*/*[contains(name(),"Data")]',{'': 'http://registry.samply.de/schemata/import_v1'})
            for dataelement in nested__repeatable_dataelements:
                result["form_type"].append(form_type)
                result["form_id"].append(form.prefixed_name)
                result["form_id_external"].append(form_id_external)
                result["dataelement_id"].append(dataelement.prefixed_name)
                result["record_id"].append(record.prefixed_name)
                result["repeatable"].append(True)
result_frame = result_frame.from_dict(result)
result_frame.to_csv(mapping_path + registry_namespace + '_form_id_mapping.csv',index=False)