__author__ = 'tri'
import pygame

from utils.observer_pattern.subject import Subject
from utils.observer_pattern.subject_unit import SubjectUnit

class EventController(Subject):

    def __init__(self):
        # Constructor of base class: Subject
        Subject.__init__(self)

        mouse_down_subject_unit = SubjectUnit()
        self.add_subject_unit(mouse_down_subject_unit, 'mouse_down')

        key_down_subject_unit = SubjectUnit()
        self.add_subject_unit(key_down_subject_unit, 'key_down')

        key_down_subject_unit = SubjectUnit()
        self.add_subject_unit(key_down_subject_unit, 'special')

        key_down_subject_unit = SubjectUnit()
        self.add_subject_unit(key_down_subject_unit, 'mouse_motion')

    def run(self):
        """
        Need to re-code
        """
        for event in pygame.event.get():
            #MOUSE
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.set_change('mouse_down', event)
                continue

            if event.type == pygame.MOUSEBUTTONUP:

                continue

            if event.type == pygame.MOUSEMOTION:
                self.set_change('mouse_motion', event)
                continue

            # KEYBOARD
            if event.type == pygame.KEYDOWN:
                self.set_change('key_down', event)
                continue

            if event.type == pygame.KEYUP:

                continue

            if event.type == pygame.QUIT:
                self.set_change('special', event)

