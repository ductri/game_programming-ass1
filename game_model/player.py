__author__ = 'tri'

from utils.observer_pattern.observer import Observer
from utils.customer_waiter_pattern.customer import Customer
from utils.constant.customer_waiter_pattern.customer_key import CUSTOMER_KEY
from utils.constant.drawable_index import DRAWABLE_INDEX
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
        Observer.__init__(self)
        Customer.__init__(self, waiter)

        # Observer to update position of player
        self.__pos_observers = []

        # Observer to update where and when player hammers
        self.__hammering_observers = []

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

            for observer in self.__hammering_observers:
                rect_bound = (event.pos[0], event.pos[1], self.hammer.size[0], self.hammer.size[1])
                observer.update(rect_bound)

        elif event.type == pygame.MOUSEMOTION:
            # Just draw the one avatar in list avatars of hammer
            drawable_object = Drawable(self.hammer.get_avatar(), event.pos, DRAWABLE_INDEX.PLAYER)

            # Insert index as prefix keyword to sort
            key = str(drawable_object.index) + CUSTOMER_KEY.HAMMER

            self.register_waiter(key, drawable_object)

            # Update state for all observers want to know position of player
            for observer in self.__pos_observers:
                observer.update(event.pos)



    def register_subject(self, observer):
        self.__pos_observers.append(observer)

    def register_pos_hammering_subject(self, observer):
        self.__hammering_observers.append(observer)

    def close(self):
        self.hammer.close()

