import itertools as it


class Board(object):
    def __init__(self, board, blank_pos=None, prev_moves=None):
        self.board = board
        self.prev_moves = prev_moves if prev_moves else []
        self.blank_pos = blank_pos if blank_pos else self.find_blank_pos()
        self.legal_next_moves = self.get_legal_next_moves()
        self.cost = self.score_board()

    def find_blank_pos(self):
        """
        Find the position of the blank piece on the puzzle board
        :return blank_pos: [j, i]
        """
        for j in range(3):
            for i in range(3):
                if self.board[j][i] == 0:
                    return [j, i]

    def get_legal_next_moves(self):
        """
        Finds what moves (UP, DOWN, LEFT, RIGHT) are legal to be performed.
        At minimum 2 will be returned. At max 4 will be returned.
        :return: [[]] all potential legal moves.
        """
        # UP DOWN RIGHT LEFT
        moves = {'D': [1, 0], 'U': [-1, 0], 'R': [0, 1], 'L': [0, -1]}
        legal_moves = {}
        for key, move in moves.items():
            new_pos = list(self.blank_pos)
            legal = True
            for idx in range(2):
                new_pos[idx] += move[idx]
                legal &= (new_pos[idx] >= 0 and new_pos[idx] < 3)
            if legal:
                legal_moves[key] = new_pos

        return legal_moves

    def score_board(self):
        """
        Score board based on how in accurate it is.
        :return: [cost]
        """
        correct_pos = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1]
        }

        cost = 0
        for j in range(3):
            for i in range(3):
                num = self.board[j][i]
                if num != 0:
                    true_pos = correct_pos[self.board[j][i]]
                    cost += abs(true_pos[0] - j) + abs(true_pos[1] - i)
        return cost

    def create_new_boards(self):
        """
        This function will give what the final state of the board is after swapping the position of the empty piece.
        :return Boards: final state of the board as a Board object after moving the blank to legal blank positions
        """
        new_boards = []
        for key, new_blank_pos in self.legal_next_moves.items():
            new_board = [list(row) for row in self.board]
            new_board[self.blank_pos[0]][self.blank_pos[1]], new_board[new_blank_pos[0]][new_blank_pos[1]] = \
                new_board[new_blank_pos[0]][new_blank_pos[1]], new_board[self.blank_pos[0]][self.blank_pos[1]]
            new_boards.append(Board(new_board, blank_pos=new_blank_pos, prev_moves=self.prev_moves + [key]))
        return new_boards


def is_puzzle_solvable(board):
    """
    Given a 2D list, determine if that board is solvable.
    Solved refers to when the state of the board is
    [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    :param board:
    :return: bool
    """
    board_2D = convert_board_2D(board)
    current_board = Board(board_2D)
    visited_boards = store_board(current_board)
    new_boards = current_board.create_new_boards()
    boards_dict, queue = insert_into_queue(new_boards)

    while len(queue) > 0 and not(queue[0] == 0):
        current_board = pull_next_board(boards_dict, queue)
        if not is_repeated_board(current_board, visited_boards):
            visited_boards = store_board(current_board, visited_boards=visited_boards)
            new_boards = current_board.create_new_boards()
            boards_dict, queue = insert_into_queue(new_boards, boards_dict=boards_dict)

    if queue[0] == 0:
        winning_board = pull_next_board(boards_dict, queue)
        return True, ''.join(winning_board.prev_moves)
    else:
        return False, None


def pull_next_board(boards_dict, queue):
    next_board = boards_dict[queue[0]]['boards'].pop()
    boards_dict[queue[0]]['count'] -= 1
    if boards_dict[queue[0]]['count'] == 0:
        key_to_remove = queue.pop(0)
        boards_dict.pop(key_to_remove)
    return next_board

def is_repeated_board(current_board, visited_boards):
    """
    Check whether we have seen a board already. If so then we are in a loop.
    :param current_board: [[], [], []]
    :param current_blank_pos: [j, i]
    :param visited_boards: {cost: {boards: [boards], 'count': int} }
    :return: boolean
    """
    blank_pos = current_board.blank_pos
    blank_pos_1D = convert_blank_1D(blank_pos)

    if blank_pos_1D not in visited_boards:
        return False

    similar_boards = visited_boards[blank_pos_1D]
    board_to_check = ''.join([str(i) for i in it.chain.from_iterable(current_board.board)])
    return board_to_check in similar_boards

def store_board(current_board, visited_boards={}):
    """
    Storing the current board into a dictionary of boards that we've seen already. Dictionary is based on the position
    of the blank tile
    :param current_board: Board
    :param visited_boards: {cost: [board0, board1...boardn]
    :return:
    """
    blank_pos = current_board.blank_pos
    blank_pos_1D = convert_blank_1D(blank_pos)

    board = current_board.board
    board_1D = ''.join([str(i) for i in it.chain.from_iterable(board)])
    if blank_pos_1D not in visited_boards:
        visited_boards[blank_pos_1D] = set()

    visited_boards[blank_pos_1D].add(board_1D)
    return visited_boards

def convert_blank_1D(blank_pos):
    return blank_pos[0] * 3 + blank_pos[1]

def insert_into_queue(new_boards, boards_dict={}):
    """
    Insert the boards into a dictionary and return the order in which their keys
    :param new_boards: list of Board objects
    :return boards_dict: dictionary of boards with key of the cost
    :return queue: list of ints. It is the call order of the keys in boards_dict
    """

    for new_board in new_boards:
        cost = new_board.cost
        if cost not in boards_dict:
            boards_dict[cost] = {'boards': [], 'count': 0}
        boards_dict[cost]['boards'].append(new_board)
        boards_dict[cost]['count'] += 1


    queue = sorted(list(boards_dict.keys()))
    return boards_dict, queue

def convert_board_2D(board):
    board_2D = []
    for j in range(3):
        row = []
        for i in range(3):
            row.append(board[3 * j + i])
        board_2D.append(row)
    return board_2D

if __name__ == '__main__':
    # board_strings = ['123405786', '123745086', '123480765', '413726580']
    # for board_string in board_strings:
    # board_string = '123405786'
    # board = [int(i) for i in board_string]
    # print(board_string, is_puzzle_solvable(board))

    # board_string = '123480765'
    # board = [int(i) for i in board_string]
    # print(board_string, is_puzzle_solvable(board))

    board_string = '876543021'
    board = [int(i) for i in board_string]
    print(board_string, is_puzzle_solvable(board))
