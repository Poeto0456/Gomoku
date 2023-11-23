import pygame
from pygame.locals import *

class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        super().__init__()
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.font = font
        self.font = pygame.font.Font('font.ttf', 45)
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
