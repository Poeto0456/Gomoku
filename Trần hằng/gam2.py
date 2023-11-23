import pygame
import sys
import pygame_gui
from Button import Button
from pygame.locals import *
from tkinter import *
import Start
from testsetting import get_font
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.mixer.music.load('main_menu_music.ogg')
        pygame.mixer.music.play(-1)
        pygame.init()
        self.GAME_W, self.GAME_H = 960,720
        self.game_canvas = pygame.Surface((self.GAME_W,self.GAME_H))
        self.screen = pygame.display.set_mode((960, 720), pygame.RESIZABLE)
        pygame.display.set_caption("Your Game Title")
        self.manager = pygame_gui.UIManager(self.screen.get_size())
        self.clock = pygame.time.Clock()
        self.bg = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.bg.fill((0, 0, 0))
        self.play_button = Button(image=None, pos=(640 * 3 // 4, 250 * 3 // 4),
                                text_input="PLAY", font=self.get_font(
                                    int(75 * 3 // 4 * self.screen.get_width() / 960)),
                                base_color="#d7fcd4", hovering_color="White")

        self.options_button = Button(image=None, pos=(640 * 3 // 4, 400 * 3 // 4),
                                    text_input="OPTIONS", font=self.get_font(
                                        int(75 * 3 // 4 * self.screen.get_width() / 960)),
                                    base_color="#d7fcd4", hovering_color="White")

        self.quit_button = Button(image=None, pos=(640 * 3 // 4, 550 * 3 // 4),
                                text_input="QUIT", font=self.get_font(
                                    int(75 * 3 // 4 * self.screen.get_width() / 960)),
                                base_color="#d7fcd4", hovering_color="White")
        self.resume_button = Button(image=None, pos=(640 * 3 // 4, 550 * 3 // 4),
                                text_input="RESUME", font=self.get_font(
                                    int(75 * 3 // 4 * self.screen.get_width() / 960)),
                                base_color="#d7fcd4", hovering_color="White"
        )
        self.ingame_options_button = Button(image=None, pos=(640 * 3 // 4, 400 * 3 // 4),
                                    text_input="OPTIONS", font=self.get_font(
                                        int(75 * 3 // 4 * self.screen.get_width() / 960)),
                                    base_color="#d7fcd4", hovering_color="White")
        
        self.ingame_quit_button = Button(image=None, pos=(640 * 3 // 4, 550 * 3 // 4),
                                text_input="QUIT", font=self.get_font(
                                    int(75 * 3 // 4 * self.screen.get_width() / 960)),
                                base_color="#d7fcd4", hovering_color="White")
        self.in_game_menu_buttons = [self.resume_button, self.ingame_options_button, self.ingame_quit_button]

    def get_font(self, size):
        return pygame.font.Font("font.ttf", size)

    def update_button_text_size(self, button, base_size):
            current_size = int(base_size * self.screen.get_width() / 960)
            button.font = self.get_font(current_size)

    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self.screen.blit(self.bg, (0, 0))
            # Handle events, update game logic, and draw UI
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.update_button_text_size(self.play_button, 75)
                    self.update_button_text_size(self.options_button, 75)
                    self.update_button_text_size(self.quit_button, 75)

            pygame.display.update()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                self.handle_resize(event)
            # Add other event handling as needed

    def play(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()

            self.screen.blit(self.bg, (0, 0))

            human_button = Button(image=None, pos=(640 * 3 // 4, 400 * 3 // 4),
                                  text_input="vs Human", font=self.get_font(60 * 3 // 4),
                                  base_color="White", hovering_color="Pink")

            ai_button = Button(image=None, pos=(640 * 3 // 4, 300 * 3 // 4),
                               text_input="vs AI", font=self.get_font(60 * 3 // 4),
                               base_color="White", hovering_color="Pink")

            back_button = Button(image=None, pos=(640 * 3 // 4, 600 * 3 // 4),
                                text_input="BACK", font=self.get_font(60 * 3 // 4),
                                base_color="White", hovering_color="Pink")
            setting_button = Button(pygame.image.load("cog_7712512.png"), pos = (1000,500),
                                    text_input = 'setting', font=self.get_font(60 * 3 // 4),
                                base_color="White", hovering_color="Pink")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if human_button.checkForInput(mouse_pos):
                        Start.main()
                    if ai_button.checkForInput(mouse_pos):
                        pass
                    if back_button.checkForInput(mouse_pos):
                        self.main_menu()
            for button in [human_button, ai_button, back_button, setting_button]:
                button.changeColor(mouse_pos)
                button.update(self.screen)
            pygame.display.update()

    def options(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()

            self.screen.blit(self.bg, (0, 0))

                # Board size button
            size_button = Button(image=None, pos=(640*3//4, 400*3//4), 
                            text_input="Board Size", font= get_font(60*3//4), 
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
                    button.changeColor(mouse_pos)
                    button.update(self.screen)

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if size_button.checkForInput(mouse_pos):
                            self.enter_boardsize()
                        if win_button.checkForInput(mouse_pos):
                            self.enter_wincondition()
                        if back_button.checkForInput(mouse_pos):
                            self.main_menu()

            pygame.display.update()

    def enter_boardsize(self):
        
        while True:
            mouse_pos = pygame.mouse.get_pos()

            self.screen.blit(self.bg, (0, 0))

            self.ui_refresh_rate = self.clock.tick(60) / 1000

            enter_text = self.get_font(45).render("Enter the board size", True, "White")
            enter_rect = enter_text.get_rect(center=(640,260))

            self.screen.blit(enter_text, enter_rect)

            back_button = Button(image=None, pos=(640,600),
                                text_input="BACK", font=self.get_font(60 * 3 // 4),
                                base_color="White", hovering_color="Pink")

            back_button.changeColor(mouse_pos)
            back_button.update(self.screen)
    def enter_wincondition(self):
        while True:
            win_mouse_pos = pygame.mouse.get_pos()

            self.screen.blit(self.bg, (0, 0))

            enter_text = self.get_font(45).render("Enter the win condition", True, "White")
            enter_rect = enter_text.get_rect(center=(640 * 3 // 4, 260 * 3 // 4))
            self.screen.blit(enter_text, enter_rect)

            back_button = Button(image=None, pos=(640 * 3 // 4, 600 * 3 // 4),
                                text_input="BACK", font=self.get_font(60),
                                base_color="White", hovering_color="Pink")

            back_button.changeColor(win_mouse_pos)
            back_button.update(self.screen)  # Move this line outside of the event loop

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.checkForInput(win_mouse_pos):
                        self.options()

            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#main_text_entry'):
                Start.board_size = int(event.text)
                self.options()
            self.manager.process_events(event)
            ui_refresh_rate = self.clock.tick(60 * 3 // 4) / 1000
            self.manager.update(ui_refresh_rate)

            self.manager.draw_ui(self.screen)

            pygame.display.update()


    def resizable_loop(self):
        full_screen = False
        while True:
            self.screen.fill((0, 0, 50))
            pygame.draw.rect(self.screen, (255, 0, 0),
                            pygame.Rect(self.screen.get_width() - 5 - (self.screen.get_width() / 5), 50,
                                        self.screen.get_width() / 5, 50))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == VIDEORESIZE:
                    if not full_screen:
                        self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
            self.clock.tick(60)

    
    def in_game(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()

            self.screen.blit(self.bg, (0, 0))

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == VIDEORESIZE:
                    self.handle_resize(event)

            # Draw your in-game content

            # Check if the user wants to open the in-game menu
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                self.handle_in_game_menu()  # Open the in-game menu

            pygame.display.update()
            self.clock.tick(60)
if __name__ == "__main__":
    # This block is executed only if the script is run directly (not imported)
    game_instance = Game()
    game_instance.run()
    def main_menu(self):
        while True:
            pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

            pygame.init()

            pygame.mixer.init()

            pygame.mixer.music.load('main_menu_music.ogg')

            pygame.mixer.music.play(-1)
            self.screen.blit(self.bg, (0, 0))

            menu_mouse_pos = pygame.mouse.get_pos()
            self.handle_events()    

            # Adjust the size of the menu text based on the screen width
            menu_text = self.get_font(int(100 * 3 // 4 * self.screen.get_width() / 960)).render(
                "MAIN MENU", True, "#b68f40")
            menu_rect = menu_text.get_rect(center=(self.screen.get_width() // 4, self.screen.get_height() // 4))

            # Calculate button positions based on the screen size
            button_y = self.screen.get_height() // 2

            play_button = Button(image=pygame.image.load("Play Rect.png"),
                                pos=(self.screen.get_width() // 2, button_y),
                                text_input="PLAY",
                                font=self.get_font(int(75 * 3 // 4 * self.screen.get_width() / 960)),
                                base_color="#d7fcd4", hovering_color="White")

            options_button = Button(image=pygame.image.load("Options Rect.png"),
                                    pos=(self.screen.get_width() // 2, button_y + 150),
                                    text_input="OPTIONS",
                                    font=self.get_font(int(75 * 3 // 4 * self.screen.get_width() / 960)),
                                    base_color="#d7fcd4", hovering_color="White")

            quit_button = Button(image=pygame.image.load("Quit Rect.png"),
                                pos=(self.screen.get_width() // 2, button_y ),
                                text_input="QUIT",
                                font=self.get_font(int(75 * 3 // 4 * self.screen.get_width() / 960)),
                                base_color="#d7fcd4", hovering_color="White")
            
            # Update button positions when the screen is resized
            play_button.update_position((self.screen.get_width() // 2, button_y))
            options_button.update_position((self.screen.get_width() // 2, button_y + 300))
            quit_button.update_position((self.screen.get_width() // 2, button_y + 300))

            self.screen.blit(menu_text, menu_rect)

            for button in [play_button, options_button, quit_button]:
                button.changeColor(menu_mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_pos):
                        self.play()
                    if options_button.checkForInput(menu_mouse_pos):
                        self.options()
                    if quit_button.checkForInput(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        pygame.mixer.music.fadeout(1000)

            self.resizable_loop()  # Call resizable_loop in the event loop
            pygame.display.update()


        
