import os

for i in os.listdir():
    if i.endswith(".txt"):
        with open(i, "r+") as f:
            content = f.readlines()

            f.truncate(0)
            f.seek(0)

            for line in content:
                if not line.startswith("tensor"):
                    f.write(line)
