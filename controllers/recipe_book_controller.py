import pygame

from views.recipe_book_view import RecipeBookView


class RecipeBookController:

    def __init__(self):

        self.view = RecipeBookView()

        self.back_to_restaurant = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos

            if self.view.back_button.collidepoint(mouse_pos):

                self.back_to_restaurant = True

    def draw(self, screen):

        self.view.draw(screen)