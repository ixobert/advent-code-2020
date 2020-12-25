import argparse
import copy
from typing import Dict, List, Tuple

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', default='input.txt')


def run(entries: List[str]) -> int:
    def run_round(entries: List[str]) -> List[str]:
        new_entries = copy.deepcopy(entries)
        num_rows = len(entries)
        # We assume that all rows as the same columns lenght.
        num_cols = len(entries[0])
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                if entries[row_idx][col_idx] == '.':
                    continue

                up = row_idx-1 if row_idx-1 >= 0 else None
                down = row_idx+1 if row_idx+1 < num_rows else None
                left = col_idx-1 if col_idx-1 >= 0 else None
                right = col_idx+1 if col_idx+1 < num_cols else None

                neighbors = []
                if up != None:
                    neighbors.append(entries[up][col_idx])
                if down != None:
                    neighbors.append(entries[down][col_idx])
                if left != None:
                    neighbors.append(entries[row_idx][left])
                if right != None:
                    neighbors.append(entries[row_idx][right])
                if up != None and left != None:
                    neighbors.append(entries[up][left])
                if down != None and left != None:
                    neighbors.append(entries[down][left])
                if up != None and right != None:
                    neighbors.append(entries[up][right])
                if down != None and right != None:
                    neighbors.append(entries[down][right])

                occupied_neighbors = 0
                for occ in neighbors:
                    if occ == '#':
                        occupied_neighbors += 1

                if entries[row_idx][col_idx] == 'L' and occupied_neighbors == 0:
                    new_entries[row_idx][col_idx] = '#'

                if entries[row_idx][col_idx] == '#' and occupied_neighbors >= 4:
                    new_entries[row_idx][col_idx] = 'L'

        return new_entries

    def count_empty_seat(entries: List[str]) -> int:
        num_rows = len(entries)
        # We assume that all rows as the same columns length.
        num_cols = len(entries[0])
        occupied_seats = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if entries[i][j] == '#':
                    occupied_seats += 1
        return occupied_seats

    def identic_state(entriesA, entriesB):
        num_rows = len(entriesA)
        # We assume that all rows as the same columns length.
        num_cols = len(entriesA[0])
        for i in range(num_rows):
            for j in range(num_cols):
                if entriesA[i][j] != entriesB[i][j]:
                    return False
        return True

    def print_matrix(entries, title):
        out = [''.join(x) for x in entries]
        out = '\n'.join(out)
        print(f"{title}\n{out}")
        print()

    result = 0
    previous_state = copy.deepcopy(entries)
    current_state = copy.deepcopy(entries)
    # print_matrix(current_state, 'Initial')
    round_ = 0
    while True:
        round_ += 1
        current_state = run_round(current_state)
        occupied_seats = count_empty_seat(current_state)
        # print_matrix(current_state, 'Current')

        if identic_state(current_state, previous_state):
            break
        previous_state = copy.deepcopy(current_state)

    result = occupied_seats
    return result


def run2(entries: List[str]) -> int:

    def find_vertical(entries, curr_row, curr_col, orientation):
        curr_row += orientation
        while True:
            curr_row = curr_row if curr_row>=0 and curr_row<len(entries) else None
            if curr_row == None or entries[curr_row][curr_col] != '.':
                return curr_row
            curr_row += orientation
        return curr_row

    def find_horizontal(entries, curr_row, curr_col, orientation):
        curr_col += orientation
        while True:
            curr_col = curr_col if curr_col>=0 and curr_col<len(entries[0]) else None
            if curr_col == None or entries[curr_row][curr_col] != '.':
                break
            curr_col += orientation
        return curr_col

    def find_up_left(entries, curr_row, curr_col):
        curr_row -= 1
        curr_col -= 1
        while True:
            curr_row = curr_row if curr_row>=0 and curr_row<len(entries) else None
            curr_col = curr_col if curr_col>=0 and curr_col<len(entries[0]) else None
            if  None in [curr_row, curr_col] or entries[curr_row][curr_col] != '.':
                break
            curr_row -= 1
            curr_col -= 1
        return [curr_row, curr_col]

    def find_up_right(entries, curr_row, curr_col):
        curr_row -= 1
        curr_col += 1
        while True:
            curr_row = curr_row if curr_row>=0 and curr_row<len(entries) else None
            curr_col = curr_col if curr_col>=0 and curr_col<len(entries[0]) else None
            if  None in [curr_row, curr_col] or entries[curr_row][curr_col] != '.':
                break
            curr_row -= 1
            curr_col += 1
        return [curr_row, curr_col]

    def find_down_left(entries, curr_row, curr_col):
        curr_row += 1
        curr_col -= 1
        while True:
            curr_row = curr_row if curr_row>=0 and curr_row<len(entries) else None
            curr_col = curr_col if curr_col>=0 and curr_col<len(entries[0]) else None
            if  None in [curr_row, curr_col] or entries[curr_row][curr_col] != '.':
                break
            curr_row += 1
            curr_col -= 1
        return [curr_row, curr_col]


    def find_down_right(entries, curr_row, curr_col):
        curr_row += 1
        curr_col += 1
        while True:
            curr_row = curr_row if curr_row>=0 and curr_row<len(entries) else None
            curr_col = curr_col if curr_col>=0 and curr_col<len(entries[0]) else None
            if  None in [curr_row, curr_col] or entries[curr_row][curr_col] != '.':
                break
            curr_row += 1
            curr_col += 1
        return [curr_row, curr_col]

    def run_round(entries: List[str]) -> List[str]:
        new_entries = copy.deepcopy(entries)
        num_rows = len(entries)
        # We assume that all rows as the same columns lenght.
        num_cols = len(entries[0])
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                if entries[row_idx][col_idx] == '.':
                    continue
                # Up
                up = find_vertical(entries, row_idx, col_idx, -1)
                down = find_vertical(entries, row_idx, col_idx, +1)
                left = find_horizontal(entries, row_idx, col_idx, -1)
                right = find_horizontal(entries, row_idx, col_idx, +1)
                up_left = find_up_left(entries, row_idx, col_idx)
                up_right = find_up_right(entries, row_idx, col_idx)
                down_left = find_down_left(entries, row_idx, col_idx)
                down_right = find_down_right(entries, row_idx, col_idx)

                neighbors = []
                if up != None:
                    neighbors.append(entries[up][col_idx])
                if down != None:
                    neighbors.append(entries[down][col_idx])
                if left != None:
                    neighbors.append(entries[row_idx][left])
                if right != None:
                    neighbors.append(entries[row_idx][right])

                for diag in [up_left, up_right, down_left, down_right]:
                    if None not in diag:
                        neighbors.append(entries[diag[0]][diag[1]])

                occupied_neighbors = 0
                for occ in neighbors:
                    if occ == '#':
                        occupied_neighbors += 1

                if entries[row_idx][col_idx] == 'L' and occupied_neighbors == 0:
                    new_entries[row_idx][col_idx] = '#'

                if entries[row_idx][col_idx] == '#' and occupied_neighbors >= 5:
                    new_entries[row_idx][col_idx] = 'L'

        return new_entries

    def count_empty_seat(entries: List[str]) -> int:
        num_rows = len(entries)
        # We assume that all rows as the same columns length.
        num_cols = len(entries[0])
        occupied_seats = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if entries[i][j] == '#':
                    occupied_seats += 1
        return occupied_seats

    def identic_state(entriesA, entriesB):
        num_rows = len(entriesA)
        # We assume that all rows as the same columns length.
        num_cols = len(entriesA[0])
        for i in range(num_rows):
            for j in range(num_cols):
                if entriesA[i][j] != entriesB[i][j]:
                    return False
        return True

    def print_matrix(entries, title):
        out = [''.join(x) for x in entries]
        out = '\n'.join(out)
        print(f"{title}\n{out}")
        print()

    result = 0
    previous_state = copy.deepcopy(entries)
    current_state = copy.deepcopy(entries)
    round_ = 0
    while True:
        round_ += 1
        current_state = run_round(current_state)
        occupied_seats = count_empty_seat(current_state)

        if identic_state(current_state, previous_state):
            break
        previous_state = copy.deepcopy(current_state)

    result = occupied_seats
    return result


def load_data(input_file):
    entries = []
    with open(input_file, mode='r') as fs:
        entries = [list(x) for x in fs.read().splitlines()]
    return {'entries': entries}


if __name__ == "__main__":
    args = parser.parse_args()

    input_file = args.input_file
    data = load_data(input_file=input_file)
    print(run(**data))
    print(run2(**data))
