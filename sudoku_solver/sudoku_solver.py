import math
import collections


class Cell(object):
    def __repr__(self):
        return 'C{val}'.format(val=self.val)

    def __str__(self):
        return self.__repr__()

    def __init__(self, board, val, x, y):
        self.val = val
        self.change = False
        self.x = x
        self.y = y
        self.missing_row_nums = board.missing_row_nums[self.y]
        self.missing_col_nums = board.missing_col_nums[self.x]
        self.missing_square_nums = board.missing_square_nums[board._determine_square_num(self.x, self.y)]
        self.valid_nums = None

    def get_valid_nums(self):
        return self.missing_square_nums.intersection(self.missing_row_nums, self.missing_col_nums)

    def has_singleton_solution(self):
        self.valid_nums = self.get_valid_nums()
        return len(self.valid_nums) == 1

    def update_val_with_singleton(self):
        if len(self.valid_nums) == 1:
            self.val = self.valid_nums.pop()
            self._remove_possibility(self.val)

    def _remove_possibility(self, only_valid_num):
        for category in (self.missing_row_nums, self.missing_col_nums, self.missing_square_nums):
            category.remove(only_valid_num)

    def _reinsert_possibility(self, valid_num):
        for category in (self.missing_row_nums, self.missing_col_nums, self.missing_square_nums):
            category.add(valid_num)


class Board(object):
    def __init__(self, board):
        self.board = board
        self.height = len(board)
        self.width = len(board[0])
        self.missing_row_nums = self._get_missing_row_nums()
        self.missing_col_nums = self._get_missing_col_nums()
        self.missing_square_nums = self._get_missing_square_nums()
        self.missing_cells = self._get_missing_cells()

    def update_value(self, val, x, y):
        board[y][x] = val

    def update_board(self):
        self.missing_row_nums = self._get_missing_row_nums()
        self.missing_col_nums = self._get_missing_col_nums()
        self.missing_square_nums = self._get_missing_square_nums()

    def get_cell_val(self, x, y):
        return self.board[y][x]

    def _get_missing_row_nums(self):
        missing_row_nums = []
        for row in self.board:
            missing_nums = set(range(1, 10))
            for num in row:
                if num in missing_nums:
                    missing_nums.remove(num)
            missing_row_nums.append(missing_nums)
        return missing_row_nums

    def _get_missing_col_nums(self):
        missing_col_nums = []
        for x in range(self.width):
            missing_nums = set(range(1, 10))
            for y in range(self.height):
                num = self.get_cell_val(x, y)
                if num in missing_nums:
                    missing_nums.remove(num)
            missing_col_nums.append(missing_nums)
        return missing_col_nums

    def _get_missing_square_nums(self):
        missing_square_nums = [set(range(1,10)) for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                square_idx = self._determine_square_num(x, y)
                num = self.get_cell_val(x, y)
                if num in missing_square_nums[square_idx]:
                    missing_square_nums[square_idx].remove(num)
        return missing_square_nums

    def _determine_square_num(self, x, y):
        row_num = math.floor(y / 3)
        col_num = math.floor(x / 3)
        return row_num * 3 + col_num

    def _get_missing_cells(self):
        missing_cells = collections.OrderedDict()
        for y, row in enumerate(self.board):
            for x, num in enumerate(row):
                if num == 0:
                    missing_cells[(x, y)] = Cell(self, num, x, y)
        return missing_cells

    def solve(self):
        print('Unsolved:')
        self.print_board()
        board_has_changed = True
        while board_has_changed:
            num_missing_cells_before = len(self.missing_cells)
            for _ in range(num_missing_cells_before):
                missing_cell_id, missing_cell = self.missing_cells.popitem(last=False)
                if missing_cell.has_singleton_solution():
                    missing_cell.update_val_with_singleton()
                    self.update_value(missing_cell.val, missing_cell.x, missing_cell.y)
                else:
                    self.missing_cells[missing_cell_id] = missing_cell
            if len(self.missing_cells) == num_missing_cells_before:
                board_has_changed = False

        if len(self.missing_cells) > 0:
            self.backtrack_solver()

        print('Solved: ')
        self.print_board()

    def backtrack_solver(self, ):
        if len(self.missing_cells) == 0:
            return True

        missing_cell_id, missing_cell = self.missing_cells.popitem(last=False)
        valid_nums = missing_cell.get_valid_nums()

        for valid_num in valid_nums:
            missing_cell._remove_possibility(valid_num)
            is_valid_path = self.backtrack_solver()
            if is_valid_path:
                missing_cell.val = valid_num
                self.update_value(valid_num, missing_cell_id[0], missing_cell_id[1])
                return is_valid_path
            missing_cell._reinsert_possibility(valid_num)

        self.missing_cells[missing_cell_id] = missing_cell
        return False

    def print_board(self):
        for row in self.board:
            str_row = [str(num) for num in row]
            print(' '.join(str_row))
        print('\n')


# Easy board
def generate_board1():
    board = [
        [8, 0, 5, 0, 4, 0, 0, 9, 0],
        [0, 6, 9, 7, 1, 0, 0, 0, 3],
        [7, 0, 0, 3, 0, 8, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 2, 4, 0],
        [5, 4, 0, 0, 3, 0, 0, 1, 8],
        [0, 1, 8, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 8, 0, 4, 0, 0, 9],
        [1, 0, 0, 0, 7, 3, 4, 5, 0],
        [0, 7, 0, 0, 5, 0, 3, 0, 2]
     ]

    return board

# Hard board
def generate_board2():
    board = [
        [int(i) for i in '006000134'],
        [int(i) for i in '300400009'],
        [int(i) for i in '080100000'],
        [int(i) for i in '600500010'],
        [int(i) for i in '000761000'],
        [int(i) for i in '030008007'],
        [int(i) for i in '000009080'],
        [int(i) for i in '100004002'],
        [int(i) for i in '245000600'],
    ]
    return board


if __name__ == '__main__':
    print('Board 1:')
    board = generate_board1()
    sudoku_puzzle = Board(board)
    sudoku_puzzle.solve()

    print('Board 2:')
    board = generate_board2()
    sudoku_puzzle = Board(board)
    sudoku_puzzle.solve()