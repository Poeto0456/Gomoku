import pygame
import sys
from Button import Button
from Game import Game
from pygame.locals import *
from tkinter import *
def main_menu(self):
        while True:
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

            self.resizable_loop()  # Call resizable_loop in the event loop
            pygame.display.update()

# Create an instance of the Game class and run the game
game_instance = Game()
game_instance.main_menu()