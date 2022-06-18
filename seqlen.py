# -*- coding: utf-8 -*-

"""
seqlen
~~~~~~~~~~~~~~
This module provides utility functions to parse all the files,
and prints a total sum of all values for `seqlen` field.
"""

import json
import glob
import logging

JSON_FILES = '/**/*.data.json'
LOG_FILE_NAME = (__name__) + '.log'
logging.basicConfig(filename=LOG_FILE_NAME, encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)

def get_seqlen_from_json(*, json_obj):
    """Return the seqlen from a single line of JSON"""
    try:
        return json.loads(json_obj)['seqlen']
    except json.JSONDecodeError:
        logger.error('Error: JSON object not valid: %s', json_obj)
        return 0

def get_total_seqlen_from_file(*, json_file):
    """Return the sum of seqlen in a single JSON file"""
    try:
        with open(json_file, encoding="utf-8") as file:
            return sum(get_seqlen_from_json(json_obj=_) for _ in file) 
    except FileNotFoundError:
        logger.error('Error: File not found: %s', json_file)
        return 0

def get_total_seqlen_from_dir(*, json_dir):  
    """Return the sum of seqlen of all the JSON file in a given directory"""
    try:
        full_path = json_dir + JSON_FILES
        total_seqlen = sum(get_total_seqlen_from_file(json_file=_) for _ in glob.glob(full_path, recursive=True))
        return total_seqlen
    except FileNotFoundError:
        print(f'Error: No file in the directory.: {json_dir}')
    finally:
        print(f'The sum of the sequence length is {total_seqlen} in the directory {json_dir}.')
        print(f'Please check for errors in {LOG_FILE_NAME}.')
