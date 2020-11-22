import socket
import psutil

from flask import Blueprint, render_template
from pprint import pprint


def create_routes():
    routes = Blueprint('info', __name__, url_prefix='/info')

    @routes.route('/')
    def index_action():
        return render_template("info/index.html",
                               HostName=socket.gethostname(),
                               CpuCount=psutil.cpu_count(),
                               CpuPercent=psutil.cpu_percent(),
                               CpuFreq=psutil.cpu_freq().max,
                               Mem=psutil.virtual_memory(),
                               Swap=psutil.swap_memory(),
                               Partitions=psutil.disk_partitions(),
                               psutil=psutil
                               )

    return routes
