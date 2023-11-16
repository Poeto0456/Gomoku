import numpy as np
import pygame

ROW_COUNT = 15
COL_COUNT = 15

# define screen size
BLOCKSIZE = 50 # individual grid
S_WIDTH = COL_COUNT * BLOCKSIZE # screen width
S_HEIGHT = ROW_COUNT * BLOCKSIZE # screen height
PADDING_RIGHT = 200 # for game menu
SCREENSIZE = (S_WIDTH + PADDING_RIGHT,S_HEIGHT)
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
def draw_board(screen):
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
def draw_piece(screen,board):
    # draw game pieces at mouse location
    for x in range(COL_COUNT):
        for y in range(ROW_COUNT):
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
def who_wins(board, piece):
    # check for horizontal win
    for c in range(COL_COUNT - 4):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece\
                and board[r][c+4] == piece:
                return True

    # check for vertical win
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-4):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece\
                and board[r+4][c] == piece:
                return True

    # check for positively sloped diagonal wih
    for c in range(COL_COUNT-4):
        for r in range(4,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece\
                and board[r-4][c+4] == piece:
                return True

    # check for negatively sloped diagonal win
    for c in range(COL_COUNT-4):
        for r in range(ROW_COUNT-4):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece\
                and board[r+4][c+4] == piece:
                return True