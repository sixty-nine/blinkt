import atexit
from sys import exit

try:
    import psutil
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install psutil")

try:
    from flask import Flask
except ImportError:
    exit("This script requires the flask module\nInstall with: sudo pip install flask")

from Blinkt import LedDirector, BlinktDriver
from Blinkt.Workers import DummyWorker, RainbowWorker, LarsonWorker, CpuLoadWorker

app = Flask(__name__)

port = 5000

director = LedDirector()
driver = BlinktDriver()


@app.route('/')
def hello_world():
    return 'Hello World! I am running on port ' + str(port)


@app.route('/rainbow')
def rainbow_action():
    director.start(RainbowWorker(driver))
    return 'Rainbow'


@app.route('/clear')
def clear_action():
    director.start(DummyWorker(driver))
    return 'Dummy'


@app.route('/larson')
def larson_action():
    director.start(LarsonWorker(driver))
    return 'Larson'


@app.route('/cpu-load')
def cpu_load_action():
    director.start(CpuLoadWorker(driver))
    return 'CPU Load'


def stop():
    director.stop()
    driver.clear()
    driver.show()
    print("Bye bye")


if __name__ == '__main__':
    atexit.register(stop)
    app.run(host='0.0.0.0', port=port)
