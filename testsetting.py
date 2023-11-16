import pygame, sys, pygame_gui
from Button import Button
import numpy as np
import Board
from pygame.locals import *
import Start

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Background.png")
manager = pygame_gui.UIManager((1280, 720))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((580, 360), (100, 50)), manager=manager,
                                               object_id='#main_text_entry')

clock = pygame.time.Clock()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        Human_button = Button(image=None, pos=(640, 400), 
                           text_input="vs Human", font=get_font(60), 
                           base_color="White", hovering_color="Pink")
        
        # Win condition button
        AI_button = Button(image=None, pos=(640, 300), 
                          text_input="vs AI", font=get_font(60), 
                          base_color="White", hovering_color="Pink")

        back_button = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(60), 
                            base_color="White", hovering_color="Pink")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Human_button.checkForInput(PLAY_MOUSE_POS):
                    Start.main()
                if AI_button.checkForInput(PLAY_MOUSE_POS):
                    pass
                if back_button.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        for button in [Human_button, AI_button, back_button]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)    

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        # Board size button
        size_button = Button(image=None, pos=(640, 400), 
                           text_input="Board Size", font=get_font(60), 
                           base_color="White", hovering_color="Pink")
        
        # Win condition button
        win_button = Button(image=None, pos=(640, 300), 
                          text_input="Win Condition", font=get_font(60), 
                          base_color="White", hovering_color="Pink")

        # Back button                   
        back_button = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(60), 
                            base_color="White", hovering_color="Pink")

        for button in [size_button, win_button, back_button]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)          

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if size_button.checkForInput(OPTIONS_MOUSE_POS):
                    enter_boardsize()
                if win_button.checkForInput(OPTIONS_MOUSE_POS):
                    enter_wincondition()
                if back_button.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()              
        
        pygame.display.update()

def enter_boardsize():
    while True:
        BOARD_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))   

        UI_REFRESH_RATE = clock.tick(60)/1000

        ENTER_TEXT = get_font(45).render("Enter the board size", True, "White")
        ENTER_RECT = ENTER_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(ENTER_TEXT, ENTER_RECT)

        back_button = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(60), 
                            base_color="White", hovering_color="Pink")

        back_button.changeColor(BOARD_MOUSE_POS)
        back_button.update(SCREEN)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(BOARD_MOUSE_POS):
                    options()  
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                Board.COL_COUNT = int(event.text)
                Board.ROW_COUNT = int(event.text)
                options()
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        manager.draw_ui(SCREEN)

        pygame.display.update()

def enter_wincondition():
    while True:
        WIN_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))    

        ENTER_TEXT = get_font(45).render("Enter the win condition", True, "White")
        ENTER_RECT = ENTER_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(ENTER_TEXT, ENTER_RECT)

        back_button = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(60), 
                            base_color="White", hovering_color="Pink")
        
        back_button.changeColor(WIN_MOUSE_POS)
        back_button.update(SCREEN)  

        win = ""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(WIN_MOUSE_POS):
                    options()              
        
        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()