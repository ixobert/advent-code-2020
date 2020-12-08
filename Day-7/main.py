import argparse
from os import remove
from typing import Dict, List, Tuple

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', default='input.txt')

def run(target:Tuple[int, str], entries:Dict[str, Tuple[int, str]]) -> int: 
    def breadth_search(rules:Dict[str, Tuple[int, str]], root:str, target:Tuple[int, str]) -> bool:
        #target = (quantity, color)
        queue = []
        queue.append(root)
        while len(queue) > 0:
            current = queue.pop(-1)
            if rules.get(current, None) == None:
                continue
            for child_quantity, child_color in rules[current]:
                if  child_color == target[1]:
                    return True
                queue.append(child_color)
        return False

    result = 0
    for recipient, children in entries.items():
        if breadth_search(rules=entries, root=recipient, target=target) == True:
            result += 1
    return result 


def run2(target:Tuple[int, str], entries:Dict[str, Tuple[int, str]]) -> int: 
    def detph_search(rules, root):
        if rules.get(root, None) == None:
            return 1
        count = 1
        for factor, color in rules[root]:
            tmp_count = detph_search(rules, color)
            count += tmp_count*factor
        return count 

    result = detph_search(rules=entries, root=target[1])

    return result-1


def load_data(input_file):
    import re
    rules = {}
    with open(input_file, mode='r') as fs:
        entries = fs.read().splitlines()
        for entry in entries:
            recipient,  tokens = entry.split('bags contain')
            recipient = recipient.strip()
            for token in tokens.split(','):
                if 'no' in token: 
                    continue
                for tmp in ['bags.', 'bag.', 'bags', 'bag']:
                    token = token.replace(tmp, '')

                token = token.strip()
                token = token.split(' ')
                quantity, color =  int(token[0]), " ".join(token[1:])

                if  rules.get(recipient, None) == None:
                    rules[recipient] = []
                rules[recipient].append((quantity, color))
    return {'target': (1,'shiny gold'), 'entries': rules}

if __name__ == "__main__":
    args = parser.parse_args()

    input_file = args.input_file
    data = load_data(input_file=input_file)
    print(run(**data))
    print(run2(**data))




