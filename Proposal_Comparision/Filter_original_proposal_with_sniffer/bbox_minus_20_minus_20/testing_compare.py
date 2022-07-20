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
    return result

#compare each line of each file with each line of another file
def compare_content(f1_rows, f2_rows):
    result = []
    for row1 in f1_rows:
        for row2 in f2_rows:
            row_result = []
            for v1, v2 in zip(row1, row2):
                # print(f'{v2} - {v1} = {v2 - v1}')
                row_result.append(abs(v2 - v1) <= 30)
            if all(row_result):
                result.append(row2)
    return result
def compare_content1(f2_rows, f1_rows):
    result1 = []
    for row2 in f2_rows:
        for row1 in f1_rows:
            row_result1 = []
            for v1, v2 in zip(row2, row1):
                # print(f'{v2} - {v1} = {v2 - v1}')
                row_result1.append(abs(v2 - v1) <= 30)
            if all(row_result1):
                result1.append(row1)
    return result1
#def compare_content1(f2_rows):
    #result1 = []
    #for row2 in f2_rows:
        #result1.append(row2[0:4])
    #return result1
#display the result based on comparision
def print_result(result):
    for line in result:
        print(' '.join(str(float(num)) for num in line))


def main(dir1, dir2):
    for file_one in dir1.glob('*.txt'):
        file_two = get_matching_file(file_one, dir2)
        f1_content = get_lines(file_one)
        #print(f1_content)
        f2_content = get_lines(file_two)
        result = compare_content(f1_content, f2_content)
        result1 = compare_content1(f2_content, f1_content)
        print_result(result)
        print_result(result1)



if __name__ == '__main__':
    main(dir1=Path(r'/home/UNT/sd0570/mmdetection/Proposal_Comparision/Filter_original_proposal_with_sniffer/Final_Test/original'),
         dir2=Path(r'/home/UNT/sd0570/mmdetection/Proposal_Comparision/Filter_original_proposal_with_sniffer/Final_Test/sniffer'))