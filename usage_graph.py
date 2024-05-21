# usage_graph.py

import psutil

def get_processor_frequency():
    frequency = psutil.cpu_freq().current
    return frequency