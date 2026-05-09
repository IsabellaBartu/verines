import pygame

from settings import *


class RecipeBookView:

    def __init__(self):

        self.title_font = pygame.font.SysFont("arial", 46, bold=True)

        self.text_font = pygame.font.SysFont("arial", 28)

        self.small_font = pygame.font.SysFont("arial", 22)

        self.back_button = pygame.Rect(980, 620, 220, 60)

    def draw_book(self, screen):

        # Livro
        pygame.draw.rect(
            screen,
            (235, 220, 180),
            (180, 70, 920, 560),
            border_radius=20
        )

        pygame.draw.rect(
            screen,
            BROWN,
            (180, 70, 920, 560),
            5,
            border_radius=20
        )

        # Linha do meio
        pygame.draw.line(
            screen,
            BROWN,
            (640, 80),
            (640, 620),
            4
        )

    def draw_left_page(self, screen):

        title = self.title_font.render(
            "Pizza Verine",
            True,
            BROWN
        )

        screen.blit(title, (240, 120))

        ingredients = [
            "- Massa artesanal",
            "- Molho de tomate",
            "- Queijo",
            "- Pepperoni"
        ]

        y = 220

        for item in ingredients:

            text = self.text_font.render(
                item,
                True,
                DARK_BROWN
            )

            screen.blit(text, (240, y))

            y += 55

    def draw_right_page(self, screen):

        math_title = self.text_font.render(
            "Anotação do avô:",
            True,
            BROWN
        )

        screen.blit(math_title, (720, 140))

        hint = [
            "“Uma pizza dividida em",
            "4 partes pode alimentar",
            "duas pessoas igualmente.”"
        ]

        y = 230

        for line in hint:

            text = self.small_font.render(
                line,
                True,
                DARK_BROWN
            )

            screen.blit(text, (720, y))

            y += 45

        math_tip = self.text_font.render(
            "Metade = 2/4 fatias",
            True,
            RED
        )

        screen.blit(math_tip, (720, 420))

    def draw_back_button(self, screen):

        mouse_pos = pygame.mouse.get_pos()

        color = YELLOW

        if self.back_button.collidepoint(mouse_pos):

            color = (255, 230, 140)

        pygame.draw.rect(
            screen,
            color,
            self.back_button,
            border_radius=15
        )

        pygame.draw.rect(
            screen,
            BROWN,
            self.back_button,
            4,
            border_radius=15
        )

        text = self.text_font.render(
            "VOLTAR",
            True,
            BROWN
        )

        screen.blit(
            text,
            (
                self.back_button.centerx - text.get_width() // 2,
                self.back_button.centery - text.get_height() // 2
            )
        )

    def draw(self, screen):

        screen.fill((180, 140, 100))

        self.draw_book(screen)

        self.draw_left_page(screen)

        self.draw_right_page(screen)

        self.draw_back_button(screen)