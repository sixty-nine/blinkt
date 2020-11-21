from BlinkIt import BlinktDriver


class Worker(object):

    interval = 1  # second

    def __init__(self, driver: BlinktDriver):
        self.driver = driver

    def initialize(self):
        pass

    def work(self):
        pass
