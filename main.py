import pygame
import sys

from settings import *

from controllers.menu_controller import MenuController
from controllers.restaurant_controller import RestaurantController
from controllers.kitchen_controller import KitchenController
from controllers.recipe_book_controller import RecipeBookController
from controllers.letter_controller import LetterController
from controllers.audio_controller import AudioController

from views.fade_view import FadeView

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

current_scene = "menu"

menu = MenuController()
restaurant = RestaurantController()
kitchen = KitchenController()
recipe_book = RecipeBookController()
letter = LetterController()

audio = AudioController()

fade = FadeView()

audio.play_music(
    "assets/sounds/music/menu_music.mp3"
)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # MENU
        if current_scene == "menu":

            menu.handle_event(event)

            if menu.start_game:

                fade.start_fade()

                audio.play_button_sound()

                audio.play_music(
                    "assets/sounds/music/restaurant_music.mp3"
                )

                current_scene = "restaurant"

        # RESTAURANTE
        elif current_scene == "restaurant":

            restaurant.handle_event(event)

            # Livro de receitas
            if restaurant.go_to_recipe_book:

                fade.start_fade()

                audio.play_button_sound()

                restaurant.go_to_recipe_book = False

                current_scene = "recipe_book"

            # Cozinha
            if restaurant.go_to_kitchen:

                fade.start_fade()

                audio.play_button_sound()

                restaurant.go_to_kitchen = False

                kitchen.correct_slices = (
                    restaurant.customer.correct_slices
                )

                current_scene = "kitchen"

        # COZINHA
        elif current_scene == "kitchen":

            kitchen.handle_event(event)

            # Som da pizza
            if event.type == pygame.MOUSEBUTTONDOWN:

                audio.play_pizza_sound()

            if kitchen.finished:

                if kitchen.success:

                    audio.play_success_sound()

                    audio.play_cash_sound()

                    restaurant.player.money += 20

                    restaurant.player.reputation += 1

                    restaurant.customer.feedback = (
                        restaurant.customer.success_feedback
                    )

                else:

                    audio.play_error_sound()

                    restaurant.player.money -= 5

                    restaurant.player.reputation -= 1

                    restaurant.customer.feedback = (
                        restaurant.customer.error_feedback
                    )

                restaurant.player.clients_served += 1

                kitchen.reset()

                # Fim do dia
                if restaurant.player.clients_served >= 3:

                    restaurant.player.clients_served = 0

                    restaurant.player.day += 1

                    fade.start_fade()

                    audio.play_paper_sound()

                    current_scene = "letter"

                else:

                    restaurant.waiting_next_customer = True

                    fade.start_fade()

                    current_scene = "restaurant"

        # LIVRO DE RECEITAS
        elif current_scene == "recipe_book":

            recipe_book.handle_event(event)

            if recipe_book.back_to_restaurant:

                fade.start_fade()

                audio.play_button_sound()

                recipe_book.back_to_restaurant = False

                current_scene = "restaurant"

        # CARTA
        elif current_scene == "letter":

            letter.handle_event(event)

            if letter.back_to_restaurant:

                fade.start_fade()

                audio.play_button_sound()

                letter.back_to_restaurant = False

                restaurant.customer.generate_customer()

                restaurant.customer.feedback = ""

                restaurant.waiting_next_customer = False

                current_scene = "restaurant"

    # DESENHO DAS CENAS

    if current_scene == "menu":

        menu.draw(screen)

    elif current_scene == "restaurant":

        restaurant.draw(screen)

    elif current_scene == "kitchen":

        kitchen.draw(screen)

    elif current_scene == "recipe_book":

        recipe_book.draw(screen)

    elif current_scene == "letter":

        letter.draw(screen)

    # Fade
    fade.update()

    fade.draw(screen)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
sys.exit()