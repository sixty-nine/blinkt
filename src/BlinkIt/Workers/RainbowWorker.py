import colorsys
import time

from BlinkIt import BlinktDriver
from BlinkIt.Workers.Worker import Worker


class RainbowWorker(Worker):
    def __init__(self, driver: BlinktDriver):
        super().__init__(driver)
        self.spacing = 360.0 / 16.0
        self.hue = 0
        self.interval = 0.1

    def initialize(self):
        self.driver.set_clear_on_exit()
        self.driver.set_brightness(0.1)

    def work(self):
        self.hue = int(time.time() * 100) % 360
        for x in range(self.driver.NUM_PIXELS):
            offset = x * self.spacing
            h = ((self.hue + offset) % 360) / 360.0
            r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            self.driver.set_pixel(x, r, g, b)

        self.driver.show()