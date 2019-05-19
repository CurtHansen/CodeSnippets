"""
This module features a class that converts XML to JSON.

The entire JSON construct will be an outer dict with inner dicts and lists.
"""

import re

SUPPORTED_NAMESPACE = '{http://www.factset.com/callstreet/xmllayout/v0.1}'


def convert_xml_to_json(root_node, override_info=None):

    if re.match(SUPPORTED_NAMESPACE, root_node.tag):
        return process_tree_node_as_dict(root_node, override_info)
    else:
        return None


def process_tree_node_as_dict(node, override_info):

    result = dict()
    clean_node_tag = clean_key(node.tag)

    if node.items():
        result.update(dict(node.items()))
    if clean_node_tag in override_info:
        result.pop("name", None)
    text = identify_valid_text_for_node(node)
    if text:
        result.update({clean_node_tag: text})

    data_structure_for_children, node_name = determine_structure_for_children(node, override_info)

    for child in node:
        if data_structure_for_child is None:
            text = identify_valid_text_for_node(child)
            if text:
                result.update({clean_child_name: text})
        elif data_structure_for_child is dict:
            result.update({clean_child_name: process_tree_node_as_dict(child, override_info)})
        elif data_structure_for_child is list:
            result.update({clean_child_name: process_tree_node_as_list_element(child, override_info)})

    return result


def process_tree_node_as_list_element(node, override_info):

    result = list()

    for child in node:
        data_structure_for_child, _ = determine_structure_for_children(child, override_info)
        if data_structure_for_child is None:
            child_dict_contents = process_tree_node_as_dict(child, override_info)
            if len(child_dict_contents) > 0:
                result.append(child_dict_contents)
        elif data_structure_for_child is dict:
            result.append(process_tree_node_as_dict(child, override_info))
        elif data_structure_for_child is list:
            result.append(process_tree_node_as_list_element(child, override_info))

    return result


def determine_structure_for_children(node, override_info):

    clean_node_tag = clean_key(node.tag)
    node_type, node_desc = None, None

    if (override_info is not None) and ('force_to_dict' in override_info) and clean_node_tag in override_info['force_to_dict']:
        node_type = dict
    if not node:
        node_desc = clean_node_tag
    elif len(node) == 1 or (len(node) > 1 and node[0].tag != node[1].tag):
        node_type, node_desc = dict, clean_node_tag
    elif (override_info is not None) and ('desc' in override_info) and (clean_node_tag in override_info['desc']):
        node_type dict, dict(node.items())['name']
    else:
        return list, clean_node_tag

    return node_type, node_desc

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
