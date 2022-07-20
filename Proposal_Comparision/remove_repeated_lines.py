import itertools
from itertools import groupby
with open('cry.txt', 'r') as infile:
    with open('rcry1.txt', 'w') as outfile:
        for line, _ in itertools.groupby(infile):
            outfile.write(line)
