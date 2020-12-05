from typing import List


def run(target:int, entries:List[int]) -> int:
    entries = sorted(entries)
    start, end = 0, len(entries)-1
    while start != end:
        current_sum = entries[start] + entries[end]
        if current_sum > target:
            end -= 1
        elif current_sum < target:
            start += 1
        else:
            print(entries[start], entries[end])
            return entries[start] * entries[end]


def run2(target:int, entries:List[int]) -> int:
    for i in range(len(entries)):
        for j in range(i, len(entries)):
            for k in range(j, len(entries)):
                if entries[i] + entries[j] + entries[k] == target:
                    return  entries[i] * entries[j] * entries[k] 



if __name__ == "__main__":
    pass
    input_file = "input.txt"

    entries = []
    with open(input_file, mode='r') as fs:
        entries = fs.read().splitlines()
        entries = [int(entry) for entry in entries]

    result = run(target=2020, entries=entries)
    print("Part 1:", result)
    result = run2(target=2020, entries=entries)
    print("Part 2:", result)



