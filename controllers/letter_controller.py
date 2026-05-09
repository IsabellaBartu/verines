import pygame

from views.letter_view import LetterView


class LetterController:

    def __init__(self):

        self.view = LetterView()

        self.back_to_restaurant = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos

            if self.view.continue_button.collidepoint(mouse_pos):

                self.back_to_restaurant = True

    def draw(self, screen):

        self.view.draw(screen)