__author__ = 'tri'
from utils.customer_waiter_pattern.customer import Customer
from utils.factory_pattern.factory import Factory
from utils.constant.drawable_index import DRAWABLE_INDEX
from utils.constant.customer_waiter_pattern.customer_key import CUSTOMER_KEY
from utils.timer.timer import Timer
from game_model.drawable import Drawable

import threading

class Head(Customer):

    def __init__(self, waiter):

        Customer.__init__(waiter)

        avatars = Factory.get_avatars('head_avatars')
        if avatars is None:
            raise BaseException('Can not load avatar for hammer')
        self.drawable_avatars = []
        for avatar in avatars:
            drawable_item = Drawable(avatar, (0, 0), DRAWABLE_INDEX.HEAD)
            self.drawable_avatars.append(drawable_item)


        return

    def appear(self, pos):
        drawable_avatar = Drawable(self.drawable_avatars[0],pos,DRAWABLE_INDEX.HEAD)
        self.register_waiter(CUSTOMER_KEY.HEAD, drawable_avatar)

        def disappear():
            self.unregister_watier(CUSTOMER_KEY.HEAD)

        timer = threading.Timer(1, disappear)
        timer.start()
        return

    def die(self):

        return

