from pygame_menu import widgets
from pygame_menu import Menu
import pygame_menu
import pygame
import sys
import math
import Board
from Button import Button
import settingmenu


board_size = 15

pygame.init()


def main():
    # game variables
    game_over = False
    turn = 0  # turn == 0 for player 1, turn == 1 for player 2
    piece_1 = 1  # black
    piece_2 = -1  # white

    # FPS
    FPS = 60
    frames_per_sec = pygame.time.Clock()

    # board 2D array
    board = Board.create_board(board_size, board_size)
    print(board)

    # game screen
    SCREEN = pygame.display.set_mode((960, 540))
    SCREEN.fill(Board.BLACK)
    pygame.display.set_caption('Gomoku (Connect 5)')

    # font
    my_font = pygame.font.Font('font.ttf', 32)

    # text message
    label_1 = my_font.render('Black wins!', True, Board.WHITE, Board.BLACK)
    label_2 = my_font.render('White wins!', True, Board.WHITE, Board.BLACK)

    # display the screen
    Board.draw_board(SCREEN, board_size)
    setting_button_image = pygame.image.load("cog_7712512.png")
    setting_button_image = pygame.transform.scale(setting_button_image,(50,50))
    # Setting button
    setting_button = Button((setting_button_image),pos=(900,50), 
                            text_input=None, font=None, base_color="White", 
                            hovering_color="Pink")
    settings_menu_visible = False
    last_click_time = pygame.time.get_ticks()

    # game loop
    while not game_over:
        mouse_pos = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if setting_button.checkForInput(mouse_pos):
                    if current_time - last_click_time > 200:
                        settings_menu_visible = not settings_menu_visible
                        if settings_menu_visible:
                            show_settings_menu(SCREEN)
                    else:
                            pygame.time.wait(200)
                              # Optional delay to avoid triggering both hide and show actions rapidly
                    last_click_time = current_time

                x_pos =event.pos[0]
                y_pos = event.pos[1]
                offset_x = (SCREEN.get_width() - Board.S_WIDTH) // 2
                offset_y = (SCREEN.get_height() - Board.S_HEIGHT) // 2

                # Adjust mouse coordinates to consider the offset
                x_pos_adjusted = x_pos - offset_x
                y_pos_adjusted = y_pos - offset_y

# Calculate row and column based on adjusted coordinates
                col = int(math.floor(x_pos_adjusted / Board.BLOCKSIZE))
                row = int(math.floor(y_pos_adjusted / Board.BLOCKSIZE))


                if 0 <= row < len(board) and 0 <= col < len(board[0]):        # turn decision, if black(1)/white(2) piece already placed, go back to the previous turn
                    if board[row][col] == 1:
                                turn = 0
                    if board[row][col] == -1:
                                turn = 1

                # Ask for Player 1 move
                if turn == 0:
                    if Board.is_valid_loc(board, row, col):
                        Board.drop_piece(board, row, col, piece_1)
                        Board.draw_piece(SCREEN, board, board_size)

                    if Board.who_wins(board, piece_1, board_size):
                        print('Black wins!')
                        SCREEN.blit(label_1, (280, 50))
                        pygame.display.update()
                        game_over = True

                        # Ask for Player 2 move
                else:
                            # check if it's a valid location then drop a piece
                    if Board.is_valid_loc(board, row, col):
                        Board.drop_piece(board, row, col, piece_2)
                        Board.draw_piece(SCREEN, board, board_size)

                    if Board.who_wins(board, piece_2, board_size):
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

        pygame.display.update()
        frames_per_sec.tick(FPS)


def show_settings_menu(screen):
    pygame.init()
    # Settings menu buttons
    quit_button = Button(image=None, pos=(720, 140),
                            text_input="QUIT", font="font.ttf",
                            base_color="White", hovering_color="Pink")
    restart_button = Button(image=None, pos=(720, 280),
                            text_input="RESTART", font="font.ttf",
                            base_color="White", hovering_color="Pink")
    back_button = Button(image=None, pos=(720, 420),
                         text_input="CONTINUE", font='font.ttf',
                         base_color="White", hovering_color="Pink")
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if option1_button.checkForInput(mouse_pos):
                    pygame.quit()   
                elif option2_button.checkForInput(mouse_pos):
                    main()
                elif back_button.checkForInput(mouse_pos):
                    pass

        for button in [option1_button, option2_button, back_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        pygame.display.update()

if __name__ == '__main__':
    main()