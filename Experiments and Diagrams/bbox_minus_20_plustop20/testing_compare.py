from pathlib import Path

#check for the matching file, file with the same name in each directory
def get_matching_file(known_file, search_dir):
    f2_file = search_dir.joinpath(known_file.name)
    if f2_file.exists():
        print(known_file.name)
        return f2_file
    raise FileNotFoundError

#split each lines of each file
def get_lines(file_loc):
    result = []
    lines = file_loc.read_text().splitlines()
    for row in lines:
        row_as = []
        for num in row.split()[:4]:
            row_as.append(float(num))
        result.append(row_as)
    #print("This is the len result:",len(result))
    return result

#split each lines of each file
def get_lines1(file_loc):
    result2 = []
    lines = file_loc.read_text().splitlines()
    for row in lines:
        row_as = []
        for num in row.split()[:4]:
            row_as.append(float(num))
        result2.append(row_as)
    #print("This is the len result:",len(result))
    return result2

#compare each line of each file with each line of another file
def compare_content(f1_rows, f2_rows):
    result1 = []
    for row1 in f1_rows:
        for row2 in f2_rows:
            row_result = []
            for v1, v2 in zip(row1, row2):
                # print(f'{v2} - {v1} = {v2 - v1}')
                row_result.append(abs(v2 - v1) <= 20)
            if all(row_result):
                result1.append(row2)
    #print("Total Sniffer Proposals:", len(result1))            #print("This is the len result for row2:", len(result))
    return result1
'''
def compare_content1(f1_rows):
    result1 = []
    for row1 in f1_rows:
        #print("this is row1[4]", row1[4])
        if row1[4] > 0.8:
            result1.append(row1[0:4])
    #print("Total Original Proposals:", len(result1))
    return result1
'''
#display the result based on comparision
def print_result(result):
    for line in result:
        print(' '.join(str(float(num)) for num in line))


def main(dir1, dir2):
    for file_one in dir1.glob('*.txt'):
        file_two = get_matching_file(file_one, dir2)
        f1_content = get_lines(file_one)
        f2_content = get_lines(file_two)
        result = compare_content(f1_content, f2_content)
        #f1_content1 = get_lines1(file_one)
        #result1 = compare_content1(f1_content1)
        print_result(result)
        #print_result(result1)



if __name__ == '__main__':
    main(dir1=Path(r'/home/UNT/sd0570/mmdetection/Experiments and Diagrams/bbox_minus_20_plustop20/original'),
         dir2=Path(r'/home/UNT/sd0570/mmdetection/Experiments and Diagrams/bbox_minus_20_plustop20/sniffer'))