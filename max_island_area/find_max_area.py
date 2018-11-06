class Pos(object):
    def __init__(self, x, y, grid, side_len):
        self.x = x
        self.y = y
        self.val = grid[self.y][self.x]
        self.side_len = side_len
        self.num_moves = 0
        if self.val > 0:
            grid[self.y][self.x] = 0
            self.moves = self.get_next_moves(grid)

    def get_next_moves(self, grid):
        checks = [self.check_up, self.check_down, self.check_left, self.check_right]
        moves = []
        for check in checks:
            result = check(grid)
            if result:
                self.num_moves += 1
                moves.append(result)
        return moves

    def check_up(self, grid):
        new_y = self.y - 1
        if new_y >= 0 and grid[new_y][self.x]:
            return Pos(self.x, new_y, grid, self.side_len)
        return None

    def check_down(self, grid):
        new_y = self.y + 1
        if new_y < self.side_len and grid[new_y][self.x]:
            return Pos(self.x, new_y, grid, self.side_len)
        return None

    def check_left(self, grid):
        new_x = self.x - 1
        if new_x >= 0 and grid[self.y][new_x]:
            return Pos(new_x, self.y, grid, self.side_len)
        return None

    def check_right(self, grid):
        new_x = self.x + 1
        if new_x < self.side_len and grid[self.y][new_x]:
            return Pos(new_x, self.y, grid, self.side_len)
        return None

def max_island(grid):
    side_len = len(grid)
    max_area = 0
    for j in range(side_len):
        for i in range(side_len):
            cur_pos = Pos(x=i, y=j, grid=grid, side_len=side_len)
            if cur_pos.val == 1:
                area = dfs(cur_pos, grid) + 1
                max_area = max(max_area, area)
    return max_area

def dfs(cur_pos, grid):
    moves = cur_pos.moves
    total = cur_pos.num_moves
    for next_pos in moves:
        total += dfs(next_pos, grid)
    return total

if __name__ == '__main__':
    grid = [
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1]
    ]
    print(max_island(grid))  # 6

    grid = [
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1]
    ]
    print(max_island(grid))  # 12
