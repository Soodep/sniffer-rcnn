import itertools
from itertools import groupby
with open('result.txt', 'r') as infile:
    with open('final.txt', 'w') as outfile:
        for line, _ in itertools.groupby(infile):
            outfile.write(line)
