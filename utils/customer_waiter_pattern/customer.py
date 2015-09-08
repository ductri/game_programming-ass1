__author__ = 'tri'


class Customer:
    """
    This class need to refactor
    """
    def __init__(self, waiter):
        self.waiter = waiter
        return

    def register_waiter(self, keyword, ob):
        self.waiter.register_waiter(keyword, ob)

    def unregister_watier(self, keyword):
        self.waiter.unregister_watier(keyword)