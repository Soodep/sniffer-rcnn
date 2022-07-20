'''	
# importing filecmp module
import filecmp
import os

# Path of first directory
dir1 = "/home/UNT/sd0570/mmdetection/Proposal_Comparision/test"

# Path of second directory
dir2 = "/home/UNT/sd0570/mmdetection/Proposal_Comparision/test1"

files1 = os.listdir(dir1)
files2 = os.listdir(dir2)
for x in files2:
	for y in files1:
		if x == y:
			print(x)
'''
from __future__ import division
import os


# Path of first directory
dir1 = "/home/UNT/sd0570/mmdetection/Proposal_Comparision/t2"

# Path of second directory
dir2 = "/home/UNT/sd0570/mmdetection/Proposal_Comparision/t1"

for file in os.listdir(dir1):
    file2 = os.path.join(dir2, file)
    if os.path.exists(file2):
        file1 = os.path.join(dir1, file)
        print(file)
        with open(file1, "r") as f1, open(file2, "r") as f2:
            # how to do the comparison?
            # how to compare first four element of line 1 of f1 with all the first four 
              #element of each line of f2 ?**
            same = True
            while True:
                line1 = f1.readline().split()[:4]
                print(line1)
                line2 = f2.readline().split()[:4]
                print(line2)
                #one way to compare but is not very logical and thorough
                if line1 == line2:
                	same = True
                if len(line1) == 0:
                    break
            if same:
                print("same files")
            else:
                print("files are different")		
	

		

	
