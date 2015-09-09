__author__ = 'tri'

from game_model.drawable import Drawable
from utils.constant.drawable_index import DRAWABLE_INDEX
from utils.customer_waiter_pattern.customer import Customer
from utils.constant.customer_waiter_pattern.customer_key import CUSTOMER_KEY
from utils.observer_pattern.subject import Subject
from utils.observer_pattern.subject_unit import SubjectUnit
from utils.timer.timer import Timer
import pygame


class TimerCounter(Customer, Subject):

    def __init__(self, waiter, end, font_size, pos, color):
        self.end = 0
        self.font_size = font_size
        self.pos = pos
        self.color = color

        self.time = end
        Customer.__init__(self, waiter)

        self.timer = None

        Subject.__init__(self)
        subject_unit = SubjectUnit()
        self.add_subject_unit(subject_unit, 'time_up')

    def run(self):

        font = pygame.font.Font("resources/font.ttf", self.font_size)

        def work():
            drawable_object = Drawable(font.render(str(self.time), True, self.color), self.pos, DRAWABLE_INDEX.TIMER_COUNTER)
            self.register_waiter(CUSTOMER_KEY.TIMER_COUNTER, drawable_object)

            drawable_object = Drawable(font.render('Time remaining:', True, (255, 0, 0)), (self.pos[0] - 280, self.pos[1]), DRAWABLE_INDEX.TIMER_COUNTER)
            self.register_waiter(CUSTOMER_KEY.TIMER_COUNTER+'sub', drawable_object)

            self.time -= 1
            if self.time < self.end + 1:
                self.set_change('time_up', 'time_up')

        self.timer = Timer(1, work)
        self.timer.start()

    def close(self):
        if self.timer is not None:
            self.timer.close()

