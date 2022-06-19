# -*- coding: utf-8 -*-

"""
seqlen
~~~~~~~~~~~~~~
This module provides utility functions to parse all the files,
and prints a total sum of all values for `seqlen` field.
"""

#import json
import argparse
import glob
import logging
import sys
import os
import cysimdjson

JSON_FILES = '/**/*.data.json'
LOG_FILE_NAME = 'seqlen.log'
logging.basicConfig(filename=LOG_FILE_NAME, level=logging.ERROR)
logger = logging.getLogger(__name__)

# def get_seqlen_from_json(*, json_obj):
#     """Return the seqlen from a single line of JSON"""
#     try:
#         return json.loads(json_obj)['seqlen']
#     except json.JSONDecodeError:
#         logger.error('Error: JSON object not valid: %s', json_obj)
#         return 0

def get_seqlen_from_json(*, json_obj):
    """Return the seqlen from a single line of JSON
       Access using JSON pointer to avoid loading the entire JSON"""
    try:
        parser = cysimdjson.JSONParser()
        return parser.parse(bytes(json_obj, 'utf-8')).at_pointer("/seqlen")
    except ValueError:
        logger.error('Error: JSON object not valid: %s', json_obj)
        return 0

# def get_total_seqlen_from_file(*, json_file):
#     """Return the sum of seqlen in a single JSON file"""
#     try:
#         with open(json_file, encoding="utf-8") as file:
#             return sum(get_seqlen_from_json(json_obj=_) for _ in file)
#     except FileNotFoundError:
#         logger.error('Error: File not found: %s', json_file)
#         return 0

def get_total_seqlen_from_file(*, json_file):
    """Return the sum of seqlen in a single JSON file"""
    try:
        with open(json_file, encoding='utf-8') as file:
            return sum(get_seqlen_from_json(json_obj=_) for _ in file)
    except FileNotFoundError:
        logger.error('Error: File not found: %s', json_file)
        return 0

def get_file_list(*, json_dir):
    """Return a list of all the files in the input directory
    """
    full_path = json_dir + JSON_FILES
    file_list = glob.glob(full_path, recursive=True)
    if not file_list:
        raise Exception(f'The {json_dir} directory failed to return any file.')
    return file_list


def get_total_seqlen_from_dir(*, input_dir):
    """Return the sum of seqlen of all the JSON file in a given directory
       using serial processing
    """
    try:
        total_seqlen = 0
        file_list = get_file_list(json_dir=input_dir)
        total_seqlen = sum(get_total_seqlen_from_file(json_file=_) for _ in file_list)
        return total_seqlen
    except FileNotFoundError:
        print(f'Error: No file in the directory.: {input_dir}')
        return None
    finally:
        print(f'The sum of the sequence length is {total_seqlen} in the directory {input_dir}.')
        print(f'Please check for errors in {LOG_FILE_NAME}.')

def main():
    """Main program"""
    get_total_seqlen_from_dir(input_dir=args.input_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", help="input directory path", type=str, required=True)
    args = parser.parse_args()
    main()
