file_in = 'final.txt'

fout = None

with open(file_in, 'r') as fin:    
    line = fin.readline() # read file in line by line
    while line: 
        if 'bbox' in line:
            try:
                if fout is not None:
                    fout.close() # close the old file
            except:
                pass

            fout = open(line.strip(), 'w')
            print('New file created', line.strip())
        else:
            fout.write(line) # write the line to the output file
        
        line = fin.readline() # read the next line of the input file

fout.close() # close the last output file
