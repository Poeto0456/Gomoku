# main_menu.py
import pygame
import sys
from pygame.locals import *
from Button import Button
from gam2 import Game  # Assuming your Game class is in game.py
import pygame_gui
def main_menu():
    pygame.init()
    GAME_W, GAME_H = 960, 720
    screen = pygame.display.set_mode((960, 720), pygame.RESIZABLE)
    pygame.display.set_caption("Your Game Title")
    manager = pygame_gui.UIManager(screen.get_size())
    clock = pygame.time.Clock()
    bg = pygame.Surface((screen.get_width(), screen.get_height()))
    bg.fill((0, 0, 0))
    def get_font(size):
        return pygame.font.Font("font.ttf", size)
    while True:
        menu_mouse_pos = pygame.mouse.get_pos()

        screen.blit(bg, (0, 0))

        # Adjust the size of the menu text based on the screen width
        menu_text = get_font(int(100 * 3 // 4 * screen.get_width() / 960)).render(
            "MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(screen.get_width() // 4, screen.get_height() // 4))

        # Calculate button positions based on the screen size
        button_y = screen.get_height() // 2

        play_button = Button(image=pygame.image.load("Play Rect.png"),
                             pos=(screen.get_width() // 2, button_y),
                             text_input="PLAY",
                             font=get_font(int(75 * 3 // 4 * screen.get_width() / 960)),
                             base_color="#d7fcd4", hovering_color="White")

        options_button = Button(image=pygame.image.load("Options Rect.png"),
                                pos=(screen.get_width() // 2, button_y + 150),
                                text_input="OPTIONS",
                                font=get_font(int(75 * 3 // 4 * screen.get_width() / 960)),
                                base_color="#d7fcd4", hovering_color="White")

        quit_button = Button(image=pygame.image.load("Quit Rect.png"),
                             pos=(screen.get_width() // 2, button_y),
                             text_input="QUIT",
                             font=get_font(int(75 * 3 // 4 * screen.get_width() / 960)),
                             base_color="#d7fcd4", hovering_color="White")

        # Update button positions when the screen is resized
        play_button.update_position((screen.get_width() // 2, button_y))
        options_button.update_position((screen.get_width() // 2, button_y + 300))
        quit_button.update_position((screen.get_width() // 2, button_y + 300))

        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    game_instance = Game()
                    game_instance.run()
                if options_button.checkForInput(menu_mouse_pos):
                    game_instance.options
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
