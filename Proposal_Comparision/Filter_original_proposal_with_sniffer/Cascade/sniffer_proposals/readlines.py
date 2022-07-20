import os

for i in os.listdir():
    if i.endswith(".txt"):
        with open(i, "r+") as f:
            content = f.readlines()

            f.truncate(0)
            f.seek(0)

            for line in content:
                if not line.startswith("0.00 0.00 0.00 0.00"):
                    f.write(line)
'''		
with open('bbox_003200.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        for line in infile:
            if not line.startswith('0.00 0.00 0.00 0.00'):
                outfile.write(line)

'''

