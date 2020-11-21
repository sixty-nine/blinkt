import threading

from BlinkIt.BlinktDriver import *
from BlinkIt.Workers import Worker


class LedDirector(object):

    def __init__(self):
        self.stopping = False
        self.commonDataStruct = {}
        self.dataLock = threading.Lock()
        self.thread = threading.Thread()
        self.worker = None

    def stop(self):
        self.stopping = True

    def start(self, worker: Worker):
        if self.thread.isAlive():
            self.thread.cancel()

        self.worker = worker
        self.worker.initialize()
        self.thread = threading.Timer(worker.interval, self.work, ())
        self.thread.daemon = True
        self.thread.start()

    def work(self):
        with self.dataLock:
            self.worker.work()

        if not self.stopping:
            self.thread.run()

