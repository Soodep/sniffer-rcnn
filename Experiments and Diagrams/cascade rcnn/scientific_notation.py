import fileinput
from glob import glob


with fileinput.input(files=glob("*.txt"), inplace=True) as f:
    for line in f:
        nums = map(float, line.split())
        print(*nums)
