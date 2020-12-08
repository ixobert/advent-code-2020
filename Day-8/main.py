import argparse
from os import remove
from typing import Dict, List, Tuple

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', default='input.txt')


def run(entries:List[str]) -> int: 
    entries = [[entry, 0] for entry in entries]
    result = 0
    i = 0 
    while i < len(entries):
        if entries[i][1] == 1: 
            return result

        entries[i][1] = 1
        instruction, value = entries[i][0].split(' ')
        value = int(value)
        if instruction == 'nop': 
            i += 1
            continue

        if instruction == 'jmp':
            i += value
            continue

        if instruction == 'acc':
            result += value
            i+=1

    return result 


def run2(entries:List[str]) -> int: 
    def helper(entries_temp):
        entries_temp = [[entry, 0] for entry in entries_temp]
        result = 0
        i = 0 
        while i < len(entries_temp):
            if entries_temp[i][1] == 1: 
               break

            entries_temp[i][1] = 1
            instruction, value = entries_temp[i][0].split(' ')
            value = int(value)
            if instruction == 'nop': 
                i += 1
                continue

            if instruction == 'jmp':
                i += value
                continue

            if instruction == 'acc':
                result += value
                i+=1

        if i >= len(entries_temp):
            return True, result
        else: 
            return False, result


    result = [False, 0]
    for i, entry in enumerate(entries):
        instruction, value = entry.split(' ')
        if instruction in ['jmp', 'nop']:
            if instruction == 'jmp':
                old_value, new_value = 'jmp', 'nop'
            else:
                old_value, new_value = 'nop', 'jmp'
            entries[i] = entry.replace(old_value, new_value)
            result = helper(entries)

            if result[0] == True:
                return result[1]
            else:
                entries[i] = entry.replace(new_value, old_value)

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




