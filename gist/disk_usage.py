#!/usr/bin/python3

import os

show_name = 'pipe'

my_dict = { 
    'publish'   : ['2d/assets', '2d/global', '2d/shots',
                   '3d/assets', '3d/global', '3d/shots',],
    'screening' : [''],
    'stuff'     : [''],
    'works'     : [''],
}


def convert_size(size_bytes): # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
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


for index, key in enumerate(my_dict.keys(), start=1):
    front_path = f'/show/{show_name}/{key}'
    if index == 1:
        for back_path in my_dict[key]:
            full_path = front_path + '/' + back_path
            try:
                raw_result = get_dir_size(full_path)
                print(full_path, ':', convert_size(raw_result))
            except:
                print(full_path,  ':', '\033[31m' + '0 GB' + '\033[0m')
    else:
        full_path = front_path
        try:
            raw_result = get_dir_size(full_path)
            print(full_path, ':', convert_size(raw_result))
        except:
            print(full_path,  ':', '\033[31m' + '0 GB' + '\033[0m')

        
        

        
        
    

    