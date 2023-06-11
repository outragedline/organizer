#!/bin/python

import os
import sys
import math

def separate(entrys, path, c=0):
    c+=1
    num_entrys = len(entrys)
    sliced_entrys = []
    if num_entrys == 0:
        return
    
    while len(sliced_entrys) <= 30 and len(entrys) > 0:
        sliced_entrys.append(entrys.pop(0))

    sub_dir_path = os.path.join(path, f"package{c}")
    os.mkdir(sub_dir_path)

    for entry in sliced_entrys:
        entry_path = os.path.join(path, entry)
        new_entry_path = os.path.join(sub_dir_path, entry)
        os.rename(entry_path, new_entry_path)
    separate(entrys,c)
    
    
        
def organize(path):
    entrys = []
    for entry in os.scandir(path):
        entry_path = os.path.join(path, entry.name)
        if os.path.isdir(entry_path):
            organize(entry_path)
        else:
            entrys.append(entry.name)
    separate(entrys, path)
            
        

root_dir_path = sys.argv[1]

if not os.path.isdir(root_dir_path):
    print("Directory doesn't exist")
    sys.exit(1)

organize(root_dir_path)
