import pygame, sys, pygame_gui
from Game.Button import Button
from pygame.locals import *
import Game.Start as Start
import Game.Board as Board
import sys

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
icon_image = pygame.image.load("Image/icon.png")
pygame.display.set_icon(icon_image)

BG = pygame.image.load("Image/Background.jpg")

clock = pygame.time.Clock()

# Các biến trạng thái âm thanh
music_playing = True
sound_playing = True
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer_music.load('Sound/mainmenu.mp3')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(1)
sound_click=pygame.mixer.Sound("Sound/click_sound.wav")

def get_font(size): 
    return pygame.font.Font("Font/go3v2.ttf", size)

def play():
    global sound_playing
    while True:      
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        Human_button = Button(image=None, pos=(640, 400), 
                           text_input="vs Human", font=get_font(70), 
                           base_color="White", hovering_color="Pink")

        AI_button = Button(image=None, pos=(640, 300), 
                          text_input="vs AI", font=get_font(70), 
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
                    if sound_playing:
                        sound_click.play()
                    Start.AI_value = 0
                    Start.main()
                if AI_button.checkForInput(PLAY_MOUSE_POS):
                    if sound_playing:
                        sound_click.play()
                    Start.AI_value = 1
                    Start.main()
                if back_button.checkForInput(PLAY_MOUSE_POS):
                    if sound_playing:
                        sound_click.play()
                    main_menu()

        for button in [Human_button, AI_button, back_button]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)    

        pygame.display.update()
    
def options():
    global sound_playing
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
                    if sound_playing:
                        sound_click.play()
                    enter_boardsize()
                if win_button.checkForInput(OPTIONS_MOUSE_POS):
                    if sound_playing:
                        sound_click.play()
                    enter_wincondition()
                if back_button.checkForInput(OPTIONS_MOUSE_POS):
                    if sound_playing:
                        sound_click.play()
                    main_menu()              
        
        pygame.display.update()

def enter_boardsize():
    manager = pygame_gui.UIManager((1280, 720))

    text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((580, 360), (100, 50)), manager=manager,
                                               object_id='#main_text_entry')
    while True:
        BOARD_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))   

        UI_REFRESH_RATE = clock.tick(60)/1000

        ENTER_TEXT = get_font(65).render("Enter the board size", True, "White")
        ENTER_RECT = ENTER_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(ENTER_TEXT, ENTER_RECT)

        back_button = Button(image=None, pos=(630, 600), 
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
                    if sound_playing:
                        sound_click.play()
                    options()  
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                if sound_playing:
                    sound_click.play()
                Board.board_size = int(event.text)
                options()
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        manager.draw_ui(SCREEN)

        pygame.display.update()

def enter_wincondition():
    manager = pygame_gui.UIManager((1280, 720))

    win_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((580, 360), (100, 50)), manager=manager,
                                               object_id='#main_text_entry')
    while True:
        WIN_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))   

        UI_REFRESH_RATE = clock.tick(60)/1000 

        ENTER_TEXT = get_font(65).render("Enter the win condition", True, "White")
        ENTER_RECT = ENTER_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(ENTER_TEXT, ENTER_RECT)

        back_button = Button(image=None, pos=(630, 600), 
                            text_input="BACK", font=get_font(60), 
                            base_color="White", hovering_color="Pink")
        
        back_button.changeColor(WIN_MOUSE_POS)
        back_button.update(SCREEN)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(WIN_MOUSE_POS):
                    if sound_playing:
                        sound_click.play()
                    options()  
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                if sound_playing:
                    sound_click.play()
                Board.n_in_a_row = int(event.text)
                Board.o_win = int(event.text)
                Board.x_win = -int(event.text)
                options()
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        manager.draw_ui(SCREEN)

        pygame.display.update()            

def main_menu():
    pygame.mixer_music.load('Sound/mainmenu.mp3')
    global music_playing
    global sound_playing
    if music_playing:
        pygame.mixer_music.play(-1)
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(140).render("MAIN MENU", True, "LightBlue")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Image/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(100), base_color="White", hovering_color="Pink")
        OPTIONS_BUTTON = Button(image=pygame.image.load("image/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(100), base_color="White", hovering_color="Pink")
        QUIT_BUTTON = Button(image=pygame.image.load("Image/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(100), base_color="White", hovering_color="Pink")

        music_icon_playing = pygame.image.load('Image/music_on.png')
        music_icon_playing = pygame.transform.scale(music_icon_playing,(50,50))
        music_icon_paused = pygame.image.load('Image/mute_music.png')
        music_icon_paused = pygame.transform.scale(music_icon_paused,(50,50))
        music_button_icon = music_icon_playing if music_playing else music_icon_paused
        music_button = Button(image=music_button_icon, pos=(1200, 50),
                              text_input=None, font=get_font(60), base_color="#d7fcd4",
                              hovering_color="White") 
        
        sound_icon_playing = pygame.image.load('Image/sound_on.png')
        sound_icon_playing = pygame.transform.scale(sound_icon_playing,(50,50))
        sound_icon_paused = pygame.image.load('Image/mute_sound.png')
        sound_icon_paused = pygame.transform.scale(sound_icon_paused,(50,50))
        sound_button_icon = sound_icon_playing if sound_playing else sound_icon_paused
        sound_button = Button(image=sound_button_icon, pos=(1200,120),
                              text_input=None, font=get_font(75 * 3 // 4), base_color="#d7fcd4",
                              hovering_color="White") 

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, music_button, sound_button]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sound_button.checkForInput(MENU_MOUSE_POS):
                    if sound_playing:
                        sound_button.image = sound_icon_paused
                    else:
                        sound_button.image = sound_icon_playing
                    sound_playing = not sound_playing
                if music_button.checkForInput(MENU_MOUSE_POS):
                    if music_playing:
                        pygame.mixer_music.stop()
                        music_button.image = music_icon_paused
                    else:
                        pygame.mixer_music.play(-1)
                        music_button.image = music_icon_playing
                    music_playing = not music_playing
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if sound_playing:
                        sound_click.play()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if sound_playing:
                        sound_click.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if sound_playing:
                        sound_click.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
