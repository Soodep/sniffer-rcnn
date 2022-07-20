from pathlib import Path


def get_matching_file(known_file, search_dir):
    f2_file = search_dir.joinpath(known_file.name)
    if f2_file.exists():
        print(known_file.name)
        return f2_file
    raise FileNotFoundError


def get_lines(file_loc):
    result = []
    lines = file_loc.read_text().splitlines()
    for row in lines:
        row_as = []
        for num in row.split()[:4]:
            row_as.append(float(num))
        result.append(row_as)
    return result


def compare_content(f1_rows, f2_rows):
    result = []
    for row1 in f1_rows:
        for row2 in f2_rows:
            row_result = []
            for v1, v2 in zip(row1, row2):
                # print(f'{v2} - {v1} = {v2 - v1}')
                try:
                    row_result.append(0.90 < abs(v2 / v1) < 1.05)
                except ZeroDivisionError:
                    z=0
            if all(row_result):
                result.append(row1)
                #result.append(row2)
    return result


def print_result(result):
    for line in result:
        print(' '.join(str(float(num)) for num in line))


def main(dir1, dir2):
    for file_one in dir1.glob('*.txt'):
        file_two = get_matching_file(file_one, dir2)
        f1_content = get_lines(file_one)
        f2_content = get_lines(file_two)
        result = compare_content(f1_content, f2_content)
        print_result(result)


if __name__ == '__main__':
    main(dir1=Path(r'/home/UNT/sd0570/mmdetection/Proposal_Comparision/2dbox and annotation comparision/test1'),
         dir2=Path(r'/home/UNT/sd0570/mmdetection/Proposal_Comparision/2dbox and annotation comparision/test'))
