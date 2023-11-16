import numpy as np
import pygame
import sys
import math
import Board

pygame.init()

board_size = 3

def main():
    # game variables
    game_over = False
    turn = 0 # turn == 0 for player 1, turn == 1 for player 2
    piece_1 = 1 # black
    piece_2 = -1 # white

    # FPS
    FPS = 60
    frames_per_sec = pygame.time.Clock()

    # board 2D array
    board = Board.create_board(Board.ROW_COUNT,Board.COL_COUNT)
    print(board)

    # game screen
    SCREEN = pygame.display.set_mode(Board.SCREENSIZE)
    SCREEN.fill(Board.WHITE)
    pygame.display.set_caption('Gomoku (Connet 5)')
    # icon = pygame.image.load('icon.png')
    # pygame.display.set_icon(icon)

    # font
    my_font = pygame.font.Font('freesansbold.ttf', 32)

    # text message
    label_1 = my_font.render('Black wins!', True, Board.WHITE, Board.BLACK)
    label_2 = my_font.render('White wins!', True, Board.WHITE, Board.BLACK)

    # display the screen
    Board.draw_board(SCREEN)

    # game loop
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_pos = event.pos[0]
                y_pos = event.pos[1]

                col = int(math.floor(x_pos / Board.BLOCKSIZE))
                row = int(math.floor(y_pos / Board.BLOCKSIZE))

                # turn decision, if black(1)/white(2) piece already placed, go back to the previous turn
                if board[row][col] == 1:
                    turn = 0
                if board[row][col] == -1:
                    turn = 1

                # Ask for Player 1 move
                if turn == 0:
                    # check if its a valid location then drop a piece
                    if Board.is_valid_loc(board, row, col):
                        Board.drop_piece(board, row, col, piece_1)
                        Board.draw_piece(SCREEN,board)

                        if Board.who_wins(board,piece_1):
                            print('Black wins!')
                            SCREEN.blit(label_1, (280,50))
                            pygame.display.update()
                            game_over = True

                # Ask for Player 2 move
                else:
                    # check if its a valid location then drop a piece
                    if Board.is_valid_loc(board, row, col):
                        Board.drop_piece(board, row, col, piece_2)
                        Board.draw_piece(SCREEN,board)

                        if Board.who_wins(board,piece_2):
                            print('White wins!')
                            SCREEN.blit(label_2, (280,50))
                            pygame.display.update()
                            game_over = True

                print(board)

                # increment turn
                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(4000)

        frames_per_sec.tick(FPS)

if __name__ == '__main__':
    main()