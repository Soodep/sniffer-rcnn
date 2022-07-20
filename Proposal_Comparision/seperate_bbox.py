file_in = 'removed_similar_lines.txt'

counter = 3199 # counter used ofr the output files

with open(file_in, 'r') as fin:    
    line = fin.readline() # read file in line by line
    while line: # so long as line is not empty,
# if you do have blank lines in your file
# you'd need to do something else
if 'tensor' in line:
    # the very first time there won't be a fout so use try
    # there are other options, like "if count > 0", etc.
    try:
fout.close() # close the old file
    except:
pass
    # augment the counter and open a new file
    counter += 1 
    fout = open('bbox_%06d.txt' % counter, 'w')
fout.write(line) # write the line to the output file bbox_003200 output_001
line = fin.readline() # read the next line of the input file
fout.close() # close the last output file