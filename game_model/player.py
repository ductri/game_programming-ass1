__author__ = 'tri'

from utils.observer_pattern.observer import Observer
from utils.customer_waiter_pattern.customer import Customer
from utils.constant.customer_waiter_pattern.customer_key import CUSTOMER_KEY
from utils.constant.drawable_index import DRAWABLE_INDEX
from utils.observer_pattern.subject import Subject
from utils.observer_pattern.subject_unit import SubjectUnit
from game_model.hammer import Hammer
from game_model.drawable import Drawable

import pygame

"""
Consider combine with hammer.py into 1 module
"""
class Player(Observer, Customer, Subject):

    def __init__(self, event_controller, waiter):

        # Constructor of base class: Observer
        Observer.__init__(self)
        # Register to receive mouse event: Mouse click and motion
        self.register(event_controller, 'mouse_down')
        self.register(event_controller, 'mouse_motion')

        # Constructor of base class: Observer
        Subject.__init__(self)
        player_motion_event = SubjectUnit()
        self.add_subject_unit(player_motion_event, 'player_motion')
        player_hammer_event = SubjectUnit()
        self.add_subject_unit(player_hammer_event, 'player_hammer')

        Customer.__init__(self, waiter)

        # Observer to update position of player
        self.__pos_observers = []

        # Observer to update where and when player hammers
        self.__hammering_observers = []

        # Attributes

        # hammer
        self.hammer = Hammer(waiter, self)

    def update(self, type_key, event):
        """
        Handler mouse click
        :param event: Mouse click event and mouse motion
        :return: None
        """
        if type_key == 'mouse_down':
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.hammer.hit()
                rect_bound = (event.pos[0], event.pos[1], self.hammer.size[0], self.hammer.size[1])
                self.set_change('player_hammer', event.pos)
                #for observer in self.__hammering_observers:
                #    rect_bound = (event.pos[0], event.pos[1], self.hammer.size[0], self.hammer.size[1])
                #    observer.update(rect_bound)

        elif type_key == 'mouse_motion':
            if event.type == pygame.MOUSEMOTION:
                # Just draw the one avatar in list avatars of hammer
                drawable_object = Drawable(self.hammer.get_avatar(), event.pos, DRAWABLE_INDEX.PLAYER)

                # Insert index as prefix keyword to sort
                key = str(drawable_object.index) + CUSTOMER_KEY.HAMMER

                self.register_waiter(key, drawable_object)

                # Update state for all observers want to know position of player
                self.set_change('player_motion', event.pos)

    def register_subject(self, observer):
        self.__pos_observers.append(observer)

    def register_pos_hammering_subject(self, observer):
        self.__hammering_observers.append(observer)

    def close(self):
        self.hammer.close()

