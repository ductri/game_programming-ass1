__author__ = 'tri'
from utils.customer_waiter_pattern.customer import Customer
from utils.factory_pattern.factory import Factory
from utils.constant.drawable_index import DRAWABLE_INDEX
from utils.constant.customer_waiter_pattern.customer_key import CUSTOMER_KEY
from utils.constant.NUM_SPRITES import NUM_SPRITES
from utils.constant.DURATION import DURATION
from utils.timer.timer import Timer
from game_model.drawable import Drawable

import threading

class Head(Customer):

    avatars = []
    def __init__(self, waiter,pos):

        Customer.__init__(waiter)
        self.avatarIndex = 0
        self.dieIndex = 0
        self.timer = None
        self.alive = True
        self.setPos(pos)

        self.avatars = Factory.get_avatars('head_avatars')
        if self.avatars is None:
            raise BaseException('Can not load avatar for hammer')

        self.drawable_avatars = []
        for avatar in self.avatars:
            drawable_item = Drawable(avatar, self.pos, DRAWABLE_INDEX.HEAD)
            self.drawable_avatars.append(drawable_item)

        self.die_avatar = Factory.get_avatars('head_avatars_die')
        if self.die_avatars is None:
                raise BaseException('Can not load avatar for die head')

        self.drawable_die_avatars = []
        for die_avatar in self.die_avatars:
            item = Drawable(die_avatar,self.pos,DRAWABLE_INDEX.HEAD)
            self.drawable_die_avatars.append(die_avatar)
        return

    def setPos(self,pos):
        self.pos = pos
    def setWidth(self,w):
        self.width = w
    def setHeight(self,h):
        self.height = h

    def appear(self, pos):

        self.avatarIndex = 0
        drawable_avatar = self.drawable_avatars[self.avatarIndex]

        self.register_waiter(CUSTOMER_KEY.HEAD, drawable_avatar)

        def doAnimation():
            if self.alive:
                self.avatarIndex += 1
                if(self.avatarIndex > NUM_SPRITES.HEAD ):
                    self.avatarIndex = 0
                    disappear()
                    self.timer.stop()
                drawable_avatar = self.drawable_avatars[self.avatarIndex]
                # Insert index as prefix keyword to sort
                self.register_waiter(CUSTOMER_KEY.HEAD, drawable_avatar)
            else:
                self.die()

        def disappear():
            self.unregister_watier(CUSTOMER_KEY.HEAD)
        if(self.timer == None):
            self.timer = threading.Timer(DURATION.HEAD, doAnimation())
        self.timer.start()
        return

    def check_collision(self,harmmer):
        #need to implement later
        return False


    def die(self):
        self.dieIndex = 0
        drawable_avatar = self.drawable_die_avatars[self.dieIndex]
        self.register_waiter(CUSTOMER_KEY.HEAD, drawable_avatar)

        def doAnimation():
            self.avatarIndex += 1
            if(self.avatarIndex > NUM_SPRITES.DIE_HEAD ):
                self.avatarIndex = 0
                disappear()
                self.timer.stop()
            drawable_avatar = self.drawable_avatars[self.avatarIndex]
            # Insert index as prefix keyword to sort
            self.register_waiter(CUSTOMER_KEY.HEAD, drawable_avatar)

        def disappear():
            self.unregister_watier(CUSTOMER_KEY.HEAD)
        self.timer = threading.Timer(DURATION.HEAD, doAnimation())
        self.timer.start()
        return


