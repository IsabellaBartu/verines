import pygame
import math
from settings import *


class KitchenView:

    def __init__(self):
        self.title_font = pygame.font.SysFont("arial", 42, bold=True)
        self.text_font = pygame.font.SysFont("arial", 28)
        self.small_font = pygame.font.SysFont("arial", 22)

        self.pizza_center = (640, 370)
        self.pizza_radius = 180

        self.deliver_button = pygame.Rect(520, 620, 240, 60)

    def draw_pizza_slice_highlight(self, screen, slice_index):
        center_x, center_y = self.pizza_center

        points = [self.pizza_center]

        for angle in range(slice_index * 90, (slice_index + 1) * 90 + 1, 4):
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * (self.pizza_radius - 10)
            y = center_y + math.sin(rad) * (self.pizza_radius - 10)
            points.append((x, y))

        pygame.draw.polygon(screen, (255, 235, 150), points)

    def draw_pizza(self, screen, selected_slices):
        center_x, center_y = self.pizza_center

        # sombra
        pygame.draw.circle(screen, (90, 60, 45), (center_x + 8, center_y + 10), self.pizza_radius)

        # borda/massa
        pygame.draw.circle(screen, (214, 150, 80), self.pizza_center, self.pizza_radius)

        # molho
        pygame.draw.circle(screen, (180, 55, 40), self.pizza_center, self.pizza_radius - 22)

        # queijo
        pygame.draw.circle(screen, (245, 210, 105), self.pizza_center, self.pizza_radius - 38)

        # fatias selecionadas
        for i in range(selected_slices):
            self.draw_pizza_slice_highlight(screen, i)

        # pepperonis
        pepperonis = [
            (560, 300), (650, 285), (720, 335),
            (585, 410), (680, 430), (760, 390),
            (610, 355), (705, 485)
        ]

        for pos in pepperonis:
            pygame.draw.circle(screen, (150, 45, 35), pos, 18)
            pygame.draw.circle(screen, (110, 30, 25), pos, 18, 3)

        # linhas das fatias
        for angle in [0, 90, 180, 270]:
            rad = math.radians(angle)
            end_x = center_x + math.cos(rad) * self.pizza_radius
            end_y = center_y + math.sin(rad) * self.pizza_radius

            pygame.draw.line(screen, BROWN, self.pizza_center, (end_x, end_y), 5)

        # contorno
        pygame.draw.circle(screen, BROWN, self.pizza_center, self.pizza_radius, 6)

    def draw_panel(self, screen):
        panel = pygame.Rect(30, 95, 420, 130)

        pygame.draw.rect(screen, BACKGROUND_COLOR, panel, border_radius=18)
        pygame.draw.rect(screen, BROWN, panel, 4, border_radius=18)

        instruction = self.text_font.render(
            "Pedido: sirva metade da pizza.",
            True,
            DARK_BROWN
        )

        hint = self.small_font.render(
            "Dica: metade de 4 fatias = 2 fatias.",
            True,
            BROWN
        )

        screen.blit(instruction, (55, 125))
        screen.blit(hint, (55, 170))

    def draw_counter(self, screen, selected_slices):
        counter_box = pygame.Rect(480, 105, 300, 70)

        pygame.draw.rect(screen, BACKGROUND_COLOR, counter_box, border_radius=15)
        pygame.draw.rect(screen, BROWN, counter_box, 4, border_radius=15)

        counter = self.text_font.render(
            f"Selecionadas: {selected_slices}/4",
            True,
            DARK_BROWN
        )

        screen.blit(
            counter,
            (
                counter_box.centerx - counter.get_width() // 2,
                counter_box.centery - counter.get_height() // 2
            )
        )

    def draw_deliver_button(self, screen):
        pygame.draw.rect(screen, YELLOW, self.deliver_button, border_radius=15)
        pygame.draw.rect(screen, BROWN, self.deliver_button, 4, border_radius=15)

        deliver_text = self.text_font.render("ENTREGAR", True, BROWN)

        screen.blit(
            deliver_text,
            (
                self.deliver_button.centerx - deliver_text.get_width() // 2,
                self.deliver_button.centery - deliver_text.get_height() // 2
            )
        )

    def draw(self, screen, selected_slices):
        screen.fill(RESTAURANT_BG)

        title = self.title_font.render("COZINHA - PIZZA VERINE", True, BROWN)
        screen.blit(title, (40, 30))

        self.draw_panel(screen)
        self.draw_counter(screen, selected_slices)
        self.draw_pizza(screen, selected_slices)
        self.draw_deliver_button(screen)