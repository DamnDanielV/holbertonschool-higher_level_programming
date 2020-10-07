#!/usr/bin/python3
"""module load from json"""
import json


def load_from_json_file(filename):
    with open(filename, mode="r", encoding="utf-8") as f:
        obj = json.loads(f.read())
        f.close()
    return obj
