import pygame

from settings import *


class FadeView:

    def __init__(self):

        self.alpha = 0

        self.fade_speed = 12

        self.fading = False

        self.fade_surface = pygame.Surface((WIDTH, HEIGHT))

        self.fade_surface.fill((0, 0, 0))

    def start_fade(self):

        self.alpha = 255

        self.fading = True

    def update(self):

        if self.fading:

            self.alpha -= self.fade_speed

            if self.alpha <= 0:

                self.alpha = 0

                self.fading = False

    def draw(self, screen):

        if self.alpha > 0:

            self.fade_surface.set_alpha(self.alpha)

            screen.blit(self.fade_surface, (0, 0))