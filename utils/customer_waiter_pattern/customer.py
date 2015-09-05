__author__ = 'tri'


class Customer:
    """
    This class need to refactor
    """
    def __init__(self, waiter):
        self.waiter = waiter
        return

    def register(self, keyword, ob):
        self.waiter.register(keyword, ob)
