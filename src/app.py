import atexit
from sys import exit

from Controllers.ExamplesController import create_routes as create_examples_routes

try:
    import psutil
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install psutil")

try:
    from flask import Flask
except ImportError:
    exit("This script requires the flask module\nInstall with: sudo pip install flask")

from Blinkt import LedDirector, BlinktDriver

app = Flask(__name__)

port = 5000

director = LedDirector()
driver = BlinktDriver()


app.register_blueprint(create_examples_routes(director, driver))


@app.route('/')
def hello_world():
    return 'Hello World! I am running on port ' + str(port)


def stop():
    director.stop()
    driver.clear()
    driver.show()
    print("Bye bye")


if __name__ == '__main__':
    atexit.register(stop)
    app.run(host='0.0.0.0', port=port)
