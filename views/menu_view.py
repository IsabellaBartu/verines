import pygame

from settings import *


class MenuView:

    def __init__(self):

        self.title_font = pygame.font.SysFont("arial", 72, bold=True)

        self.button_font = pygame.font.SysFont("arial", 36)

        self.play_button = pygame.Rect(
            WIDTH // 2 - 150,
            350,
            300,
            80
        )

    def draw_button(self, screen):

        mouse_pos = pygame.mouse.get_pos()

        color = YELLOW

        if self.play_button.collidepoint(mouse_pos):

            color = (255, 230, 140)

        pygame.draw.rect(
            screen,
            color,
            self.play_button,
            border_radius=20
        )

        pygame.draw.rect(
            screen,
            BROWN,
            self.play_button,
            4,
            border_radius=20
        )

        button_text = self.button_font.render(
            "JOGAR",
            True,
            BROWN
        )

        screen.blit(
            button_text,
            (
                self.play_button.centerx - button_text.get_width() // 2,
                self.play_button.centery - button_text.get_height() // 2
            )
        )

    def draw(self, screen):

        screen.fill(BACKGROUND_COLOR)

        title = self.title_font.render(
            "VERINE'S",
            True,
            BROWN
        )

        screen.blit(
            title,
            (
                WIDTH // 2 - title.get_width() // 2,
                180
            )
        )

        self.draw_button(screen)