import pygame
import sys
import math

import Draw as dr
import AI_MCTS
import Board
from Button import Button

pygame.init()

AI_value = 0
music_playing = True
chess_playing = True
chess_click=pygame.mixer.Sound("chess.mp3")

def main():  
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer_music.load('Tokyo.mp3')
    pygame.mixer_music.play(-1)
    pygame.mixer_music.set_volume(0.3)
    board_size = Board.board_size

    # game variables
    game_over = False
    turn = 0 # turn == 0 for player 1, turn == 1 for player 2
    piece_1 = 1 # black
    piece_2 = -1 # white

    AI = AI_MCTS.AI_MCTS(is_output_analysis = True)

    # FPS
    FPS = 60
    frames_per_sec = pygame.time.Clock()

    # board 2D array
    board = Board.Board()
    print(board.board)

    # game screen
    SCREEN = pygame.display.set_mode((1280, 720))
    SCREEN.fill((211, 211, 211))
    BG = pygame.image.load("Background.jpg")
    pygame.display.set_caption('Gomoku')
    SCREEN.blit(BG, (0,0))
            
    # font
    my_font = pygame.font.Font('go3v2.ttf', 56)

    # text message
    label_1 = my_font.render('Black wins!', True, dr.WHITE, dr.BLACK)
    label_2 = my_font.render('White wins!', True, dr.WHITE, dr.BLACK)
    label_3 = my_font.render('Draw!', True, dr.WHITE, dr.BLACK)

    # display the screen
    dr.draw_board(SCREEN, board_size)
    global music_playing
    global chess_playing
    global AI_value

    if AI_value == 0:
    # game loop
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        show_settings_menu(SCREEN, board)
                    SCREEN.blit(BG, (0,0))
                    dr.draw_board(SCREEN, board_size)
                    dr.draw_piece(SCREEN, board.board, board_size)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_pos = event.pos[0]
                    y_pos = event.pos[1]

                    col = int(math.floor(x_pos / dr.BLOCKSIZE))
                    row = int(math.floor(y_pos / dr.BLOCKSIZE))

                    # turn decision, if black(1)/white(2) piece already placed, go back to the previous turn
                    if board.board[row][col] == 1:
                        turn = 0
                    if board.board[row][col] == -1:
                        turn = 1

                    # Ask for Player 1 move
                    if turn == 0:
                        # check if its a valid location then drop a piece
                        if board.step((row,col)):
                            dr.drop_piece(board.board, row, col, piece_1)
                            if chess_playing:
                                chess_click.play()
                            dr.draw_piece(SCREEN,board.board, board_size)

                            if board.result() == (True, 1):
                                SCREEN.blit(label_1, (480,50))
                                pygame.display.update()
                                game_over = True
                            elif board.result() == (True, 0):
                                SCREEN.blit(label_3, (580, 50))
                                pygame.display.update()
                                game_over = True

                    # Ask for Player 2 move
                    else:
                        # check if its a valid location then drop a piece
                        if board.step((row,col)):
                            dr.drop_piece(board.board, row, col, piece_2)
                            if chess_playing:
                                chess_click.play()
                            dr.draw_piece(SCREEN,board.board, board_size)

                            if board.result() == (True, -1):
                                SCREEN.blit(label_2, (480,50))
                                pygame.display.update()
                                game_over = True
                            elif board.result() == (True, 0):
                                SCREEN.blit(label_3, (580, 50))
                                pygame.display.update()
                                game_over = True

                    print(board.board)

                    # increment turn
                    turn += 1
                    turn = turn % 2

                    if game_over:
                        pygame.mixer_music.stop()
                        pygame.time.wait(4000)

            frames_per_sec.tick(FPS)

    elif AI_value == 1:
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        show_settings_menu(SCREEN, board)
                    SCREEN.blit(BG, (0,0))
                    dr.draw_board(SCREEN, board_size)
                    dr.draw_piece(SCREEN, board.board, board_size)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_pos = event.pos[0]
                    y_pos = event.pos[1]

                    col = int(math.floor(x_pos / dr.BLOCKSIZE))
                    row = int(math.floor(y_pos / dr.BLOCKSIZE))

                    # turn decision, if black(1)/white(-1) piece already placed, go back to the previous turn

                        # check if its a valid location then drop a piece
                    if board.step((row, col)):
                        dr.drop_piece(board.board, row, col, piece_1)
                        if chess_playing:
                            chess_click.play()
                        dr.draw_piece(SCREEN,board.board, board_size)

                        if board.result() == (True, 1):
                            SCREEN.blit(label_1, (480,50))
                            pygame.display.update()
                            game_over = True
                            pygame.mixer_music.stop()
                            pygame.time.wait(4000)
                            break
                        elif board.result() == (True, 0):
                            SCREEN.blit(label_3, (580, 50))
                            pygame.display.update()
                            game_over = True
                            pygame.mixer_music.stop()
                            pygame.time.wait(4000)
                            break
 
                    row, col = AI.take_action(board)
                    # Check if valid move
                    board.step((row, col))
                    dr.drop_piece(board.board, row, col, piece_2)
                    if chess_playing:
                            chess_click.play()
                    dr.draw_piece(SCREEN, board.board, board_size)

                    if board.result() == (True, -1):
                        SCREEN.blit(label_2, (480,50))
                        pygame.display.update()
                        game_over = True
                    elif board.result() == (True, 0):
                        SCREEN.blit(label_3, (580, 50))
                        pygame.display.update()
                        game_over = True

                if game_over:
                    pygame.mixer_music.stop()
                    pygame.time.wait(4000)

            frames_per_sec.tick(FPS)

def show_settings_menu(screen, board):
    global music_playing
    global chess_playing
    pause = True
    
    SURFACE = pygame.Surface((1280, 720)) 
    SURFACE.set_alpha(50)
    pygame.draw.rect(SURFACE, (128, 128, 128, 100), [0, 0, 1280, 720])
    screen.blit(SURFACE, (0, 0))

    # Settings menu buttons
    music_button = Button(image=None, pos=(640, 500), 
                          text_input="MUSIC", font=pygame.font.Font("go3v2.ttf", 60), 
                          base_color="White", hovering_color="Pink")

    sound_button = Button(image=None, pos=(640, 400), 
                           text_input="SOUND", font=pygame.font.Font("go3v2.ttf", 60), 
                           base_color="White", hovering_color="Pink")
        
        # Win condition button
    restart_button = Button(image=None, pos=(640, 300), 
                          text_input="RESTART", font=pygame.font.Font("go3v2.ttf", 60), 
                          base_color="White", hovering_color="Pink")
    
    while pause:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if music_button.checkForInput(mouse_pos):
                    if music_playing:
                        pygame.mixer_music.stop()
                        music_playing = False
                    else:
                        pygame.mixer_music.play(-1)
                        music_playing = True
                elif sound_button.checkForInput(mouse_pos):
                    chess_playing = not chess_playing
                elif restart_button.checkForInput(mouse_pos):
                    board.reset()
                    dr.draw_board(screen, Board.board_size)
                    
            
        for button in [music_button, restart_button, sound_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        pygame.display.update()

def play_background_music():
    global music_playing
    while music_playing:
        pygame.mixer.music.play(-1)
        pygame.time.delay(100)

if __name__ == '__main__':
    main()
