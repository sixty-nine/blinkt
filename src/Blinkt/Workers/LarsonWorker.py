import time
import math

from Blinkt import BlinktDriver
from Blinkt.Workers.Worker import Worker


class LarsonWorker(Worker):

    REDS = [0, 0, 0, 0, 0, 16, 64, 255, 64, 16, 0, 0, 0, 0, 0, 0]

    def __init__(self, driver: BlinktDriver):
        super().__init__(driver)
        self.interval = 0.1
        self.start_time = 0

    def initialize(self):
        self.driver.set_clear_on_exit()
        self.start_time = time.time()

    def work(self):
        delta = (time.time() - self.start_time) * 16
        offset = int(abs((delta % len(LarsonWorker.REDS)) - self.driver.NUM_PIXELS))

        for i in range(self.driver.NUM_PIXELS):
            self.driver.set_pixel(i, LarsonWorker.REDS[offset + i], 0, 0)

        self.driver.show()
