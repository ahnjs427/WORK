#!/usr/bin/env python

import os

show_name = 'pipe'

publish_2d_list   = ['2d/assets', '2d/global', '2d/shots']
publish_3d_list   = ['3d/assets', '3d/global', '3d/shots']
screening_list    = ['*']
stuff_list        = ['*']
works_list        = ['*']


def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total

def convert_size(size_bytes):
    import math
    if size_bytes == 0:
        return '0B'
    size_name = ('B', 'KB', 'MB', 'GB', 'TB')
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f'{s} {size_name[i]}'

for directory in publish_3d_list:
    pull_path = f'/show/{show_name}/publish/{directory}'
    result = get_dir_size(pull_path)
    if os.path.isdir(pull_path):
        print(f'{show_name}/publish/{directory}', convert_size(result))
    else:
        print('updda')