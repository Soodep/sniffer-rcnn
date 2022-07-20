lines_seen = set() # holds lines already seen
outfile = open('test150n.txt', "w")
for line in open('result.txt', "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
