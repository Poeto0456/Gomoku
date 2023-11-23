import numpy as np
import pygame

ROW_COUNT = 15
COL_COUNT = 15

# define screen size
BLOCKSIZE = 30  # Adjusted for 960x540 resolution
PADDING_RIGHT = 150  # Adjusted for 960x540 resolution
RADIUS = 12  # Adjusted for 960x540 resolution


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (205, 128, 0)

# create a board array
def create_board(row, col):
    board = np.zeros((row, col))
    return board

# draw a board in pygame window
def draw_board(screen, board_size):
    global BLOCKSIZE,S_HEIGHT,S_WIDTH
    BLOCKSIZE = screen.get_height() // board_size
    S_WIDTH = board_size * BLOCKSIZE
    S_HEIGHT = board_size * BLOCKSIZE

    # calculate the starting position to center the board on the screen
    start_x = (screen.get_width() - S_WIDTH) // 2
    start_y = (screen.get_height() - S_HEIGHT) // 2

    for x in range(start_x, S_WIDTH + start_x, BLOCKSIZE):
        for y in range(start_y, S_HEIGHT + start_y, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen, BROWN, rect)

    # draw inner grid lines

    # draw vertical lines
    for x in range(start_x + BLOCKSIZE // 2, S_WIDTH + start_x - BLOCKSIZE // 2 + BLOCKSIZE, BLOCKSIZE):
        line_start = (x, start_y + BLOCKSIZE // 2)
        line_end = (x, start_y + S_HEIGHT - BLOCKSIZE // 2)
        pygame.draw.line(screen, BLACK, line_start, line_end, 2)

    # draw horizontal lines
    for y in range(start_y + BLOCKSIZE // 2, S_HEIGHT + start_y - BLOCKSIZE // 2 + BLOCKSIZE, BLOCKSIZE):
        line_start = (start_x + BLOCKSIZE // 2, y)
        line_end = (start_x + S_WIDTH - BLOCKSIZE // 2, y)
        pygame.draw.line(screen, BLACK, line_start, line_end, 2)

    pygame.display.update()

# drop a piece
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# draw a piece on the board
def draw_piece(screen, board, board_size):
    S_WIDTH = board_size * BLOCKSIZE
    S_HEIGHT = board_size * BLOCKSIZE
    start_x = (screen.get_width() - S_WIDTH) // 2
    start_y = (screen.get_height() - S_HEIGHT) // 2
    # draw game pieces at the center of each grid intersection
    for x in range(board_size):
        for y in range(board_size):
            circle_pos = (start_x+ x* BLOCKSIZE  + BLOCKSIZE // 2, 
                          start_y+ y* BLOCKSIZE + BLOCKSIZE // 2)
            if board[y][x] == 1:
                pygame.draw.circle(screen, BLACK, circle_pos, RADIUS * (BLOCKSIZE//30))
            elif board[y][x] == -1:
                pygame.draw.circle(screen, WHITE, circle_pos, RADIUS * (BLOCKSIZE//30))
    pygame.display.update()

# check if it is a valid location
def is_valid_loc(board, row, col):
    return board[row][col] == 0


# victory decision
def who_wins(board, piece, board_size):
    # check for horizontal win
    for c in range(board_size - 4):
        for r in range(board_size):
            if (board[r][c] == piece 
                and board[r][c + 1] == piece 
                and board[r][c + 2] == piece 
                and board[r][c + 3] == piece 
                and board[r][c + 4] == piece):
                return True

    # check for vertical win
    for c in range(board_size):
        for r in range(board_size - 4):
            if (board[r][c] == piece 
                and board[r + 1][c] == piece 
                and board[r + 2][c] == piece 
                and board[r + 3][c] == piece 
                and board[r + 4][c] == piece):
                return True

    # check for positively sloped diagonal win
    for c in range(board_size - 4):
        for r in range(4, board_size):
            if (board[r][c] == piece 
                and board[r - 1][c + 1] == piece 
                and board[r - 2][c + 2] == piece 
                and board[r - 3][c + 3] == piece 
                and board[r - 4][c + 4] == piece):
                return True

    # check for negatively sloped diagonal win
    for c in range(board_size - 4):
        for r in range(board_size - 4):
            if (board[r][c] == piece 
                and board[r + 1][c + 1] == piece 
                and board[r + 2][c + 2] == piece 
                and board[r + 3][c + 3] == piece 
                and board[r + 4][c + 4] == piece):
                return True
