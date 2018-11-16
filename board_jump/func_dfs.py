def can_win(board, pos):
    pos_history = set()
    return _depth_first_search(board, pos, pos_history)

def _depth_first_search(board, pos, pos_history):
    if board[pos] == 0:
        return True
    elif pos in pos_history:
        return False

    pos_history.add(pos)
    next_poss = _get_legal_jumps(board, pos)
    result = False
    for next_pos in next_poss:
        result |= _depth_first_search(board, next_pos, pos_history)

    return result

def _get_legal_jumps(board, pos):
    left_pos = pos - board[pos]
    right_pos = pos + board[pos]

    legal_moves = []
    for new_pos in (left_pos, right_pos):
        if (new_pos >= 0) and (new_pos < len(board)):
            legal_moves.append(new_pos)

    return legal_moves

def test():
    board = [1, 2, 1, 1, 0]
    results = [True] * len(board)
    for idx, result in zip(range(len(board)), results):
        assert result == can_win(board, idx)

    board = [1, 1, 1, 1, 1]
    results = [False] * len(board)
    for idx, result in zip(range(len(board)), results):
        assert result == can_win(board, idx)

    board = [10, 10, 0, 10, 10, 3]
    results = [False, False, True, False, False, True]
    for idx, result in zip(range(len(board)), results):
        assert result == can_win(board, idx)


if __name__ == '__main__':
    test()
    board = [1, 3, 2, 0, 5, 2, 8, 4, 1]
    for idx in range(len(board)):
        print(idx, can_win(board, idx), board[idx])