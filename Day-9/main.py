import argparse
from os import remove, stat
from typing import Dict, List, Tuple

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', default='input.txt')


def run(entries:List[str]) -> int: 
    def helper(entries_:List[str], target:int) -> bool:
        for i, value in enumerate(entries_):
            if target - value in entries_:
                if target -value != value:
                    return True
        return False
    
    result = 0
    k = 5
    for i in range(k, len(entries)):
        start = max(0, i - k)
        end = start + k
        check_pair = helper(entries_=entries[start:end], target=entries[i])
        if check_pair is False:
            result = entries[i]
            break
    return result 


def run2(entries:List[str]) -> int: 
    def helper(entries_:List[str], target:int) -> bool:
        for i, value in enumerate(entries_):
            if target - value in entries_:
                if target -value != value:
                    return True
        return False
    
    def find_bad_number(entries:List[str]):
        k = 25
        for i in range(k, len(entries)):
            start = max(0, i - k)
            end = start + k
            check_pair = helper(entries_=entries[start:end], target=entries[i])
            if check_pair is False:
               return entries[i]
        return result 

    result = 0
    bad_number = find_bad_number(entries=entries)

    for i in range(len(entries)):
        for j in range(i, len(entries)):
            current_sum = sum(entries[i:j])
            if current_sum == bad_number:
                print(entries[i], entries[j-1], bad_number)
                return entries[i] + entries[j-2]
    return result
  
  

def load_data(input_file):
    entries = []
    with open(input_file, mode='r') as fs:
        entries = [int(x) for x in fs.read().splitlines()]
    return {'entries': entries}

if __name__ == "__main__":
    args = parser.parse_args()

    input_file = args.input_file
    data = load_data(input_file=input_file)
    print(run(**data))
    print(run2(**data))




