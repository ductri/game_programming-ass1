__author__ = 'tri'


class SubjectUnit:

    def __init__(self):
        self.__observers = []

    def attach(self, observer):
        self.__observers.append(observer)

    def notice_all(self, type_key, data):
        for observer in self.__observers:
            observer.update(type_key, data)



