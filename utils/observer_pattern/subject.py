__author__ = 'tri'


class Subject:
    """Abstract class"""

    def __init__(self):

        return

    def register_mouse_down(self):
        raise NotImplementedError

    def register_mouse_motion(self):
        raise NotImplementedError

    def register_mouse_up(self):
        raise NotImplementedError

    def register_key_down(self):
        raise NotImplementedError

    def register_key_up(self):
        raise NotImplementedError

    def register_special_event(self):
        raise NotImplementedError

    def register_subject(self):
        raise NotImplementedError
