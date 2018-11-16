class JumpGame(object):
    def __init__(self, board):
        assert min(board) >= 0
        self.board = board
        self.seen_idx = set()

    def can_win(self, start_idx):
        self.seen_idx = set()
        return self._depth_first_search(start_idx)

    def _depth_first_search(self, start_idx):
        if self.board[start_idx] == 0:
            return True
        elif start_idx in self.seen_idx:
            return False

        self.seen_idx.add(start_idx)
        next_idxs = self._get_next_idxs(start_idx)
        result = False
        for next_idx in next_idxs:
            result |= self._depth_first_search(next_idx)

        return result

    def _get_next_idxs(self, start_idx):
        left_jump = start_idx - self.board[start_idx]
        right_jump = start_idx + self.board[start_idx]

        legal_jumps = []
        for jump in (left_jump, right_jump):
            if (jump >= 0) and (jump < len(self.board)):
                legal_jumps.append(jump)

        return legal_jumps

def test():
    board = [1, 2, 1, 1, 0]
    jump_game = JumpGame(board)
    for idx in range(len(board)):
        assert jump_game.can_win(idx)

    board = [1, 1, 1, 1, 1]
    jump_game = JumpGame(board)
    for idx in range(len(board)):
        assert not jump_game.can_win(idx)

    board = [10, 10, 0, 10, 10, 3]
    results = [False, False, True, False, False, True]
    jump_game = JumpGame(board)
    for idx, result in zip(range(len(board)), results):
        assert result == jump_game.can_win(idx)


if __name__ == '__main__':
    test()