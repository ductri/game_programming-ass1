__author__ = 'tri'

from utils.factory_pattern.factory import Factory
from utils.customer_waiter_pattern.customer import Customer
from utils.constant.customer_waiter_pattern.customer_key import CUSTOMER_KEY
from utils.timer.timer import Timer
from utils.observer_pattern.observer import Observer
from game_model.drawable import Drawable

import threading


# TODO clean code: set private attribute
# TODO Bug when use scroll mouse
class Hammer(Customer, Observer):
    """
    This class managers hammer of player, detail:
    - Animation when hammer
    - Sound effect when hammer
    - Avatar of hammer
    - Replace cursor with avatar
    """

    def __init__(self, waiter, subject):
        """
        Constructor
        :param waiter: waiter for implement hammer action
        :return: None
        """

        # Constructor of base class
        Customer.__init__(self, waiter)
        Observer.__init__(self, subject)
        self.register_subject()

        avatars = Factory.get_avatars('hammer_avatars')
        if avatars is None:
            raise BaseException('Can not load avatar for hammer')
        self.drawable_avatars = []
        for avatar in avatars:
            drawable_item = Drawable(avatar, (0, 0), 2)
            self.drawable_avatars.append(drawable_item)

        # Default is the first one
        self.drawable_avatar = self.drawable_avatars[0]

        self.sound_hit = Factory.get_sound('hammer_hit')
        if self.sound_hit is None:
            raise BaseException('Can not load "hit" sound effect of hammer')

        # Used to step counter, change image when hammer
        self.index = 0

        # Used to prevent hammer when hammering
        self.hammering = False

        self.timer = None

        self.pos = (0,0)

    def hit(self):
        """
        This function play a sound in new thread, so it can be call
         2 times concurrent
        :return:
        """
        if not self.hammering:
            self.sound_hit.play()

        # Hammer action effect
        # TODO Need to improve effect
        def work():
            self.hammering = True
            self.index += 1
            if self.index > 8:
                self.index = 0
                self.hammering = False
                self.timer.stop()

            avatar_index = 4 - abs(self.index - 4)
            self.drawable_avatar = self.drawable_avatars[avatar_index]
            self.drawable_avatar.pos = self.pos
            print self.index

            # Insert index as prefix keyword to sort
            key = str(self.drawable_avatar.index) + CUSTOMER_KEY.HAMMER
            self.register_waiter(key, self.drawable_avatar)

        if self.timer is None:
            self.timer = Timer(0.5, work)

        if not self.hammering:
            self.timer.start()

    def get_avatar(self):
            return self.drawable_avatar.bitmap

    def update(self, pos):
        """
        Override function of base class: Observer
        :param event:
        :return:
        """

        self.pos = pos