import pygame
import sys

from settings import *

from controllers.menu_controller import MenuController
from controllers.restaurant_controller import RestaurantController
from controllers.kitchen_controller import KitchenController
from controllers.recipe_book_controller import RecipeBookController
from controllers.letter_controller import LetterController

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

current_scene = "menu"

menu = MenuController()
restaurant = RestaurantController()
kitchen = KitchenController()
recipe_book = RecipeBookController()
letter = LetterController()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if current_scene == "menu":

            menu.handle_event(event)

            if menu.start_game:
                current_scene = "restaurant"

        elif current_scene == "restaurant":

            restaurant.handle_event(event)

            if restaurant.go_to_recipe_book:
                restaurant.go_to_recipe_book = False
                current_scene = "recipe_book"

            if restaurant.go_to_kitchen:
                restaurant.go_to_kitchen = False
                kitchen.correct_slices = restaurant.customer.correct_slices
                current_scene = "kitchen"

        elif current_scene == "kitchen":

            kitchen.handle_event(event)

            if kitchen.finished:

                if kitchen.success:
                    restaurant.player.money += 20
                    restaurant.player.reputation += 1
                    restaurant.customer.feedback = restaurant.customer.success_feedback
                else:
                    restaurant.player.money -= 5
                    restaurant.player.reputation -= 1
                    restaurant.customer.feedback = restaurant.customer.error_feedback

                restaurant.player.clients_served += 1

                kitchen.reset()

                if restaurant.player.clients_served >= 3:
                    restaurant.player.clients_served = 0
                    restaurant.player.day += 1
                    current_scene = "letter"
                else:
                    restaurant.waiting_next_customer = True
                    current_scene = "restaurant"

        elif current_scene == "recipe_book":

            recipe_book.handle_event(event)

            if recipe_book.back_to_restaurant:
                recipe_book.back_to_restaurant = False
                current_scene = "restaurant"

        elif current_scene == "letter":

            letter.handle_event(event)

            if letter.back_to_restaurant:
                letter.back_to_restaurant = False
                restaurant.customer.generate_customer()
                restaurant.customer.feedback = ""
                restaurant.waiting_next_customer = False
                current_scene = "restaurant"

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

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()