#convert scientific notation into decimal

import fileinput
from glob import glob

for i in glob("*.txt"):
    with fileinput.input(files=i, inplace=True) as f:
        for line in f:
            nums = map(float, line.split())
            print(*nums)
                