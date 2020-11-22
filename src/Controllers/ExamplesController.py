from flask import Blueprint

from Blinkt.Workers import \
    DummyWorker, RainbowWorker, LarsonWorker, CpuLoadWorker, GraphWorker, MemLoadWorker, \
    CandleWorker


def create_routes(director, driver):
    routes = Blueprint('leds', __name__, url_prefix='/blinkt')

    @routes.route('/rainbow')
    def rainbow_action():
        director.start(RainbowWorker(driver))
        return 'Rainbow'

    @routes.route('/clear')
    def clear_action():
        director.start(DummyWorker(driver))
        return 'Dummy'

    @routes.route('/larson')
    def larson_action():
        director.start(LarsonWorker(driver))
        return 'Larson'

    @routes.route('/candle')
    def candle_action():
        director.start(CandleWorker(driver))
        return 'Larson'

    @routes.route('/cpu-load')
    def cpu_load_action():
        director.start(CpuLoadWorker(driver))
        return 'CPU Load'

    @routes.route('/mem-load')
    def mem_load_action():
        director.start(MemLoadWorker(driver))
        return 'Memory Load'

    @routes.route('/graph')
    def graph_action():
        director.start(GraphWorker(driver))
        return 'Graph'

    return routes
