from sys import exit

try:
    import psutil
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install psutil")


from Blinkt.Workers.Worker import Worker


class MemLoadWorker(Worker):

    REDS = [0, 0, 0, 0, 0, 16, 64, 255, 64, 16, 0, 0, 0, 0, 0, 0]
    interval = 0.1

    def show_graph(self, v, r, g, b):
        v *= self.driver.NUM_PIXELS
        for x in range(self.driver.NUM_PIXELS):
            if v < 0:
                r, g, b = 0, 0, 0
            else:
                r, g, b = [int(min(v, 1.0) * c) for c in [r, g, b]]
            self.driver.set_pixel(x, r, g, b)
            v -= 1

        self.driver.show()

    def work(self):
        v = psutil.virtual_memory().percent / 100.0
        self.show_graph(v, 255, 0, 255)

