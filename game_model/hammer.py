__author__ = 'tri'

from utils.factory_pattern.factory import Factory
from utils.duration.duration import Duration
from utils.customer_waiter_pattern.customer import Customer
from game_model.drawable import Drawable


# TODO clean code: set private attribute
class Hammer(Customer):
    """
    This class managers hammer of player, detail:
    - Animation when hammer
    - Sound effect when hammer
    - Avatar of hammer
    - Replace cursor with avatar
    """

    def __init__(self, waiter):
        """
        Constructor
        :param waiter: waiter for implement hammer action
        :return: None
        """

        # Constructor of base class
        Customer.__init__(self, waiter)

        avatars = Factory.get_avatar('hammer_avatars')
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

        self.index = 0

    def hit(self, pos):
        """
        This function play a sound in new thread, so it can be call
         2 times concurrent
        :return:
        """
        self.sound_hit.play()

        # Hammer action effect
        # TODO Need to improve
        def work():
            keep_work = True
            self.index += 1
            if self.index > 8:
                self.index = 0
                keep_work = False
            avatar_index = 4 - abs(self.index - 4)
            self.drawable_avatar = self.drawable_avatars[avatar_index]
            self.drawable_avatar.pos = pos
            self.register('2_hammer', self.drawable_avatar)

            return keep_work

        duration = Duration(0.05, 0.5, work)
        duration.start()

    def get_avatar(self):
            return self.drawable_avatar.bitmap
