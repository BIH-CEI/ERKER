import xml.etree.ElementTree as et

def addMisc(parent_node, node_id, attributes_map:dict={}, text="") -> et.Element:
    child_node = et.SubElement(parent_node,node_id)
    for key, value in attributes_map.items():
        child_node.set(key, value)
    child_node.text = text
    return child_node