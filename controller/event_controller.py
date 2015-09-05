__author__ = 'tri'
import pygame

from utils.observer_pattern.subject import Subject


class EventController(Subject):

    def __init__(self):
        self.mouse_down_observers = []
        self.mouse_up_observers = []
        self.mouse_motion_observers = []

        self.key_down_observers = []
        self.key_up_observers = []
        self.special_observers = []

    def register_mouse_down(self, observer):
        self.mouse_down_observers.append(observer)

    def register_mouse_up(self, observer):
        self.mouse_up_observers.append(observer)

    def register_mouse_motion(self, observer):
        self.mouse_motion_observers.append(observer)

    def register_key_down(self, observer):
        self.key_down_observers.append(observer)

    def register_key_up(self, observer):
        self.key_up_observers.append(observer)

    def register_special_event(self, observer):
        self.special_observers.append(observer)

    def run(self):
        """
        Need to re-code
        """
        for event in pygame.event.get():
            #MOUSE
            if event.type == pygame.MOUSEBUTTONDOWN:
                for mouse_down_observer in self.mouse_down_observers:
                    mouse_down_observer.update(event)
                continue

            if event.type == pygame.MOUSEBUTTONUP:
                for mouse_up_observer in self.mouse_up_observers:
                    mouse_up_observer.update(event)
                continue

            if event.type == pygame.MOUSEMOTION:
                for mouse_motion_observer in self.mouse_motion_observers:
                    mouse_motion_observer.update(event)
                continue

            # KEYBOARD
            if event.type == pygame.KEYDOWN:
                for key_down_observer in self.key_down_observers:
                    key_down_observer.update(event)
                continue

            if event.type == pygame.KEYUP:
                for key_up_observer in self.key_up_observers:
                    key_up_observer.update(event)
                continue

            for special_observer in self.special_observers:
                special_observer.update(event)
