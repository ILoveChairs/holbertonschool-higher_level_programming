#!/usr/bin/python3

'''
    quick doc
'''

import xml.etree.ElementTree as ET


def adder_recursive(key, parent_dict, parent_element):
    new = ET.SubElement(parent_element, key)
    if isinstance(parent_dict[key], dict):
        for sub_key in parent_dict[key]:
            adder_recursive(sub_key, parent_dict[key], new)
    else:
        new.text = str(parent_dict[key])


def serialize_to_xml(dictionary, filename):
    '''
        quick doc
    '''

    root = ET.Element('data')
    for element in dictionary:
        adder_recursive(element, dictionary, root)
    tree = ET.ElementTree(root)
    ET.indent(tree)
    tree.write(filename)


def reader_recursive(element):
    if len(element):
        new_dict = {}
        for sub_element in element:
            content = reader_recursive(sub_element)
            if not len(content):
                new_dict[sub_element.tag] = reader_recursive(sub_element).text
            else:
                new_dict[sub_element.tag] = reader_recursive(sub_element)
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
