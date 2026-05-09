import pygame
import math

from views.kitchen_view import KitchenView


class KitchenController:

    def __init__(self):

        self.view = KitchenView()

        self.selected_slices = 0

        self.correct_slices = 0

        self.finished = False

        self.success = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos

            # Clique na pizza
            center_x, center_y = self.view.pizza_center

            dx = mouse_pos[0] - center_x

            dy = mouse_pos[1] - center_y

            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance <= self.view.pizza_radius:

                if self.selected_slices < 4:

                    self.selected_slices += 1

            # Botão entregar
            if self.view.deliver_button.collidepoint(mouse_pos):

                self.finished = True

                self.success = self.selected_slices == self.correct_slices

    def draw(self, screen):

        self.view.draw(screen, self.selected_slices)

    def reset(self):

        self.selected_slices = 0

        self.finished = False

        self.success = False