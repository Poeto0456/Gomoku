import pygame, sys, pygame_gui
from Button import Button
import numpy as np
import Board
from pygame.locals import *
import Start

pygame.init()
SCREEN_SIZE = (960, 540)
SCREEN = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
icon_image = pygame.image.load("3.jpg")

# Set the window icon
pygame.display.set_icon(icon_image)

# Load resources
BG = pygame.image.load("Background.png")

# Set up pygame_gui
manager = pygame_gui.UIManager(SCREEN_SIZE)

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((580*3//4, 360*3//4), (100*3//4, 50*3//4)), manager=manager,
                                               object_id='#main_text_entry')

clock = pygame.time.Clock()

def toggle_audio(audio, playing, button, icon_playing, icon_paused):
    if playing:
        audio.stop()
        button.image = icon_paused
    else:
        audio.play(-1)
        button.image = icon_playing
    return not playing

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        Human_button = Button(image=None, pos=(640*3//4, 400*3//4), 
                           text_input="vs Human", font=get_font(60*3//4), 
                           base_color="White", hovering_color="Pink")
        
        # Win condition button
        AI_button = Button(image=None, pos=(640*3//4, 300*3//4), 
                          text_input="vs AI", font=get_font(60*3//4), 
                          base_color="White", hovering_color="Pink")

        back_button = Button(image=None, pos=(640*3//4, 600*3//4), 
                            text_input="BACK", font=get_font(60*3//4), 
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
        size_button = Button(image=None, pos=(640*3//4, 400*3//4), 
                           text_input="Board Size", font=get_font(60*3//4), 
                           base_color="White", hovering_color="Pink")
        
        # Win condition button
        win_button = Button(image=None, pos=(640*3//4, 300*3//4), 
                          text_input="Win Condition", font=get_font(60*3//4), 
                          base_color="White", hovering_color="Pink")

        # Back button                   
        back_button = Button(image=None, pos=(640*3//4, 600*3//4), 
                            text_input="BACK", font=get_font(60*3//4), 
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

        UI_REFRESH_RATE = clock.tick(60*3//4)/1000

        ENTER_TEXT = get_font(int(45*3//4 * SCREEN.get_width() / 960)).render("Enter the board size", True, "White")
        ENTER_RECT = ENTER_TEXT.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2))
        SCREEN.blit(ENTER_TEXT, ENTER_RECT)

        back_button = Button(image=None, pos=(640*3//4, 600*3//4), 
                            text_input="BACK", font=get_font(60*3//4), 
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
                Start.board_size = int(event.text)
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
        ENTER_RECT = ENTER_TEXT.get_rect(center=(640*3//4, 260*3//4))
        SCREEN.blit(ENTER_TEXT, ENTER_RECT)

        back_button = Button(image=None, pos=(640*3//4, 600*3//4), 
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
def resizable_loop():
    full_screen = False
    while True:
        SCREEN.fill((0, 0, 50))
        pygame.draw.rect(SCREEN, (255, 0, 0), pygame.Rect(SCREEN.get_width() - 5 - (SCREEN.get_width() / 5), 50, SCREEN.get_width() / 5, 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == VIDEORESIZE:
                if not full_screen:
                    SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)
def main_menu():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer_music.load('main_menu_music.ogg')
    pygame.mixer_music.play(-1)
    pygame.mixer_music.set_volume(0.5)
    sound_click=pygame.mixer.Sound("click_sound.ogg")
    music_playing = True
    sound_playing = True
    last_sound_play_time = pygame.time.get_ticks()
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100*3//4).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640*3//4, 100*3//4))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640*3//4, 250*3//4), 
                            text_input="PLAY", font=get_font(75*3//4), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640*3//4, 400*3//4), 
                            text_input="OPTIONS", font=get_font(75*3//4), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640*3//4, 550*3//4), 
                            text_input="QUIT", font=get_font(75*3//4), base_color="#d7fcd4", hovering_color="White")
        music_icon_playing = pygame.image.load('music_on.png')
        music_icon_playing = pygame.transform.scale(music_icon_playing,(20,20))
        music_icon_paused = pygame.image.load('mute_music.png')
        music_icon_paused = pygame.transform.scale(music_icon_paused,(20,20))
        music_button_icon = music_icon_playing if music_playing else music_icon_paused
        music_button = Button(image=music_button_icon, pos=(800,150),
                              text_input=None, font=get_font(75 * 3 // 4), base_color="#d7fcd4",
                              hovering_color="White") 
        sound_icon_playing = pygame.image.load('sound_on.png')
        sound_icon_playing = pygame.transform.scale(sound_icon_playing,(20,20))
        sound_icon_paused = pygame.image.load('mute_sound.png')
        sound_icon_paused = pygame.transform.scale(sound_icon_paused,(20,20))
        sound_button_icon = sound_icon_playing if sound_playing else sound_icon_paused
        sound_button = Button(image=sound_button_icon, pos=(800,200),
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
                if sound_playing:
                    sound_click.play()
                if sound_button.checkForInput(MENU_MOUSE_POS):
                    if sound_playing:
                        sound_click.stop()
                        sound_button.image = sound_icon_paused
                    else:
                        sound_click.play()
                        sound_button.image = sound_icon_playing
                    sound_playing = not sound_playing
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer_music.stop()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer_music.stop()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer_music.stop()
                    pygame.quit()
                    sys.exit()
                if music_button.checkForInput(MENU_MOUSE_POS):
                    if music_playing:
                        pygame.mixer_music.stop()
                        music_button.image = music_icon_paused
                    else:
                        pygame.mixer_music.play(-1)
                        music_button.image = music_icon_playing
                    music_playing = not music_playing
                
        resizable_loop
        pygame.display.update()

main_menu()
