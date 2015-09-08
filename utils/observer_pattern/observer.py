__author__ = 'tri'


class Observer:

    def __init__(self):
        return

    def register(self, subject, type_key):
        subject.register(self,type_key)

    def update(self, type_key, data):
        raise NotImplementedError

