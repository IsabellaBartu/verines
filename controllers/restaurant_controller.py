import pygame

from views.restaurant_view import RestaurantView
from models.player import Player
from models.customer import Customer


class RestaurantController:

    def __init__(self):

        self.view = RestaurantView()

        self.player = Player()
        self.customer = Customer()

        self.go_to_kitchen = False
        self.go_to_recipe_book = False
        self.waiting_next_customer = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos

            if self.waiting_next_customer:

                if self.view.next_customer_button.collidepoint(mouse_pos):
                    self.customer.generate_customer()
                    self.customer.feedback = ""
                    self.waiting_next_customer = False

            else:

                if self.view.recipe_button.collidepoint(mouse_pos):
                    self.go_to_recipe_book = True

                elif self.view.prepare_button.collidepoint(mouse_pos):
                    self.go_to_kitchen = True

    def draw(self, screen):

        self.view.draw(
            screen,
            self.player,
            self.customer,
            self.waiting_next_customer
        )