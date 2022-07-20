from pathlib import Path
import os
import sys
import glob
import shutil

dir_name = '/home/UNT/sd0570/mmdetection/Experiments and Diagrams/bbox_minus_20_plustop20/Annotations'
# Get list of all files in a given directory sorted by name
list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) ) )
#list_of_files = sorted(filter( os.path.isfile, glob.glob('*.txt')))
#count = 0
d = dict()
for fileName in list_of_files:
    with open(fileName,'r') as f:
        data = f.read()
        occurances = data.count("car")
        occurances1 = data.count("person")
        print("Number of occurance of the word car:", occurances + occurances1, "in file:",fileName)
'''
        for line in f:
            line = line.strip()
            line = line.lower()
            words = line.split(" ")
            for word in words:
                if word in d:
                    d[word]= d[word] + 1
                else:
                    d[word]=1
            #remove the lieading spaces and newline character
        for key in list(d.keys()):

            print(key,":",d[key])
'''




