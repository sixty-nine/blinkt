import colorsys
import time
import numpy as np

from Blinkt import BlinktDriver
from Blinkt.Workers.Worker import Worker


class CandleWorker(Worker):

    def __init__(self, driver: BlinktDriver):
        super().__init__(driver)
        self.start = 0
        self.end = 60

    def initialize(self):
        self.driver.clear()

    def work(self):
        wait = np.random.choice(np.random.noncentral_chisquare(5, 1, 1000), 1)[0] / 50
        n = np.random.choice(np.random.noncentral_chisquare(5, 0.1, 1000), 1)
        limit = int(n[0])
    
        if limit > self.driver.NUM_PIXELS:
            limit = self.driver.NUM_PIXELS
    
        for pixel in range(limit):
            hue = self.start + (((self.end - self.start) / float(self.driver.NUM_PIXELS)) * pixel)
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue/360.0, 1.0, 1.0)]
            self.driver.set_pixel(pixel, r, g, b)
            self.driver.show()
            time.sleep(0.05 / (pixel + 1))
    
        time.sleep(wait)
        self.driver.clear()
