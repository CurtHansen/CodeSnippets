"""
This module features a class that converts XML to JSON.
The entire JSON construct will be an outer dict with inner dicts and lists.
"""

import re

SUPPORTED_NAMESPACE = '{http://www.factset.com/callstreet/xmllayout/v0.1}'


def convert_xml_to_json(root_node,
                        list_nodes_forced_as_dict_entry=None,
                        list_nodes_using_name=None):

    list_nodes_forced_as_dict_entry = list_nodes_forced_as_dict_entry or []
    list_nodes_using_name = list_nodes_using_name or []

    if re.match(SUPPORTED_NAMESPACE, root_node.tag):
        return process_node_as_dict(root_node, list_nodes_forced_as_dict_entry, list_nodes_using_name)
    else:
        return None


def process_node_as_dict(node,
                         list_nodes_forced_as_dict_entry,
                         list_nodes_using_name):

    node_dictionary = dict()
    clean_node_tag = clean_key(node.tag)

    if node.items():
        node_dictionary.update(dict(node.items()))
    if clean_node_tag in list_nodes_using_name:
        node_dictionary.pop("name", None)
    text = identify_valid_text_for_node(node)
    if text:
        node_dictionary.update({clean_node_tag: text})

    for child in node:
        data_structure_for_child = determine_container_structure_for_node(child, list_nodes_forced_as_dict_entry)
        child_node_key = determine_key_label_for_node(child, list_nodes_using_name)
        if not child:
            text = identify_valid_text_for_node(child)
            if text:
                node_dictionary.update({child_node_key: text})
        elif data_structure_for_child is dict:
            node_dictionary.update({child_node_key: process_node_as_dict(child, list_nodes_forced_as_dict_entry,
                                                                         list_nodes_using_name)})
        elif data_structure_for_child is list:
            node_dictionary.update({child_node_key: process_node_as_list(child, list_nodes_forced_as_dict_entry,
                                                                         list_nodes_using_name)})

    return node_dictionary


def process_node_as_list(node,
                         list_nodes_forced_as_dict_entry,
                         list_nodes_using_name):

    node_list = list()

    for child in node:
        data_structure_for_child = determine_container_structure_for_node(child, list_nodes_forced_as_dict_entry)
        if data_structure_for_child is None:
            child_dict_contents = process_node_as_dict(child, list_nodes_forced_as_dict_entry,
                                                       list_nodes_using_name)
            if len(child_dict_contents) > 0:
                node_list.append(child_dict_contents)
        elif data_structure_for_child is dict:
            node_list.append(process_node_as_dict(child, list_nodes_forced_as_dict_entry, list_nodes_using_name))
        elif data_structure_for_child is list:
            node_list.append(process_node_as_list(child, list_nodes_forced_as_dict_entry, list_nodes_using_name))

    return node_list


def determine_container_structure_for_node(node, list_nodes_forced_as_dict_entry):

    clean_node_tag = clean_key(node.tag)

    if clean_node_tag in list_nodes_forced_as_dict_entry:
        node_type = dict
    elif len(node) == 1:
        node_type = dict
    elif len(node) > 1:
        if node[0].tag == node[1].tag:
            node_type = list
        else:
            node_type = dict
    else:
        node_type = None

    return node_type


def determine_key_label_for_node(node, list_nodes_using_name):
    clean_node_tag = clean_key(node.tag)
    if clean_node_tag in list_nodes_using_name:
        return dict(node.items())['name']
    else:
        return clean_node_tag


def identify_valid_text_for_node(node):
    if node.text:
        return node.text.strip()


def clean_key(key):
    return key.replace(SUPPORTED_NAMESPACE, '')


def clean_string(input_string,
                 list_tags_to_remove):
    """
    Remove all substrings of text in 'input_string' that start with a certain start tag and end with an end tag.
    We are removing specified patterns in the text where those patterns are known to cause issues.
    Do this cleaning using a non-greedy regex for each start/end tag pair.

    Parameters
    ----------
    input_string: string, the string to be cleaned.
    list_tags_to_remove: list, each of whose elements is a 2-tuple holding the start and end tags to match.

    Returns
    -------
    A string (that has been 'cleaned'; i.e., whose instances of the pattern have been removed).
    """

    for tag_pair in list_tags_to_remove:
        input_string = re.sub('%s.*?%s' % tag_pair, '', input_string)

    return input_string
