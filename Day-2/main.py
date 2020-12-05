import argparse
from typing import List
parser = argparse.ArgumentParser()
parser.add_argument('--input-file', default='input.txt')

def run(entries:List[str]) -> int: 
    result = len(entries)
    for minimum, maximum, character, word in entries:
        character_count = word.count(character)
        if character_count < minimum or character_count > maximum:
            result -= 1
    return result 

def run2(entries:List[str]) -> int: 
    result = 0
    for minimum, maximum, character, word in entries:
        if character in [word[minimum-1], word[maximum-1]] and word[minimum-1] != word[maximum-1] :
            result += 1
    return result 

def load_data(input_file):
    def _parse_row(entry):
        import re
        parsed = re.split('[-:\ ]', entry)
        minimum = int(parsed[0]) 
        maximum = int(parsed[1])
        character = parsed[2]
        word = parsed[4]
        return minimum, maximum, character, word

    entries = []
    with open(input_file, mode='r') as fs:
        entries = fs.read().splitlines()
        entries = list(map(_parse_row, entries))
    return {'entries': entries}


if __name__ == "__main__":
    args = parser.parse_args()

    input_file = args.input_file
    data = load_data(input_file=input_file)
    print(run(**data))
    print(run2(**data))




