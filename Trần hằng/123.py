import pygame
import pygame_gui
import sys
import math
import numpy as np
from pygame.locals import *

class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        super().__init__()
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.font = pygame.font.Font(None, 45)
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def update_position(self, pos):
        self.rect.topleft = pos

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.checkForInput(pygame.mouse.get_pos()):
                # Do something when the button is clicked
                pass

    def handle_hover(self):
        if self.checkForInput(pygame.mouse.get_pos()):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

ROW_COUNT = 15
COL_COUNT = 15

# define screen size
BLOCKSIZE = 30  # Adjusted for 960x540 resolution
PADDING_RIGHT = 150  # Adjusted for 960x540 resolution
RADIUS = 12  # Adjusted for 960x540 resolution

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (205, 128, 0)

# create a board array
def create_board(row, col):
    board = np.zeros((row, col))
    return board

# draw a board in pygame window
def draw_board(screen, board_size):
    S_WIDTH = board_size * BLOCKSIZE
    S_HEIGHT = board_size * BLOCKSIZE
    for x in range(0, S_WIDTH, BLOCKSIZE):
        for y in range(0, S_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen, BROWN, rect)

    # draw inner grid lines
    # draw vertical lines
    for x in range(BLOCKSIZE // 2, S_WIDTH - BLOCKSIZE // 2 + BLOCKSIZE, BLOCKSIZE):
        line_start = (x, BLOCKSIZE // 2)
        line_end = (x, S_HEIGHT - BLOCKSIZE // 2)
        pygame.draw.line(screen, BLACK, line_start, line_end, 2)

    # draw horizontal lines
    for y in range(BLOCKSIZE // 2, S_HEIGHT - BLOCKSIZE // 2 + BLOCKSIZE, BLOCKSIZE):
        line_start = (BLOCKSIZE // 2, y)
        line_end = (S_WIDTH - BLOCKSIZE // 2, y)
        pygame.draw.line(screen, BLACK, line_start, line_end, 2)
    pygame.display.update()

# drop a piece
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# draw a piece on the board
def draw_piece(screen, board, board_size):
    # draw game pieces at the mouse location
    for x in range(board_size):
        for y in range(board_size):
            circle_pos = (x * BLOCKSIZE + BLOCKSIZE // 2, y * BLOCKSIZE + BLOCKSIZE // 2)
            if board[y][x] == 1:
                pygame.draw.circle(screen, BLACK, circle_pos, RADIUS)
            elif board[y][x] == -1:
                pygame.draw.circle(screen, WHITE, circle_pos, RADIUS)
    pygame.display.update()

# check if it is a valid location
def is_valid_loc(board, row, col):
    return board[row][col] == 0

# victory decision
def who_wins(board, piece, board_size):
    # check for horizontal win
    for c in range(board_size - 4):
        for r in range(board_size):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece \
                    and board[r][c + 4] == piece:
                return True

    # check for vertical win
    for c in range(board_size):
        for r in range(board_size - 4):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece \
                    and board[r + 4][c] == piece:
                return True

    # check for positively sloped diagonal win
    for c in range(board_size - 4):
        for r in range(4, board_size):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece \
                    and board[r - 4][c + 4] == piece:
                return True

    # check for negatively sloped diagonal win
    for c in range(board_size - 4):
        for r in range(board_size - 4):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece \
                    and board[r + 4][c + 4] == piece:
                return True


def main():
    pygame.init()
    # game variables
    game_over = False
    turn = 0  # turn == 0 for player 1, turn == 1 for player 2
    piece_1 = 1  # black
    piece_2 = -1  # white

    # FPS
    FPS = 60
    frames_per_sec = pygame.time.Clock()

    # board 2D array
    board = create_board(ROW_COUNT, COL_COUNT)
    print(board)

    # game screen
    SCREEN = pygame.display.set_mode((1280, 750))
    SCREEN.fill(WHITE)
    pygame.display.set_caption('Gomoku (Connect 5)')

    # font
    my_font = pygame.font.Font('freesansbold.ttf', 32)


    # text message
    label_1 = my_font.render('Black wins!', True, WHITE, BLACK)
    label_2 = my_font.render('White wins!', True, WHITE, BLACK)

    # display the screen
    draw_board(SCREEN, ROW_COUNT)

    # Setting button
    setting_button = Button(None, pos=(960, 540),
                            text_input='setting', font="font.ttf",
                            base_color="White", hovering_color="Pink")
    
    # game loop
    while not game_over:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if setting_button.checkForInput(mouse_pos):
                    show_settings_menu(SCREEN)

                x_pos = event.pos[0]
                y_pos = event.pos[1]

                col = int(math.floor(x_pos / BLOCKSIZE))
                row = int(math.floor(y_pos / BLOCKSIZE))

                # turn decision, if black(1)/white(2) piece already placed, go back to the previous turn
                if board[row][col] == 1:
                    turn = 0
                if board[row][col] == -1:
                    turn = 1

                # Ask for Player 1 move
                if turn == 0:
                    # check if it's a valid location then drop a piece
                    if is_valid_loc(board, row, col):
                        drop_piece(board, row, col, piece_1)
                        draw_piece(SCREEN, board, ROW_COUNT)

                        if who_wins(board, piece_1, ROW_COUNT):
                            print('Black wins!')
                            SCREEN.blit(label_1, (280, 50))
                            pygame.display.update()
                            game_over = True

                # Ask for Player 2 move
                else:
                    # check if it's a valid location then drop a piece
                    if is_valid_loc(board, row, col):
                        drop_piece(board, row, col, piece_2)
                        draw_piece(SCREEN, board, ROW_COUNT)

                        if who_wins(board, piece_2, ROW_COUNT):
                            print('White wins!')
                            SCREEN.blit(label_2, (280, 50))
                            pygame.display.update()
                            game_over = True

                print(board)

                # increment turn
                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(4000)
        setting_button.changeColor(mouse_pos)
        setting_button.update(SCREEN)
        frames_per_sec.tick(FPS)
    

def show_settings_menu(screen):
    while True:
        mouse_pos = pygame.mouse.get_pos()

        screen.fill(WHITE)  # Clear the screen

        # Settings menu buttons
        option1_button = Button(image=None, pos=(640 * 3 // 4, 300 * 3 // 4),
                                text_input="Option 1", font='font.ttf',
                                base_color="White", hovering_color="Pink")
        option2_button = Button(image=None, pos=(640 * 3 // 4, 400 * 3 // 4),
                                text_input="Option 2", font='font.ttf',
                                base_color="White", hovering_color="Pink")
        back_button = Button(image=None, pos=(640 * 3 // 4, 600 * 3 // 4),
                             text_input="BACK", font='font.ttf',
                             base_color="White", hovering_color="Pink")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if option1_button.checkForInput(mouse_pos):
                    # Handle Option 1 action
                    pass
                elif option2_button.checkForInput(mouse_pos):
                    # Handle Option 2 action
                    pass
                elif back_button.checkForInput(mouse_pos):
                    return  # Return to the previous menu

        for button in [option1_button, option2_button, back_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        pygame.display.update()


if __name__ == '__main__':
    main()
