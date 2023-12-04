import numpy as np
import pygame

ROW_COUNT = 15
COL_COUNT = 15


BLOCKSIZE = 50 
RADIUS = 20

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
    global BLOCKSIZE,S_HEIGHT,S_WIDTH,start_x,start_y
    BLOCKSIZE = screen.get_height() // board_size
    S_WIDTH = board_size * BLOCKSIZE
    S_HEIGHT = board_size * BLOCKSIZE
    start_x = (screen.get_width() - S_WIDTH) // 2
    start_y = (screen.get_height() - S_HEIGHT) // 2

    for x in range(start_x, S_WIDTH + start_x, BLOCKSIZE):
        for y in range(start_y, S_HEIGHT + start_y, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen, BROWN, rect)
    # calculate the starting position to center the board on the screen


    # draw inner grid lines
    # draw vertical lines
    for x in range(start_x + BLOCKSIZE // 2, 
                    S_WIDTH + start_x - BLOCKSIZE // 2 + BLOCKSIZE, BLOCKSIZE):
                line_start = (x, start_y + BLOCKSIZE // 2)
                line_end = (x, start_y + S_HEIGHT - BLOCKSIZE // 2)
                pygame.draw.line(screen, BLACK, line_start, line_end, 2)
    # draw horizontal lines
    for y in range(start_y + BLOCKSIZE // 2, 
                   S_HEIGHT + start_y - BLOCKSIZE // 2 + BLOCKSIZE , BLOCKSIZE):
        line_start = (start_x + BLOCKSIZE // 2, y)
        line_end = (start_x + S_WIDTH - BLOCKSIZE // 2, y)
        pygame.draw.line(screen, BLACK, line_start, line_end, 2)

    pygame.display.update()

# drop a piece
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# draw a piece on board
def draw_piece(screen,board, board_size):
    # draw game pieces at mouse location
    for x in range(board_size):
        for y in range(board_size):
            circle_pos = (start_x+ x* BLOCKSIZE  + BLOCKSIZE // 2, 
                          start_y+ y* BLOCKSIZE + BLOCKSIZE // 2)
            if board[y][x] == 1:
                pygame.draw.circle(screen, BLACK, circle_pos, RADIUS * (BLOCKSIZE//40))
            elif board[y][x] == -1:
                pygame.draw.circle(screen, WHITE, circle_pos, RADIUS * (BLOCKSIZE//40))
    pygame.display.update()
