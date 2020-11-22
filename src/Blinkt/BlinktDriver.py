HAS_BLINKT = False

try:
    import blinkt
    HAS_BLINKT = True
except ImportError:
    pass

class BlinktDriver(object):
    """
    Wraps the call to the Pimoroni Blinkt library.
    If import of blinkt library failed, this class will output to the console
    instead of trying to call the Pimoroni hardware.
    """

    NUM_PIXELS = 8

    def __init__(self):
        if (HAS_BLINKT):
            BlinktDriver.NUM_PIXELS = blinkt.NUM_PIXELS

    def set_pixel(self, pixel_no, red, green, blue, brightness = 1):
        if HAS_BLINKT:
            blinkt.set_pixel(pixel_no, red, green, blue, brightness)
        else:
            print("""set_pixel({}, {}, {},{})""".format(pixel_no, red, green, blue, brightness))

    def set_all(self, red, green, blue, brightness = 1):
        if HAS_BLINKT:
            blinkt.set_all(red, green, blue, brightness)
        else:
            print("""set_all({}, {},{})""".format(red, green, blue, brightness))

    def set_brightness(self, brightness):
        if HAS_BLINKT:
            blinkt.set_brightness(brightness)
        else:
            print("""set_brightness({})""".format(brightness))

    def set_clear_on_exit(self, value = False):
        if HAS_BLINKT:
            blinkt.set_clear_on_exit(value)
        else:
            print("""set_clear_on_exit({})""".format(value))

    def clear(self):
        if HAS_BLINKT:
            blinkt.clear()
        else:
            print("clear()")

    def show(self):
        if HAS_BLINKT:
            blinkt.show()
        else:
            print("show()")
