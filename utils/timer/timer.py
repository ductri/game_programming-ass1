__author__ = 'tri'

import threading
import datetime
import time


class Timer(threading.Thread):
    """
    Like timer in java
    """
    def __init__(self, interval, work_function=None):
        """
        Constructor
        :param interval:
        :param work_function:
        :return:
        """
        self.time_stick = interval
        self.work_function = work_function
        self.enable = False
        threading.Thread.__init__(self, name="unknown")
        self.timer_alive = True
        # Run immediately
        super(Timer, self).start()

    # Override run function of base class: threading
    def run(self):
        # Actually work
        while self.timer_alive:
            if self.enable:
                if self.work_function is not None:
                    self.work_function()
                else:
                    raise NotImplementedError
                time.sleep(self.time_stick)

    def start(self):
        self.enable = True

    def stop(self):
        self.enable = False

    def set_interval(self, interval):
        self.time_stick = interval

    def close(self):
        self.stop()
        self.timer_alive = False
