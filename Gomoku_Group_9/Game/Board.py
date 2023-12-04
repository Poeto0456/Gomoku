import numpy as np
import sys
sys.path.insert(0, "D:\DSEB\DSEB Sem 3\pyt\git\gomoku 1.3\Gomoku\Gomoku_Group_9")
from Functions import coordinates_set

o = 1
x = -1
empty = 0

n_in_a_row = 5 
o_win = n_in_a_row
x_win = -n_in_a_row
start_player = 1
board_size = 15

class Board:
    def __init__(self):
        self.board = np.zeros((board_size, board_size))
        self.available_actions = coordinates_set(board_size , board_size)
        self.last_action = None  
        self.current_player = start_player  

    def __copy__(self):
        new_board = Board()
        new_board.board = self.board.copy()
        new_board.available_actions = self.available_actions.copy()
        new_board.last_action = self.last_action
        new_board.current_player = self.current_player
        return new_board
    
    def reset(self):
        self.board = np.zeros((board_size, board_size))
        self.available_actions = coordinates_set(board_size, board_size)
        self.last_action = None
        self.current_player = start_player

    def step(self, action):
        i = action[0]
        j = action[1]
        if (i, j) not in self.available_actions:
            return False  
        self.board[i, j] = self.current_player
        self.available_actions.remove((i, j))
        self.last_action = (i, j)
        self.current_player = -self.current_player
        return True

    def result(self):
        for piece in coordinates_set(board_size, board_size) - self.available_actions:
            i = piece[0]
            j = piece[1]

            if j in range(board_size - n_in_a_row + 1):
                s = sum([self.board[i, j + v] for v in range(n_in_a_row)])
                if s == o_win or s == x_win:
                    return True, s / n_in_a_row

            if i in range(board_size - n_in_a_row + 1):
                s = sum([self.board[i + v, j] for v in range(n_in_a_row)])
                if s == o_win or s == x_win:
                    return True, s / n_in_a_row

            if i in range(board_size - n_in_a_row + 1) and j in range(board_size - n_in_a_row + 1):
                s = sum([self.board[i + v, j + v] for v in range(n_in_a_row)])
                if s == o_win or s == x_win:
                    return True, s / n_in_a_row

            if i not in range(n_in_a_row - 1) and j in range(board_size - n_in_a_row + 1):
                s = sum([self.board[i - v, j + v] for v in range(n_in_a_row)])
                if s == o_win or s == x_win:
                    return True, s / n_in_a_row

        if len(self.available_actions) == 0:
            return True, empty

        return False, empty
