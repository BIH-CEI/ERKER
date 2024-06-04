from __future__ import annotations
from helper import addMisc
import xml.etree.ElementTree as et
from xml.dom import minidom
from typing import Optional
from xml.sax.saxutils import unescape
from pathlib import Path


class BHImport:

    def __init__(self, namespace: str, mdrURL: str):
        imp_BHImport = et.Element('BHImport')
        imp_BHImport.set(
            'xmlns', 'http://registry.samply.de/schemata/import_v1')
        mdr_node = addMisc(imp_BHImport, 'Mdr')
        addMisc(mdr_node, 'URL', text=mdrURL)
        addMisc(mdr_node, 'Namespace', text=namespace)
        self.xml = imp_BHImport
        self.patients = {}
        self.namespace = namespace
        self.mdrURL = mdrURL
        

    def addPatient(self, patient_id: str) -> Patient:
        self.patients[patient_id] = Patient(patient_id, self)
        return self.patients[patient_id]

    def getPatient(self, patient_id: str,create: bool = True) -> Patient:
        if patient_id in self.patients:
            return self.patients[patient_id]
        if create:
            return self.addPatient(patient_id)
        raise Exception("Patient not Found!")


    def makeXML(self,sort_table,split:bool=False,chunk_size:int=10) -> str|dict:
        if not split:
            self.serialization_result = self.makeXMLForPatientList(self.patients, sort_table)
            return self.serialization_result
        else:
            result = {}
            patient_list = list(self.patients.items())
            for i in range(0,len(patient_list),chunk_size):
                patients_chunk = dict(patient_list[i:i+chunk_size])
                result[i]=self.makeXMLForPatientList(patients_chunk, sort_table)
            self.serialization_result = result
            return self.serialization_result     
    
    def makeXMLForPatientList(self,patient_dict,sort_table) -> str:
        imp_BHImport = et.Element('BHImport')
        imp_BHImport.set(
                'xmlns', 'http://registry.samply.de/schemata/import_v1')
        mdr_node = addMisc(imp_BHImport, 'Mdr')
        addMisc(mdr_node, 'URL', text=self.mdrURL)
        addMisc(mdr_node, 'Namespace', text=self.namespace)
        for patient_id, patient in patient_dict.items():
            patient.makeXML(imp_BHImport,sort_table)
        return unescape(minidom.parseString(et.tostring(imp_BHImport, encoding='unicode', method='xml')).toprettyxml(indent="   "),{"&apos;": "'", "&quot;": '"'})

    def write_xml(self, name:str):
        if self.serialization_result==None:
            raise Exception("Please call makeXML before write_xml")
        if type(self.serialization_result) == dict:
            Path(f"./{name}").mkdir(parents=True, exist_ok=True)
            for chunk_id, xml in self.serialization_result.items():
                output = open(f"./{name}/chunk_{chunk_id}.xml", 'w', encoding = 'utf-8')
                output.write(xml)
                output.close()
            return
        if type(self.serialization_result) == str:
            output = open(f'{name}.xml', 'w', encoding = 'utf-8')
            output.write(self.serialization_result)
            output.close()
            return      
        raise Exception("Unable to write xml!")
    
class Patient:
    def __init__(self, patient_id: str, import_object: BHImport):
        self.patient_id = patient_id
        self.import_object = import_object
        self.locations = {}

    def addLocation(self, location_name: str) -> Location:
        self.locations[location_name] = Location(location_name, self)
        return self.locations[location_name]
    
    def getLocation(self, location_name: str,create: Optional[bool] = True) -> Location:
        if location_name in self.locations:
            return self.locations[location_name]
        if create:
            return self.addLocation(location_name)
        raise Exception("Location not Found!")

    def makeXML(self,parent_node,sort_table):
        patient_node = addMisc(parent_node, 'BHPatient')
        addMisc(patient_node, 'Identifier', {'encrypted': ''}, self.patient_id)
        locations_node = addMisc(patient_node, 'Locations')
        for location_name, location in self.locations.items():
            location.makeXML(locations_node,sort_table)



class Location:

    def __init__(self, location_name: str, patient_object: Patient):
        self.location_name = location_name
        self.patient_object = patient_object
        self.episodes={}
        self.forms= {}

    def addEpisode(self,name:str, optional_text:str) -> Episode:
        self.episodes[name] = Episode(name,optional_text, self)
        return self.episodes[name]

    def getEpisode(self, name: str,optional_text:str ,create: bool = True) -> Episode:
        if name in self.episodes:
            return self.episodes[name]
        if create:
            return self.addEpisode(name, optional_text)
        raise Exception("Episode not Found!")
    
    def addForm(self, form_id:str, form_name:str) -> Form:
        self.forms[form_id] = Form(form_id,form_name, self)
        return self.forms[form_id]
    
    def getForm(self, form_id:str, form_name:str ,create: bool = True) -> Form:
        if form_id in self.forms:
            return self.forms[form_id]
        if create:
            return self.addForm(form_id, form_name)
        raise Exception("Form not Found!")
    
    def makeXML(self,locations_node,sort_table):
        location_node = addMisc(locations_node,'Location', {'name': self.location_name})
        base_data_node = addMisc(location_node, 'BasicData')
        episodes_node = addMisc(location_node, 'Episodes')
        
        sorted_forms = (self.forms[form_id] for form_id in sort_table["base_forms"] if form_id in self.forms.keys())
        for form in sorted_forms:
            form.makeXML(base_data_node,sort_table)
        for episode_name, episode in self.episodes.items():
            episode.makeXML(episodes_node,sort_table)

class Episode:

    def __init__(self, name: str, optional_text:str, location_object: Location):
        self.name = name
        self.optional_text = optional_text
        self.location_object = location_object
        self.forms= {}

    def addForm(self, form_id:str, form_name:str) -> Form:
        self.forms[form_id] = Form(form_id,form_name, self)
        return self.forms[form_id]
    
    def getForm(self, form_id:str, form_name:str ,create: bool = True) -> Form:
        if form_id in self.forms:
            return self.forms[form_id]
        if create:
            return self.addForm(form_id, form_name)
        raise Exception("Form not Found!")
    
    def makeXML(self,episodes_node,sort_table):
        episode_node =  addMisc(episodes_node, 'Episode', {'name':self.name,'optionalText':self.optional_text})
        logi_node = addMisc(episode_node, 'LogitudinalData')
        
        sorted_forms = (self.forms[form_id] for form_id in sort_table["episode_forms"] if form_id in self.forms.keys())
        for form in sorted_forms:
            form.makeXML(logi_node,sort_table)

class Form:

    def __init__(self, form_id:str, form_name:str, form_parent:Episode|Location):
        self.form_id = form_id
        self.form_name = form_name
        self.records={}
        self.dataelements={}

    def addDataelement(self, dataelemnt_id:str, col_name:str,value:str, repeatable: bool = False) -> Dateelement:
        if not repeatable:
            self.dataelements[dataelemnt_id] = Dateelement(dataelemnt_id, col_name,value)
            return self.dataelements[dataelemnt_id]
        else:
            if dataelemnt_id not in self.dataelements:
                self.dataelements[dataelemnt_id] = Dateelement(dataelemnt_id, col_name,"")
            self.dataelements[dataelemnt_id].addValue(value)

    def addRecord(self, record_id:str, record_name:str,is_repeatable: bool = False) -> Record:
        self.records[record_id] = Record(record_id, record_name, self,is_repeatable)
        return self.records[record_id]

    def getRecord(self, record_id:str, record_name:str,is_repeatable: bool = False,create: bool = True) -> Record:
        if record_id in self.records:
            return self.records[record_id]
        if create:
            return self.addRecord(record_id, record_name, is_repeatable)
        raise Exception("Record not Found!")

    def makeXML(self,parent_node,sort_table):
        form_node = addMisc(parent_node, self.form_id,{'name':self.form_name})
        for record_id, record in self.records.items():
            record.makeXML(form_node,sort_table)
        for data_element_id, data_element in self.dataelements.items():
            data_element.makeXML(form_node)

class Record:

    def __init__(self, record_id:str, record_name:str, form:Form, is_repeatable: bool = False):
        self.record_id = record_id
        self.record_name = record_name
        self.rows = {}
        self.form = form
        self.is_repeatable = is_repeatable

    def addDataelement(self, dataelemnt_id:str, col_name:str,value:str, row_index:int = 0) -> Dateelement:
        if  row_index not in self.rows:
            self.rows[row_index] = Row(self)
        return self.rows[row_index].addDataelement(dataelemnt_id,col_name,value) 

    def makeXML(self,form_node,sort_table):
        record_node = addMisc(form_node,  self.record_id,{'name':self.record_name})
        for row_index, row in self.rows.items():
            parent_node = record_node
            if self.is_repeatable:
                parent_node = addMisc(record_node, 'Row')
            row.makeXML(parent_node,sort_table)


class Row:

    def __init__(self, record:Record):
        self.dataelements = {}
        self.record = record
    
    def addDataelement(self, dataelemnt_id:str, col_name:str,value:str) -> Dateelement:
        self.dataelements[dataelemnt_id] = Dateelement(dataelemnt_id, col_name,value)
        return self.dataelements[dataelemnt_id]
    
    def makeXML(self,record_node,sort_table:dict):
        sorted_data_elements = (self.dataelements[data_element_id] for data_element_id in sort_table[(self.record.form.form_id,self.record.record_id)] if data_element_id in self.dataelements.keys())
        for data_element in sorted_data_elements:
            data_element.makeXML(record_node)

class Dateelement:

    def __init__(self, dataelemnt_id:str, col_name:str,value:str):#, parent:et.Element):
        self.data_element_id=dataelemnt_id
        self.col_name = col_name
        self.value = value
        self.values = []

    def addValue(self,value):
        self.values.append(value)

    def makeXML(self,parent_node):
        data_element_node = addMisc(parent_node, self.data_element_id, {'name': self.col_name}, str(self.value))
        for value in self.values:
           addMisc(data_element_node, "Value", {}, str(value)) 
