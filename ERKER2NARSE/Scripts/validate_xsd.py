# load libraries
import xmlschema

# setup OSSE environment
registry_namespace = 'osse-46'
registry_url = ''

# setup working environment
project_path = os.getcwd()
mapping_path = './Files/'
data_path = './Files/'

schema = xmlschema.XMLSchema(registry_url + 'schemata/import_v1.xsd')
print(schema.validate(data_path + "import.xml"))
