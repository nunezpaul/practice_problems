class Cell(object):
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'C{val}'.format(val=self.val)

    def __init__(self, val):
        self.val = val


def convert_curr_row(row):
    new_row = []
    for idx, num in enumerate(row):
        if idx == 0:
            prev_cell = Cell(num)
            count = 0
            continue

        new_row.append(prev_cell)
        count += 1

        if num != prev_cell.val:
            prev_cell.val *= count
            prev_cell = Cell(num)
            count = 0

    if num == prev_cell.val:
        new_row.append(prev_cell)
        prev_cell.val *= (count + 1)
    else:
        new_row.append(Cell(num))

    return new_row


def add_rows(prev_row, curr_row):
    max_num = 0
    for (prev_cell, curr_cell) in zip(prev_row, curr_row):
        if prev_cell.val > 0 and curr_cell.val > 0:
            curr_cell.val += prev_cell.val
            prev_cell.val = 0
            max_num = max(max_num, curr_cell.val)

    return max_num


def find_largest_island(grid):
    converted_grid = [convert_curr_row(row) for row in grid]

    for idx, row in enumerate(converted_grid):
        if idx == 0:
            prev_row = row
            max_num = 0
            continue
        row_max_num = add_rows(prev_row, row)
        max_num = max(max_num, row_max_num)
        prev_row = row

    return max_num


if __name__ == '__main__':
    grid = [
        [1, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 1]
    ]


    assert find_largest_island(grid) == 10


    grid = [
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1]
    ]

    assert find_largest_island(grid) == 12
