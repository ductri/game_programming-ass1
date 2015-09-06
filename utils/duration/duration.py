__author__ = 'tri'

import threading
import datetime
import time


class Duration(threading.Thread):

    def __init__(self, time_stick, time_duration, work_function=None):
        """
        Constructor
        :param time_stick: time to sleep each loop, equivalence interval of timer, in second
        :param time_duration: time to live, in second
        :return: None
        """
        self.time_stick = time_stick
        self.time_duration = time_duration
        self.work_function = work_function
        threading.Thread.__init__(self, name="unknown")

    # Override run function of base class
    def run(self):
        start = datetime.datetime.now()
        end = datetime.datetime.now()
        i = 0
        while (end - start).total_seconds() < self.time_duration:
            end = datetime.datetime.now()
            time.sleep(self.time_stick)
            i += 1

            # Actually work
            if self.work_function is not None:
                self.work_function()
            else:
                raise NotImplementedError
