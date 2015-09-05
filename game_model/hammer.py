__author__ = 'tri'
from utils.observer_pattern.observer import Observer
from utils.factory_pattern.factory import Factory


class Hammer(Observer):
    """
    This class managers hammer of player, detail:
    - Animation when hammer
    - Sound effect when hammer
    - Avatar of hammer
    - Replace cursor with avatar
    """

    def __init__(self, subject):
        """
        Constructor
        :param subject: subject to observer whenever event hasppens
        :return: None
        """
        # Constructor of base class
        Observer.__init__(self,subject)
        # Register event mouse move to replace cursor with avatar
        self.register_mouse_motion()

        self.avatar = Factory.get_avatar('hammer_avatar')
        if self.avatar is None:
            raise BaseException('Can not load avatar for hammer')

        self.sound_hit = Factory.get_sound('hammer_hit')
        if self.sound_hit is None:
            raise BaseException('Can not load "hit" sound effect of hammer')

    def update(self, event):
        """
        Overloading base function. This function is called when expected
        event happens
        :param event: Expected event. In this case, it's mouse move event
        :return: None
        """
        print 'From Hammer: ' + str(event.pos)


    def hit(self):
        """
        This function play a sound in new thread, so it can be call
         2 times concurrent
        :return:
        """
        self.sound_hit.play()