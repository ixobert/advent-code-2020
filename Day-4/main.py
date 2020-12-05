import argparse
from os import remove
from typing import Dict, List

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', default='input.txt')

def run(entries:List[str]) -> int: 
    result = len(entries)
    mandatory_keys = set(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
    for i, entry in enumerate(entries):
        keys = set(x.split(':')[0] for x in entry.split(' '))
        if 'cid' in keys:
            keys.remove('cid')
        if keys != mandatory_keys:
            result -= 1
    return result 


def run2(entries:List[str]) -> int: #Add arguments types and return type
    result = 0

    import re
    def _to_int(x) -> int:
        try:
            return int(x)
        except ValueError:
            return -1
    def _check_size(x:str) -> bool:
        value = _to_int(x[0:-2])
        if x.endswith('cm'):
            return value >= 150 and value <= 193
        elif x.endswith('in'):
            return value >= 59 and value <= 76
        else :
            return False

    result = len(entries)
    rules = {
        'byr': lambda x: bool(re.match('^[0-9]{4}$', x)) and _to_int(x) >= 1920 and _to_int(x) <= 2002,
        'iyr': lambda x: bool(re.match('^[0-9]{4}$', x)) and _to_int(x) >= 2010 and _to_int(x) <= 2020,
        'eyr': lambda x: bool(re.match('^[0-9]{4}$', x)) and _to_int(x) >= 2020 and _to_int(x) <= 2030,
        'hgt': lambda x: bool(re.match('^[0-9]*(in|cm$)', x)) and _check_size(x),
        'hcl': lambda x: bool(re.match('^#([0-9a-f]){6}$', x)),
        'ecl': lambda x: bool(re.match('(^amb$)|(^blu$)|(^brn$)|(^gry$)|(^grn$)|(^hzl$)|(^oth$)', x)),
        'pid': lambda x: bool(re.match('^[0-9]{9}$', x))
    }

    mandatory_keys = set(list(rules.keys()))
    for i, entry in enumerate(entries):
        fields = {x.split(':')[0]:x.split(':')[1].strip() for x in entry.split(' ')}
        if 'cid' in fields:
            fields.pop('cid')
        keys = set(list(fields.keys()))
        if 'cid' in keys:
            keys.remove('cid')
        #First check: Validate all the keys
        if keys != mandatory_keys:
            result -= 1
            continue
        #Second check: Validate all the values
        checks = [rules[key](value) for key, value in fields.items()]
        if False in checks:
            result -= 1
    return result 

def load_data(input_file):
    def _group(entries:List[str]) -> List[List[str]]:
        passports = []
        temp = []
        for entry in entries:
            if not entry:
                temp_joined = " ".join(temp)
                passports.append(temp_joined)
                temp = []
            else:
                temp.append(entry)
        temp_joined = " ".join(temp)
        passports.append(temp_joined)
        return passports

    entries = []
    with open(input_file, mode='r') as fs:
        entries = fs.read().splitlines()
    
    passports = _group(entries)

    return {'entries': passports}


if __name__ == "__main__":
    args = parser.parse_args()

    input_file = args.input_file
    data = load_data(input_file=input_file)
    print(run(**data))
    print(run2(**data))




