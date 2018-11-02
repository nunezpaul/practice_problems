import itertools as it

def IsPuzzleSolvable(board):
    """
    Given a 2D list, determine if that board is solvable.
    Solved refers to when the state of the board is
    [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    :param board:
    :return: bool
    """
    blank_pos = FindBlankPos(board)
    visited_boards = StoreBoard(blank_pos, board)
    new_blank_pos_s = GetLegalMoves(blank_pos)
    new_boards = GetNewBoard(blank_pos, new_blank_pos_s, board)
    new_boards_cost = ScoreBoards(new_boards)
    boards_dict, queue = InsertIntoQueue(new_boards, new_boards_cost)

    count = 0
    while len(queue) > 0 and not(queue[0] == 0):
        current_board, blank_pos = PullNextBoard(boards_dict, queue)
        if not IsRepeatedBoard(current_board, blank_pos, visited_boards):
            visited_boards = StoreBoard(blank_pos, current_board, visited_boards=visited_boards)
            new_blank_pos_s = GetLegalMoves(blank_pos)
            new_boards = GetNewBoard(blank_pos, new_blank_pos_s, current_board)
            new_boards_cost = ScoreBoards(new_boards)
            boards_dict, queue = InsertIntoQueue(new_boards, new_boards_cost, boards_dict=boards_dict)
            count += 1

    return count


def PullNextBoard(boards_dict, queue):
    current_board = boards_dict[queue[0]]['boards'].pop()
    boards_dict[queue[0]]['count'] -= 1
    if boards_dict[queue[0]]['count'] == 0:
        _ = queue.pop(0)
    current_blank_pos = FindBlankPos(current_board)
    return current_board, current_blank_pos


def IsRepeatedBoard(current_board, current_blank_pos, visited_boards):
    """
    Check whether we have seen a board already. If so then we are in a loop.
    :param current_board: [[], [], []]
    :param current_blank_pos: [j, i]
    :param visited_boards: {cost: {boards: [boards], 'count': int} }
    :return: boolean
    """
    if current_blank_pos[0] not in visited_boards:
        return False
    if current_blank_pos[1] not in visited_boards[current_blank_pos[0]]:
        return False

    similar_boards = visited_boards[current_blank_pos[0]][current_blank_pos[1]]
    return current_board in similar_boards


def StoreBoard(blank_pos, board, visited_boards={}):
    """
    Storing the current board into a dictionary of boards that we've seen already. Dictionary is based on the position
    of the blank tile
    :param blank_pos: [j, i]
    :param board: [[], [], []]
    :param visited_boards: {cost: [board0, board1...boardn]
    :return:
    """
    if blank_pos[0] not in visited_boards:
        visited_boards[blank_pos[0]] = {}
    if blank_pos[1] not in visited_boards[blank_pos[0]]:
        visited_boards[blank_pos[0]][blank_pos[1]] = []

        visited_boards[blank_pos[0]][blank_pos[1]].append(board)
    return visited_boards


def InsertIntoQueue(new_boards, new_boards_cost, boards_dict={}):
    """
    Insert the boards into a dictionary and return the order in which their keys
    :param new_boards: list of boards
    :param new_boards_cost: list of ints
    :return: new_boards_sorted: list of boards
    """

    for idx, cost in enumerate(new_boards_cost):
        if cost not in boards_dict:
            boards_dict[cost] = {'boards': [], 'count': 0}
        boards_dict[cost]['boards'].append(new_boards[idx])
        boards_dict[cost]['count'] += 1


    queue = sorted(list(boards_dict.keys()))
    return boards_dict, queue

def ScoreBoards(new_boards):
    """
    Score each based on how in accurate it is.
    :param new_boards:
    :return: [cost]
    """
    costs = []
    for new_board in new_boards:
        new_board_flat = it.chain.from_iterable(new_board)
        cost = 0
        for idx, tile_num in enumerate(new_board_flat):
            if idx == 8:
                idx = -1
            cost += abs(tile_num - (idx + 1))
        costs.append(cost)
    return costs

def GetNewBoard(blank_pos, new_blank_pos_s, board):
    """
    this function will give what the final state of the board is after swapping the position of the empty piece.
    :param blank_pos: original position of the blank tile
    :param new_blank_pos: new position of the blank tile
    :param board: original state of the board
    :return: final state after swapping the piece
    """
    new_boards = []
    for new_blank_pos in new_blank_pos_s:
        new_board = [list(row) for row in board]
        new_board[blank_pos[0]][blank_pos[1]], new_board[new_blank_pos[0]][new_blank_pos[1]] = \
            new_board[new_blank_pos[0]][new_blank_pos[1]], new_board[blank_pos[0]][blank_pos[1]]
        new_boards.append(new_board)
    return new_boards

def GetLegalMoves(blank_pos):
    """
    Finds what moves (UP, DOWN, LEFT, RIGHT) are legal to be performed.
    At minimum 2 will be returned. At max 4 will be returned.
    :param blank_pos:
    :return: [[]] all potential legal moves.
    """
    # UP DOWN RIGHT LEFT
    moves = {'U': [1,0], 'D': [-1,0], 'R': [0, 1], 'L':[0, -1]}
    #moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    legal_moves = []
    for move in moves:
        new_pos = list(blank_pos)
        legal = True
        for idx in range(2):
            new_pos[idx] += move[idx]
            legal &= (new_pos[idx] >= 0 and new_pos[idx] < 3)
        if legal:
            legal_moves.append(new_pos)

    return legal_moves

def FindBlankPos(board):
    """
    Find the position of the blank piece on the puzzle board
    :param board:
    :return: [j, i]
    """
    for j in range(3):
        for i in range(3):
            if board[j][i] == 0:
                return [j, i]


if __name__ == '__main__':
    board = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
    print(IsPuzzleSolvable(board))