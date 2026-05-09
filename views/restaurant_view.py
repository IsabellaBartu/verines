import pygame
import math

from settings import *


class RestaurantView:

    def __init__(self):

        self.title_font = pygame.font.SysFont("arial", 42, bold=True)

        self.text_font = pygame.font.SysFont("arial", 28)

        self.prepare_button = pygame.Rect(930, 600, 260, 70)

        self.next_customer_button = pygame.Rect(930, 600, 260, 70)

        self.recipe_button = pygame.Rect(640, 600, 250, 70)

        self.animation_timer = 0

    def draw_floor(self, screen):

        tile_size = 80

        colors = [
            (210, 180, 140),
            (190, 160, 120)
        ]

        for row in range(10):

            for col in range(16):

                color = colors[(row + col) % 2]

                pygame.draw.rect(
                    screen,
                    color,
                    (
                        col * tile_size,
                        row * tile_size,
                        tile_size,
                        tile_size
                    )
                )

    def draw_tables(self, screen):

        table_positions = [
            (500, 230),
            (850, 230)
        ]

        for x, y in table_positions:

            pygame.draw.circle(
                screen,
                (120, 70, 50),
                (x, y),
                70
            )

            pygame.draw.circle(
                screen,
                (150, 100, 70),
                (x, y),
                60
            )

    def draw_counter(self, screen):

        pygame.draw.rect(
            screen,
            (120, 70, 50),
            (0, 520, WIDTH, 200)
        )

        pygame.draw.rect(
            screen,
            (150, 100, 70),
            (0, 520, WIDTH, 20)
        )

    def draw_window(self, screen):

        pygame.draw.rect(
            screen,
            (180, 220, 255),
            (930, 60, 250, 140),
            border_radius=15
        )

        pygame.draw.rect(
            screen,
            BROWN,
            (930, 60, 250, 140),
            5,
            border_radius=15
        )

        pygame.draw.line(
            screen,
            BROWN,
            (1055, 60),
            (1055, 200),
            4
        )

        pygame.draw.line(
            screen,
            BROWN,
            (930, 130),
            (1180, 130),
            4
        )

    def draw_lights(self, screen):

        pygame.draw.circle(
            screen,
            (255, 220, 120),
            (250, 80),
            40
        )

        pygame.draw.circle(
            screen,
            (255, 220, 120),
            (650, 80),
            40
        )

    def draw_customer(self, screen):

        self.animation_timer += 0.05

        breathing_offset = math.sin(
            self.animation_timer
        ) * 6

        y_position = 420 + breathing_offset

        # Cabeça
        pygame.draw.circle(
            screen,
            (240, 220, 190),
            (220, int(y_position)),
            60
        )

        # Corpo
        pygame.draw.rect(
            screen,
            (120, 70, 50),
            (
                170,
                int(y_position + 60),
                100,
                140
            ),
            border_radius=20
        )

    def draw_dialogue(self, screen, customer):

        dialogue_box = pygame.Rect(350, 330, 700, 180)

        pygame.draw.rect(
            screen,
            BACKGROUND_COLOR,
            dialogue_box,
            border_radius=20
        )

        pygame.draw.rect(
            screen,
            BROWN,
            dialogue_box,
            4,
            border_radius=20
        )

        customer_name = self.text_font.render(
            customer.name,
            True,
            BROWN
        )

        order_text = self.text_font.render(
            customer.order,
            True,
            DARK_BROWN
        )

        feedback_text = self.text_font.render(
            customer.feedback,
            True,
            RED
        )

        screen.blit(customer_name, (380, 350))

        screen.blit(order_text, (380, 410))

        screen.blit(feedback_text, (380, 470))

    def draw_hud(self, screen, player):

        title = self.title_font.render(
            "VERINE'S RESTAURANTE",
            True,
            BROWN
        )

        money_text = self.text_font.render(
            f"Dinheiro: R$ {player.money}",
            True,
            DARK_BROWN
        )

        reputation_text = self.text_font.render(
            f"Reputação: {'★' * player.reputation}",
            True,
            DARK_BROWN
        )

        day_text = self.text_font.render(
            f"Dia {player.day}",
            True,
            DARK_BROWN
        )

        screen.blit(title, (40, 20))

        screen.blit(money_text, (40, 90))

        screen.blit(reputation_text, (40, 130))

        screen.blit(day_text, (40, 170))

    def draw_button(self, screen, rect, text):

        mouse_pos = pygame.mouse.get_pos()

        color = YELLOW

        if rect.collidepoint(mouse_pos):

            color = (255, 230, 140)

        pygame.draw.rect(
            screen,
            color,
            rect,
            border_radius=15
        )

        pygame.draw.rect(
            screen,
            BROWN,
            rect,
            4,
            border_radius=15
        )

        button_text = self.text_font.render(
            text,
            True,
            BROWN
        )

        screen.blit(
            button_text,
            (
                rect.centerx - button_text.get_width() // 2,
                rect.centery - button_text.get_height() // 2
            )
        )

    def draw(self, screen, player, customer, waiting_next_customer):

        self.draw_floor(screen)

        self.draw_window(screen)

        self.draw_lights(screen)

        self.draw_tables(screen)

        self.draw_counter(screen)

        self.draw_customer(screen)

        self.draw_dialogue(screen, customer)

        self.draw_hud(screen, player)

        self.draw_button(
            screen,
            self.recipe_button,
            "LIVRO DE RECEITAS"
        )

        if waiting_next_customer:

            self.draw_button(
                screen,
                self.next_customer_button,
                "PRÓXIMO CLIENTE"
            )

        else:

            self.draw_button(
                screen,
                self.prepare_button,
                "PREPARAR PEDIDO"
            )