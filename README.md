# Simple web service for Pimoroni Blinkt examples 

This is a simple Flask webservice to run few of the [Pimoroni Blinkt](https://shop.pimoroni.com/products/blinkt)
code examples.

## Running the webservice

```bash
cd src
python app.py
```

## Available end-points

 * /clear    - will clear the LEDs
 * /rainbow  - will run the rainbow.py example
 * /larson   - will run the larson.py example
 * /cpu-load - will run the cpu-load.py example
 * /mem-load - will run the mem-load.py example
 * /graph - will run the graph.py example
 
## Pimoroni library abstraction

In order to be able to run this webservice without having the actual Blinkt attached,
the code wraps the calls to the Pimoroni library in `BlinktDriver.py`.

If the import of the Blinkt library failed, the calls will be displayed on the console.

## Implementing more examples

Each example is implemented in a class in `Blinkt/Workers`.

This class must implement the `Blinkt/Workers/Worker` interface.

In a Worker class you can use:

 * `self.interval` is the time interval to call the worker (default 1 second)
 * `self.driver`  is a reference to the Blinkt library abstraction interface
 * the `__init__(self, driver: BlinktDriver)` constructor (be sure to call the superclass constructor)
 * the `initialize()` method is called once when the worker is started
 * the `work()` method is called repeatedly 
 
 When implementing new Worker classes, an end-point must be created in app.py so that it can be
 called remotely.
 
 ## Simple worker example
 
 This one will clear the LEDs, then do nothing.
 
 ```python
from BlinkIt.Workers.Worker import Worker

class DummyWorker(Worker):
    def initialize(self):
        self.driver.clear()
        self.driver.show()
```

Add an end-point in app.py:

```python
from BlinkIt.Workers import DummyWorker

# ...

@app.route('/dummy')
def dummy_action():
    director.start(DummyWorker(driver))
    return 'Dummy'
```

## References

 * [Pimoroni Blinkt python library documentation](http://docs.pimoroni.com/blinkt)
 * [Pimoroni blinkt python library](https://github.com/pimoroni/blinkt)
 * [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/#what-is-a-thread)
 * [Flask user guide](https://flask.palletsprojects.com/en/1.1.x/)
