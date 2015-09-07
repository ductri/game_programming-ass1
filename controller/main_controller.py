__author__ = 'tri'

from utils.observer_pattern.observer import Observer
from utils.factory_pattern.factory import Factory
from utils.customer_waiter_pattern.waiter import Waiter
from utils.constant.customer_waiter_pattern.customer_key import CUSTOMER_KEY
from game_model.player import Player
from game_model.drawable import Drawable

import pygame


class MainController(Observer, Waiter):
    """Control common stage of game, include:
    - Init game
    - Load background
    - Load model
    """

    def __init__(self, event_controller, env):

        # Save event_controller to use later
        self.event_controller = event_controller
        self.env = env

        # Constructor of base class
        Observer.__init__(self,event_controller)
        Waiter.__init__(self)

        # Register to receive some special events
        self.register_special_event()

        # Attribute declare
        self.quit_game = False
        self.player = None
        self.drawable_components = []

        # Init pygame
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(self.env.screen_size)
        pygame.mouse.set_visible(False)    # Hide default mouse cursor

    def update(self, event):
        """
        Called when expected event is happened
        :param event: event is happened
        :return: None
        """
        if event.type == pygame.QUIT:
            self.quit_game = True

    def init_game(self):
        """
        Init logically game
        :return: None
        """
        self.screen.fill((255, 255, 255))
        background = Factory.get_background()
        if background is not None:
            drawable_object = Drawable(background, (0, 0), 1)
            key = str(drawable_object.index) + CUSTOMER_KEY.BACKGROUND      # Insert index as prefix keyword to sort
            self.register(key, drawable_object)
        else:
            raise 'Can not load background image'

        self.player = Player(self.event_controller, self)

    def run(self):
        """
        Implement from Waiter. This function clear and then draw whole screen.
        :return: None
        """
        self.screen.fill((255, 255, 255))
        for key in sorted(self.objects.keys()):     # TODO: Need to improve
            self.screen.blit(self.objects[key].bitmap, self.objects[key].pos)
