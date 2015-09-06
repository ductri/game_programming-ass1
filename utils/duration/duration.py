__author__ = 'tri'
import threading
import random
import datetime
import time

class Duration(threading.Thread):

    def __init__(self, time):
        self.time = random.randrange(2, 6)
        threading.Thread.__init__(self, name="ductri")

        return

    # Override run function of base class
    def run(self):
        start = datetime.datetime.now()
        end = datetime.datetime.now()
        i = 0
        while (end - start).total_seconds() < self.time:
            print str(i) + str(self.time)
            end = datetime.datetime.now()
            time.sleep(0.08)
            i += 1
