__author__ = 'tri'
from utils.customer_waiter_pattern.customer import Customer
from utils.factory_pattern.factory import Factory
from utils.constant.drawable_index import DRAWABLE_INDEX
from utils.constant.customer_waiter_pattern.customer_key import CUSTOMER_KEY
from utils.timer.timer import Timer
from game_model.drawable import Drawable

import datetime
import pygame


class Head(Customer):

    def __init__(self, name, waiter, stick_time):

        Customer.__init__(self, waiter)

        self.name = name

        self.appear_index = 0
        self.die_index = 0
        self.disappear_index = 0
        self.stand_index = 0

        self.appear_timer = None
        self.die_timer = None
        self.disappear_timer = None
        self.stand_timer = None
        self.main_timer = None

        self.alive = True
        self.showing = False

        self.size = (40, 40)
        self.rect_bound = pygame.Rect(0, 0, self.size[0], self.size[1])

        appear_avatars = Factory.get_avatars('head_appear_avatars')
        if appear_avatars is None:
            raise BaseException('Can not load avatar for Head')
        self.appear_drawable_avatars = []
        for avatar in appear_avatars:
            pos = (0, 0)
            drawable_item = Drawable(avatar, pos, DRAWABLE_INDEX.HEAD)
            self.appear_drawable_avatars.append(drawable_item)

        die_avatars = Factory.get_avatars('head_die_avatars')
        if die_avatars is None:
            raise BaseException('Can not load avatar for Head')
        self.die_drawable_avatars = []
        for avatar in die_avatars:
            pos = (0, 0)
            drawable_item = Drawable(avatar, pos, DRAWABLE_INDEX.HEAD)
            self.die_drawable_avatars.append(drawable_item)

        disappear_avatars = Factory.get_avatars('head_disappear_avatars')
        if disappear_avatars is None:
            raise BaseException('Can not load avatar for Head')
        self.disappear_drawable_avatars = []
        for avatar in disappear_avatars:
            pos = (0, 0)
            drawable_item = Drawable(avatar, pos, DRAWABLE_INDEX.HEAD)
            self.disappear_drawable_avatars.append(drawable_item)

        stand_avatars = Factory.get_avatars('head_stand_avatars')
        if disappear_avatars is None:
            raise BaseException('Can not load avatar for Head')
        self.stand_drawable_avatars = []
        for avatar in stand_avatars:
            pos = (0, 0)
            drawable_item = Drawable(avatar, pos, DRAWABLE_INDEX.HEAD)
            self.stand_drawable_avatars.append(drawable_item)

        self.stick_time = stick_time

        return

    def appear(self, pos):
        self.showing = True
        self.rect_bound = pygame.Rect(pos[0] + 15, pos[1] + 15, self.size[0], self.size[1])

        # Update position to draw on screen
        for drawable_avatar in self.appear_drawable_avatars:
            drawable_avatar.pos = pos
        # Update position to draw on screen
        for drawable_avatar in self.disappear_drawable_avatars:
            drawable_avatar.pos = pos
        # Update position to draw on screen
        for drawable_avatar in self.die_drawable_avatars:
            drawable_avatar.pos = pos
        # Update position to draw on screen
        for drawable_avatar in self.stand_drawable_avatars:
            drawable_avatar.pos = pos

        drawable_object = self.appear_drawable_avatars[self.appear_index]
        # Start drawing
        self.register_waiter(str(drawable_object.index) + CUSTOMER_KEY.HEAD + self.name, drawable_object)

        def do_animation():
            self.appear_index += 1
            if self.appear_index > (self.appear_drawable_avatars.__len__() - 1):
                self.appear_index = 0
                self.appear_timer.stop()

                # After appearing animation is standing animation
                self.stand()
                return
            drawable_object = self.appear_drawable_avatars[self.appear_index]
            key = str(drawable_object.index) + CUSTOMER_KEY.HEAD + self.name
            # Insert index as prefix keyword to sort
            self.register_waiter(key, drawable_object)

            blank = Factory.get_avatars('blank')
            drawable_object1 = Drawable(blank[0], (self.get_rect_bound()[0], self.get_rect_bound()[1]), 2)
            self.register_waiter('blank1', drawable_object1)
            drawable_object2 = Drawable(blank[0], (self.get_rect_bound()[0] + self.get_rect_bound()[2],
                                                   self.get_rect_bound()[1] + self.get_rect_bound()[3]), 2)
            self.register_waiter('blank2', drawable_object2)

        if self.appear_timer is None:
            self.appear_timer = Timer(self.stick_time, do_animation)

        self.appear_timer.start()

    def disappear(self):
        self.alive = False
        drawable_object = self.disappear_drawable_avatars[self.disappear_index]
        # Start drawing
        self.register_waiter(str(drawable_object.index) + CUSTOMER_KEY.HEAD + self.name, drawable_object)

        def do_animation():
            self.disappear_index += 1
            if self.disappear_index > (self.disappear_drawable_avatars.__len__() - 1):
                self.disappear_index = 0
                self.showing = False
                self.disappear_timer.stop()

                # Disappear actually from screen
                key = str(self.disappear_drawable_avatars[0].index) + CUSTOMER_KEY.HEAD + self.name
                self.unregister_waiter(key)
                # Close all timer
                self.close()

                return
            drawable_object = self.disappear_drawable_avatars[self.disappear_index]
            key = str(drawable_object.index) + CUSTOMER_KEY.HEAD + self.name
            # Insert index as prefix keyword to sort
            self.register_waiter(key, drawable_object)

        if self.disappear_timer is None:
            self.disappear_timer = Timer(self.stick_time, do_animation)

        self.disappear_timer.start()

    def show(self, pos, duration):
        self.appear(pos)
        start = datetime.datetime.now()

        def work():
            end = datetime.datetime.now()
            if (end - start).total_seconds() > duration:
                self.disappear()
                self.main_timer.stop()
                self.stand_timer.stop()
        self.main_timer = Timer(0.1, work)
        self.main_timer.start()

    def stand(self):
        drawable_object = self.stand_drawable_avatars[self.stand_index]
        # Start drawing
        self.register_waiter(str(drawable_object.index) + CUSTOMER_KEY.HEAD + self.name, drawable_object)

        def do_animation():
            self.stand_index += 1
            if self.stand_index > (self.stand_drawable_avatars.__len__() - 1):
                self.stand_index = 0
                return
            drawable_object = self.stand_drawable_avatars[self.stand_index]
            key = str(drawable_object.index) + CUSTOMER_KEY.HEAD + self.name
            # Insert index as prefix keyword to sort
            self.register_waiter(key, drawable_object)

        if self.stand_timer is None:
            self.stand_timer = Timer(self.stick_time, do_animation)
            print 'stick_time = ' + str(self.stick_time)

        self.stand_timer.start()

    def die(self):
        self.alive = False
        drawable_object = self.die_drawable_avatars[self.die_index]
        # Start drawing
        self.register_waiter(str(drawable_object.index) + CUSTOMER_KEY.HEAD + self.name, drawable_object)

        def do_animation():
            self.die_index += 1
            if self.die_index > (self.die_drawable_avatars.__len__() - 1):
                self.die_index = 0
                self.die_timer.stop()
                self.disappear()
                return
            drawable_object = self.die_drawable_avatars[self.die_index]
            key = str(drawable_object.index) + CUSTOMER_KEY.HEAD + self.name
            # Insert index as prefix keyword to sort
            self.register_waiter(key, drawable_object)

        if self.die_timer is None:
            self.die_timer = Timer(0.1, do_animation)

        self.appear_timer.stop()
        self.stand_timer.stop()
        self.main_timer.stop()

        self.die_timer.start()

    def get_rect_bound(self):
        return self.rect_bound

    def set_stick_time(self, stick_time):
        self.stick_time = stick_time
        print 'set stick_time = ' + str(stick_time)

    def close(self):
        if self.appear_timer is not None:
            self.appear_timer.close()

        if self.die_timer is not None:
            self.die_timer.close()

        if self.disappear_timer is not None:
            self.disappear_timer.close()

        if self.stand_timer is not None:
            self.stand_timer.close()

        if self.main_timer is not None:
            self.main_timer.close()


