import math
import time

from Blinkt.Workers.Worker import Worker


class GraphWorker(Worker):
    def show_graph(self, v, r, g, b):
        v *= self.driver.NUM_PIXELS
        for x in range(self.driver.NUM_PIXELS):
            if v < 0:
                r, g, b = 0, 0, 0
            else:
                r, g, b = [int(min(v,1.0) * c) for c in [r, g, b]]
            self.driver.set_pixel(x, r, g, b)
            v -= 1

        self.driver.show()

    def work(self):
        t = time.time()
        v = (math.sin(t) + 1) / 2 # Get a value between 0 and 1
        self.show_graph(v, 255, 0, 255)
