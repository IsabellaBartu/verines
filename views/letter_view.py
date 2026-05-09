import pygame

from settings import *


class LetterView:

    def __init__(self):

        self.title_font = pygame.font.SysFont("arial", 42, bold=True)

        self.text_font = pygame.font.SysFont("arial", 28)

        self.small_font = pygame.font.SysFont("arial", 24)

        self.continue_button = pygame.Rect(950, 620, 220, 60)

    def draw_letter(self, screen):

        pygame.draw.rect(
            screen,
            (235, 220, 180),
            (170, 70, 940, 560),
            border_radius=20
        )

        pygame.draw.rect(
            screen,
            BROWN,
            (170, 70, 940, 560),
            5,
            border_radius=20
        )

    def draw_text(self, screen):

        title = self.title_font.render(
            "Carta do Avô Verine",
            True,
            BROWN
        )

        screen.blit(title, (240, 120))

        lines = [
            "“Fulano...",
            "",
            "Se você está lendo isso,",
            "talvez eu já tenha partido.",
            "",
            "O restaurante nunca foi",
            "apenas um restaurante.”"
        ]

        y = 220

        for line in lines:

            text = self.text_font.render(
                line,
                True,
                DARK_BROWN
            )

            screen.blit(text, (240, y))

            y += 55

    def draw_button(self, screen):

        mouse_pos = pygame.mouse.get_pos()

        color = YELLOW

        if self.continue_button.collidepoint(mouse_pos):

            color = (255, 230, 140)

        pygame.draw.rect(
            screen,
            color,
            self.continue_button,
            border_radius=15
        )

        pygame.draw.rect(
            screen,
            BROWN,
            self.continue_button,
            4,
            border_radius=15
        )

        text = self.text_font.render(
            "CONTINUAR",
            True,
            BROWN
        )

        screen.blit(
            text,
            (
                self.continue_button.centerx - text.get_width() // 2,
                self.continue_button.centery - text.get_height() // 2
            )
        )

    def draw(self, screen):

        screen.fill((80, 60, 45))

        self.draw_letter(screen)

        self.draw_text(screen)

        self.draw_button(screen)