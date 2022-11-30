#!/usr/bin/python3

import os
from pprint import pprint

show_name = 'pipe'

my_dict = { 
    'publish': ['2d/assets', '2d/global', '2d/shots'],
    'publish': ['3d/assets', '3d/global', '3d/shots'],   
    'screening' : ['*'],
    'stuff'     : ['*'],
    'wors'      : ['*'],
}


def convert_size(size_bytes):
    import math
    if size_bytes == 0:
        return '0B'
    size_name = ('B', 'KB', 'MB', 'GB', 'TB')
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f'{s} {size_name[i]}'

def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


for directory in my_dict.keys():
    pull_path = f'/show/{show_name}/publish/{directory}'
    result = get_dir_size(pull_path)
    print(result)

# for k, v in my_dict.items():
#     print(f'key: {k}, value: {v}')

# for i in my_dict.keys():
#     print(i)

    