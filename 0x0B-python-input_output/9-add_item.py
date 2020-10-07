#!/usr/bin/python3
"""module add item"""
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


def add_item():
    """add args to a file"""
    try:
        lista = load_from_json_file('./add_item.json')
    except:
        lista = []
    for i in range(1, len(sys.argv)):
        lista.append(sys.argv[i])
    save_to_json_file(lista, './add_item.json')


if __name__ == "__main__":
    add_item()
