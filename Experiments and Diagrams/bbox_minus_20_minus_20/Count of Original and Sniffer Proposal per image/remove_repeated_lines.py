lines_seen = set() # holds lines already seen
outfile = open('final_result.txt', "w")
for line in open('only_sniffer_count.txt', "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
