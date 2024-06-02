#!/usr/bin/python3

'''
    quick doc
'''

import xml.etree.ElementTree as ET


def adder_recursive(element, parent):
    new = ET.SubElement(parent, element)
    if isinstance(element, dict):
        for sub_element in element:
            adder_recursive(sub_element, new)
    else:
        new.text = parent[element]


def serialize_to_xml(dictionary, filename):
    '''
        quick doc
    '''

    root = ET.Element('data')
    for element in root:
        adder_recursive(element, root)
    tree = ET.ElementTree(root)
    tree.write(filename)


def reader_recursive(element):
    if len(element):
        new_dict = {}
        for sub_element in element:
            new_dict[sub_element.tag] = reader_recursive(sub_element).text
        return new_dict
    else:
        return element


def deserialize_from_xml(filename):
    '''
        quick doc
    '''

    tree = ET.parse(filename)
    root = tree.getroot()
    return reader_recursive(root)
