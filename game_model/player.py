__author__ = 'tri'

from utils.observer_pattern.observer import Observer
from utils.customer_waiter_pattern.customer import Customer
from utils.constant.customer_waiter_pattern.customer_key import CUSTOMER_KEY
from utils.observer_pattern.subject import Subject
from game_model.hammer import Hammer
from game_model.drawable import Drawable

import pygame

"""
Consider combine with hammer.py into 1 module
"""
class Player(Observer, Customer, Subject):

    def __init__(self, event_controller, waiter):

        # Constructor of base class
        Observer.__init__(self, event_controller)
        Customer.__init__(self, waiter)
        self.__observers = []

        # Register to receive mouse event: Mouse click and motion
        self.register_mouse_down()
        self.register_mouse_motion()

        # Attributes

        # hammer
        self.hammer = Hammer(waiter, self)

    def update(self, event):
        """
        Handler mouse click
        :param event: Mouse click event and mouse motion
        :return: None
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.hammer.hit()
        elif event.type == pygame.MOUSEMOTION:
            # Just draw the one avatar in list avatars of hammer
            drawable_object = Drawable(self.hammer.get_avatar(), event.pos, 2)

            # Insert index as prefix keyword to sort
            key = str(drawable_object.index) + CUSTOMER_KEY.HAMMER

            self.register_waiter(key, drawable_object)

            for observer in self.__observers:
                observer.update(event.pos)

    def register_subject(self, observer):
        self.__observers.append(observer)