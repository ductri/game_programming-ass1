__author__ = 'tri'


class Subject:
    """Abstract class"""

    def __init__(self):
        self.__subject_units = {}
        return

    def add_subject_unit(self, subject_unit, type_key):
        self.__subject_units[type_key] = subject_unit

    def set_change(self, type_key, data):
        self.__subject_units[type_key].notice_all(type_key, data)

    def register(self, observer, type_key):
        self.__subject_units[type_key].attach(observer)
