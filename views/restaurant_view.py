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
        self.light_timer = 0
        self.rain_timer = 0

    def get_time_of_day(self, player):
        if player.day % 3 == 1:
            return "day"
        elif player.day % 3 == 2:
            return "afternoon"
        else:
            return "night"

    def draw_floor(self, screen):
        tile_size = 80
        colors = [(210, 180, 140), (190, 160, 120)]

        for row in range(10):
            for col in range(16):
                color = colors[(row + col) % 2]
                pygame.draw.rect(
                    screen,
                    color,
                    (col * tile_size, row * tile_size, tile_size, tile_size)
                )

    def draw_tables(self, screen):
        for x, y in [(500, 230), (850, 230)]:
            pygame.draw.circle(screen, (120, 70, 50), (x, y), 70)
            pygame.draw.circle(screen, (150, 100, 70), (x, y), 60)

    def draw_counter(self, screen):
        pygame.draw.rect(screen, (120, 70, 50), (0, 520, WIDTH, 200))
        pygame.draw.rect(screen, (150, 100, 70), (0, 520, WIDTH, 20))

    def draw_window(self, screen, time_of_day):
        if time_of_day == "day":
            window_color = (180, 220, 255)
        elif time_of_day == "afternoon":
            window_color = (245, 160, 90)
        else:
            window_color = (45, 60, 110)

        pygame.draw.rect(
            screen,
            window_color,
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

        pygame.draw.line(screen, BROWN, (1055, 60), (1055, 200), 4)
        pygame.draw.line(screen, BROWN, (930, 130), (1180, 130), 4)

        # Chuva aparece à noite
        if time_of_day == "night":
            self.draw_rain(screen)

    def draw_rain(self, screen):
        self.rain_timer += 4

        for i in range(12):
            x = 945 + i * 20
            y = 65 + ((self.rain_timer + i * 25) % 140)

            pygame.draw.line(
                screen,
                (170, 200, 255),
                (x, y),
                (x - 8, y + 18),
                2
            )

    def draw_lights(self, screen):
        self.light_timer += 0.03

        glow = math.sin(self.light_timer) * 15
        radius = int(40 + glow)

        for pos in [(250, 80), (650, 80)]:
            pygame.draw.circle(screen, (255, 220, 120), pos, radius)
            pygame.draw.circle(screen, (255, 240, 180), pos, radius // 2)

    def draw_customer(self, screen):
        self.animation_timer += 0.05

        breathing_offset = math.sin(self.animation_timer) * 6
        y_position = 420 + breathing_offset

        pygame.draw.circle(
            screen,
            (240, 220, 190),
            (220, int(y_position)),
            60
        )

        pygame.draw.rect(
            screen,
            (120, 70, 50),
            (170, int(y_position + 60), 100, 140),
            border_radius=20
        )

    def draw_dialogue(self, screen, customer):
        dialogue_box = pygame.Rect(350, 330, 700, 180)

        pygame.draw.rect(screen, BACKGROUND_COLOR, dialogue_box, border_radius=20)
        pygame.draw.rect(screen, BROWN, dialogue_box, 4, border_radius=20)

        customer_name = self.text_font.render(customer.name, True, BROWN)
        order_text = self.text_font.render(customer.order, True, DARK_BROWN)
        feedback_text = self.text_font.render(customer.feedback, True, RED)

        screen.blit(customer_name, (380, 350))
        screen.blit(order_text, (380, 410))
        screen.blit(feedback_text, (380, 470))

    def draw_hud(self, screen, player):
        title = self.title_font.render("VERINE'S RESTAURANTE", True, BROWN)
        money_text = self.text_font.render(f"Dinheiro: R$ {player.money}", True, DARK_BROWN)
        reputation_text = self.text_font.render(f"Reputação: {'★' * player.reputation}", True, DARK_BROWN)
        day_text = self.text_font.render(f"Dia {player.day}", True, DARK_BROWN)

        screen.blit(title, (40, 20))
        screen.blit(money_text, (40, 90))
        screen.blit(reputation_text, (40, 130))
        screen.blit(day_text, (40, 170))

    def draw_button(self, screen, rect, text):
        mouse_pos = pygame.mouse.get_pos()
        color = (255, 230, 140) if rect.collidepoint(mouse_pos) else YELLOW

        pygame.draw.rect(screen, color, rect, border_radius=15)
        pygame.draw.rect(screen, BROWN, rect, 4, border_radius=15)

        button_text = self.text_font.render(text, True, BROWN)

        screen.blit(
            button_text,
            (
                rect.centerx - button_text.get_width() // 2,
                rect.centery - button_text.get_height() // 2
            )
        )

    def draw_night_overlay(self, screen, time_of_day):
        if time_of_day == "night":
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.fill((10, 10, 40))
            overlay.set_alpha(70)
            screen.blit(overlay, (0, 0))

        elif time_of_day == "afternoon":
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.fill((255, 130, 40))
            overlay.set_alpha(25)
            screen.blit(overlay, (0, 0))

    def draw(self, screen, player, customer, waiting_next_customer):
        time_of_day = self.get_time_of_day(player)

        self.draw_floor(screen)
        self.draw_window(screen, time_of_day)
        self.draw_lights(screen)
        self.draw_tables(screen)
        self.draw_counter(screen)
        self.draw_customer(screen)
        self.draw_dialogue(screen, customer)
        self.draw_hud(screen, player)

        self.draw_button(screen, self.recipe_button, "LIVRO DE RECEITAS")

        if waiting_next_customer:
            self.draw_button(screen, self.next_customer_button, "PRÓXIMO CLIENTE")
        else:
            self.draw_button(screen, self.prepare_button, "PREPARAR PEDIDO")

        self.draw_night_overlay(screen, time_of_day)