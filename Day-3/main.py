import argparse
from typing import List
parser = argparse.ArgumentParser()
parser.add_argument('--input-file', default='input.txt')

def run(entries:List[str]) -> int: 
    result = 1
    num_rows = len(entries)
    num_cols = len(entries[0]) #We assume that all the rows have the same number of columns
    i,j = 0,0
    temp_result = 0
    while i < num_rows:
        if entries[i][j] == '#':
            temp_result += 1
        i += 1
        j = (j+3) % num_cols
    result *= temp_result
    return result 


def run2(entries:List[str]) -> int:
    result = 1
    slopes = [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
    ]
    num_rows = len(entries)
    num_cols = len(entries[0]) #We assume that all the rows have the same number of columns
    for slope in slopes:
        i,j = 0,0
        temp_result = 0
        while i < num_rows:
            if entries[i][j] == '#':
                temp_result += 1
            i += slope[1]
            j = (j+slope[0]) % num_cols
        result *= temp_result
    return result 


def load_data(input_file):
    entries = []
    with open(input_file, mode='r') as fs:
        entries = fs.read().splitlines()
    return {'entries': entries}


if __name__ == "__main__":
    args = parser.parse_args()

    input_file = args.input_file
    data = load_data(input_file=input_file)
    print(run(**data))
    print(run2(**data))




