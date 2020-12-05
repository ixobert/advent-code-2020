import argparse
from os import remove
from typing import Dict, List

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', default='input.txt')

def run(entries:List[str]) -> int: 
    result = -1
    for entry in entries:
        row,col = 0, 0 

        start, end = 0, 127
        for i in range(7-1): 
            if entry[i] == 'F':
                end = (end + start) // 2
            elif entry[i] == 'B':
                start = (end+start+1) // 2
            pass
        if entry[6] == 'F':
            row = start
        elif entry[6] == 'B':
            row = end

        start, end = 0, 7
        for i in range(7, 7+3):
            if entry[i] == 'L':
                end = (start + end) // 2
            elif entry[i] == 'R':
                start = (start+1 + end) // 2
        if entry[-1] == 'L':
            col = start
        elif entry[-1] == 'R':
            col = end

        seat = row * 8 + col
        if seat > result:
            result = seat
    return result 


def run2(entries:List[str]) -> int: 
    result = -1
    seats = []
    for entry in entries:
        row,col = 0, 0 

        start, end = 0, 127
        for i in range(7-1): 
            if entry[i] == 'F':
                end = (end + start) // 2
            elif entry[i] == 'B':
                start = (end+start+1) // 2
            pass
        if entry[6] == 'F':
            row = start
        elif entry[6] == 'B':
            row = end

        start, end = 0, 7
        for i in range(7, 7+3):
            if entry[i] == 'L':
                end = (start + end) // 2
            elif entry[i] == 'R':
                start = (start+1 + end) // 2
        if entry[-1] == 'L':
            col = start
        elif entry[-1] == 'R':
            col = end

        seat = row * 8 + col
        seats.append(seat)
    seats = sorted(seats)
    for i in range(1,len(seats)):
        if seats[i] - seats[i-1] == 2:
            result = seats[i]-1
            break
    return result 


def load_data(input_file):
    entries = []
    with open(input_file, 'r') as reader:
        entries = reader.read().splitlines()
    return {'entries': entries}


if __name__ == "__main__":
    args = parser.parse_args()

    input_file = args.input_file
    data = load_data(input_file=input_file)
    print(run(**data))
    print(run2(**data))




