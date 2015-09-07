__author__ = 'tri'
from utils.customer_waiter_pattern.customer import Customer
from utils.factory_pattern.factory import Factory
from game_model.drawable import Drawable


class Head(Customer):

    def __init__(self, customer):

        avatars = Factory.get_avatars()
        if avatars is None:
            raise BaseException('Can not load avatar for hammer')
        self.drawable_avatars = []
        for avatar in avatars:
            drawable_item = Drawable(avatar, (0, 0), 2)
            self.drawable_avatars.append(drawable_item)

        return