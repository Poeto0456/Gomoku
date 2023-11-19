import numpy as np
import pygame

ROW_COUNT = 15
COL_COUNT = 15

# define screen size
BLOCKSIZE = 50 # individual grid
PADDING_RIGHT = 200 # for game menu
RADIUS = 20 # game piece radius

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BROWN = (205,128,0)

# create a board array
def create_board(row, col):
    board = np.zeros((row,col))
    return board

# draw a board in pygame window
def draw_board(screen, board_size):
    S_WIDTH = board_size * BLOCKSIZE
    S_HEIGHT = board_size * BLOCKSIZE
    for x in range(0,S_WIDTH,BLOCKSIZE):
        for y in range(0,S_HEIGHT,BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen,BROWN,rect)

    # draw inner grid lines
    # draw vertical lines
    for x in range(BLOCKSIZE // 2, S_WIDTH - BLOCKSIZE // 2 + BLOCKSIZE, BLOCKSIZE):
        line_start = (x, BLOCKSIZE // 2)
        line_end = (x,S_HEIGHT-BLOCKSIZE // 2)
        pygame.draw.line(screen, BLACK, line_start,line_end,2)

    # draw horizontal lines
    for y in range(BLOCKSIZE // 2, S_HEIGHT - BLOCKSIZE // 2 + BLOCKSIZE, BLOCKSIZE):
        line_start = (BLOCKSIZE // 2,y)
        line_end = (S_WIDTH-BLOCKSIZE // 2,y)
        pygame.draw.line(screen, BLACK, line_start,line_end,2)
    pygame.display.update()

# drop a piece
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# draw a piece on board
def draw_piece(screen,board, board_size):
    # draw game pieces at mouse location
    for x in range(board_size):
        for y in range(board_size):
            circle_pos = (x * BLOCKSIZE + BLOCKSIZE//2, y * BLOCKSIZE + BLOCKSIZE//2)
            if board[y][x] == 1:
                pygame.draw.circle(screen, BLACK, circle_pos, RADIUS)
            elif board[y][x] == -1:
                pygame.draw.circle(screen, WHITE, circle_pos, RADIUS)
    pygame.display.update()

# check if it is a valid location
def is_valid_loc(board, row, col):
    return board[row][col] == 0

# victory decision
def who_wins(board, piece, board_size, win_condition):
    # check for horizontal win
    for c in range(board_size - win_condition + 1):
        for r in range(board_size):
            count = 0 # count the number of consecutive pieces
            for i in range(win_condition):
                if board[r][c+i] == piece:
                    count += 1
                else:
                    break
            if count == win_condition: # if the count reaches the win condition, return True
                return True

    # check for vertical win
    for c in range(board_size):
        for r in range(board_size - win_condition + 1):
            count = 0
            for i in range(win_condition):
                if board[r+i][c] == piece:
                    count += 1
                else:
                    break
            if count == win_condition:
                return True

    # check for positively sloped diagonal win
    for c in range(board_size - win_condition + 1):
        for r in range(win_condition - 1, board_size):
            count = 0
            for i in range(win_condition):
                if board[r-i][c+i] == piece:
                    count += 1
                else:
                    break
            if count == win_condition:
                return True

    # check for negatively sloped diagonal win
    for c in range(board_size - win_condition + 1):
        for r in range(board_size - win_condition + 1):
            count = 0
            for i in range(win_condition):
                if board[r+i][c+i] == piece:
                    count += 1
                else:
                    break
            if count == win_condition:
                return True

    # check for draw
    if np.count_nonzero(board) == board_size ** 2: #the board is full and no one wins
        return "It's a draw!"

    # otherwise, return False
    return False
