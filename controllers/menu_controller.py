from views.menu_view import MenuView


class MenuController:

    def __init__(self):

        self.view = MenuView()

        self.start_game = False

    def handle_event(self, event):

        if event.type == 1025:

            mouse_pos = event.pos

            if self.view.play_button.collidepoint(mouse_pos):

                self.start_game = True

    def draw(self, screen):

        self.view.draw(screen)