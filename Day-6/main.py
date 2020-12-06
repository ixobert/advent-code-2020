import argparse
from os import remove
from typing import Dict, List

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', default='input.txt')

def run(entries:List[str]) -> int: 
    result = 0
    for group in entries:
        questions = set([char for char in group if char != ' '])
        result += len(questions)
    return result 


def run2(entries:List[str]) -> int: 
    result = 0
    for group in entries:
        persons_answers = group.split(' ')
        # if len(persons_answers) == 1:
            # continue
        answers_intersections = set([char for char in persons_answers[0]])
        for i in range(1, len(persons_answers)):
            if i == 0 :
                continue
            person_answer = persons_answers[i]
            answers = set([char for char in person_answer])
            answers_intersections = answers_intersections.intersection(answers) 
        result += len(answers_intersections)
    return result 


def load_data(input_file):
    def _group(entries:List[str]) -> List[List[str]]:
        groups = []
        temp = []
        for entry in entries:
            if not entry:
                temp_joined = " ".join(temp)
                groups.append(temp_joined)
                temp = []
            else:
                temp.append(entry)
        temp_joined = " ".join(temp)
        groups.append(temp_joined)
        return groups

    entries = []
    with open(input_file, mode='r') as fs:
        entries = fs.read().splitlines()
    
    groups = _group(entries)

    return {'entries': groups}

if __name__ == "__main__":
    args = parser.parse_args()

    input_file = args.input_file
    data = load_data(input_file=input_file)
    print(run(**data))
    print(run2(**data))




