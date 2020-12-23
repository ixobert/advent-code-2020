import argparse
from os import remove, stat
from typing import Dict, List, Tuple

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', default='input.txt')


def run(entries:List[int]) -> int: 
    result = 0
    entries = sorted(entries)
    entries.insert(0, 0)
    entries.append(entries[-1] + 3)
    diff_occurences = {value:0 for value in range(1, 4)}
    for i in range(1, len(entries)):
        diff = entries[i] - entries[i-1]
        if diff <= 3:
            diff_occurences[diff] += 1
    result = diff_occurences[1] * diff_occurences[3]
    return result 


def run2(entries:List[int]) -> int: 
    cache = {}
    def helper(elems:List[int], idx) -> int:
        if idx == len(elems)-1:
            return 1
        if idx in cache:
            return cache[idx]
        sum_ = 0
        for i in range(1,4):
            if i + idx >= len(elems): continue
            if elems[idx+i] - elems[idx] <= 3:
                sum_ += helper(elems=elems, idx=idx+i)
            else: 
                break
        cache[idx] = sum_
        return sum_

    entries = sorted(entries)
    entries.insert(0, 0)
    entries.append(entries[-1] + 3)
    result = helper(entries, 0)

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




