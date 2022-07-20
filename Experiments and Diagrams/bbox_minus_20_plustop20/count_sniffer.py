from pathlib import Path
import os
import sys
import glob
import shutil

dir_name = '/home/UNT/sd0570/mmdetection/Experiments and Diagrams/bbox_minus_20_plustop20/sniffer'
# Get list of all files in a given directory sorted by name
list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) ) )
#list_of_files = sorted(filter( os.path.isfile, glob.glob('*.txt')))
#count = 0
for fileName in list_of_files:
    with open(fileName,'r') as f:
        x = len(f.readlines())
        #print(fileName)
        print(x)




