from BlinkIt.Workers.Worker import Worker


class DummyWorker(Worker):
    def initialize(self):
        self.driver.clear()
        self.driver.show()
