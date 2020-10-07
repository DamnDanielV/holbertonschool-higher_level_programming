#!/usr/bin/python3
"""module from json to string"""
import json


def from_json_string(my_str):
    """decodes json"""
    return json.loads(my_str)
