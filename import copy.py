import copy

BOARD_SIZE = 15
WIN_COUNT = 5
DEPTH = 2

class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        
    def place_stone(self, x, y, stone):
        if self.board[x][y] == ' ':
            self.board[x][y] = stone
            return True
        return False

    def check_win(self, x, y):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for i in range(1, WIN_COUNT):
                if 0 <= x + i * dx < BOARD_SIZE and 0 <= y + i * dy < BOARD_SIZE and \
                   self.board[x][y] == self.board[x + i * dx][y + i * dy]:
                    count += 1
                else:
                    break
            for i in range(1, WIN_COUNT):
                if 0 <= x - i * dx < BOARD_SIZE and 0 <= y - i * dy < BOARD_SIZE and \
                   self.board[x][y] == self.board[x - i * dx][y - i * dy]:
                    count += 1
                else:
                    break
            if count >= WIN_COUNT:
                return True
        return False

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def display(self):
        for row in self.board:
            print(' '.join(row))
            print()

def evaluate(board, stone):
    # Simple evaluation function: the more stones in a line, the better.
    score = 0
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board.board[x][y] == stone:
                for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                    count = 1
                    for i in range(1, WIN_COUNT):
                        if 0 <= x + i * dx < BOARD_SIZE and 0 <= y + i * dy < BOARD_SIZE and \
                           board.board[x][y] == board.board[x + i * dx][y + i * dy]:
                            count += 1
                    score += count ** 2
    return score

def minimax(board, depth, maximizingPlayer, alpha, beta):
    if depth == 0 or board.check_win(0, 0) or board.is_full():
        return evaluate(board, 'O') - evaluate(board, 'X')

    if maximizingPlayer:
        maxEval = float('-inf')
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if board.board[x][y] == ' ':
                    new_board = copy.deepcopy(board)
                    new_board.place_stone(x, y, 'O')
                    eval = minimax(new_board, depth - 1, False, alpha, beta)
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return maxEval

    else:
        minEval = float('inf')
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if board.board[x][y] == ' ':
                    new_board = copy.deepcopy(board)
                    new_board.place_stone(x, y, 'X')
                    eval = minimax(new_board, depth - 1, True, alpha, beta)
                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return