import pygame


class AudioController:

    def __init__(self):

        # Botões
        self.button_sound = pygame.mixer.Sound(
            "assets/sounds/sfx/button_click.wav"
        )

        # Pizza
        self.pizza_sound = pygame.mixer.Sound(
            "assets/sounds/sfx/pizza_click.wav"
        )

        # Sucesso
        self.success_sound = pygame.mixer.Sound(
            "assets/sounds/sfx/success.wav"
        )

        # Erro
        self.error_sound = pygame.mixer.Sound(
            "assets/sounds/sfx/error.wav"
        )

        # Dinheiro
        self.cash_sound = pygame.mixer.Sound(
            "assets/sounds/sfx/cash.wav"
        )

        # Papel
        self.paper_sound = pygame.mixer.Sound(
            "assets/sounds/sfx/paper.wav"
        )

        self.current_music = None

        self.set_volumes()

    def set_volumes(self):

        self.button_sound.set_volume(0.4)

        self.pizza_sound.set_volume(0.4)

        self.success_sound.set_volume(0.5)

        self.error_sound.set_volume(0.5)

        self.cash_sound.set_volume(0.5)

        self.paper_sound.set_volume(0.5)

    def play_button_sound(self):

        self.button_sound.play()

    def play_pizza_sound(self):

        self.pizza_sound.play()

    def play_success_sound(self):

        self.success_sound.play()

    def play_error_sound(self):

        self.error_sound.play()

    def play_cash_sound(self):

        self.cash_sound.play()

    def play_paper_sound(self):

        self.paper_sound.play()

    def play_music(self, music_path):

        if self.current_music != music_path:

            pygame.mixer.music.load(music_path)

            pygame.mixer.music.set_volume(0.4)

            pygame.mixer.music.play(-1)

            self.current_music = music_path