__author__ = 'tri'


class Waiter:
    """
    This class need to refactor
    """
    def __init__(self):
        self.objects = {}
        return

    def register_waiter(self, keyword, ob):
        self.objects[keyword] = ob

    def unregister_waiter(self, keyword):
        del self.objects[keyword]

    def run(self):
        raise NotImplementedError

