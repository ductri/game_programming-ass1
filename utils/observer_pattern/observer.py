__author__ = 'tri'


class Observer:

    def __init__(self, subject):
        self.subject = subject

    ################
    # Mouse events #
    ################
    def register_mouse_down(self):
        self.subject.register_mouse_down(self)

    def register_mouse_up(self):
        self.subject.register_mouse_up(self)

    def register_mouse_motion(self):
        self.subject.register_mouse_motion(self)
    ################
    # Key events   #
    ################
    def register_key_event(self):
        self.subject.register_key_down(self)

    ##################
    # Special events #
    ##################
    def register_special_event(self):
        self.subject.register_special_event(self)

    def update(self, event):
        raise NotImplementedError
