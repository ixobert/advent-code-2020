import argparse
from os import remove, stat
from typing import Dict, List, Tuple

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', default='input.txt')


def run(entries:List[str], preamble_size:int) -> int: 
    def helper(entries_:List[str], target:int) -> bool:
        for i, value in enumerate(entries_):
            if target - value in entries_:
                if target -value != value:
                    return True
        return False
    
    result = 0
    for i in range(preamble_size, len(entries)):
        start = max(0, i - preamble_size)
        end = start + preamble_size
        check_pair = helper(entries_=entries[start:end], target=entries[i])
        if check_pair is False:
            result = entries[i]
            break
    return result 


def run2(entries:List[str], preamble_size:int) -> int: 
    def helper(entries_:List[str], target:int) -> bool:
        for i, value in enumerate(entries_):
            if target - value in entries_:
                if target -value != value:
                    return True
        return False
    
    def find_bad_number(entries:List[str], preamble_size:int):
        for i in range(preamble_size, len(entries)):
            start = max(0, i - preamble_size)
            end = start + preamble_size
            check_pair = helper(entries_=entries[start:end], target=entries[i])
            if check_pair is False:
               return entries[i]
        return result 

    result = 0
    bad_number = find_bad_number(entries=entries, preamble_size=preamble_size)

    for i in range(len(entries)):
        for j in range(i, len(entries)):
            current_sum = sum(entries[i:j])
            if current_sum == bad_number:
                return entries[i] + entries[j-2]
    return result
  
  

def load_data(input_file):
    entries = []
    with open(input_file, mode='r') as fs:
        entries = [int(x) for x in fs.read().splitlines()]
    preamble_size = 25
    return {'entries': entries, 'preamble_size':preamble_size}

if __name__ == "__main__":
    args = parser.parse_args()

    input_file = args.input_file
    data = load_data(input_file=input_file)
    print(run(**data))
    print(run2(**data))




