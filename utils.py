
import time

def get_current_time():

    return time.time()

def get_time_diff(start):

    return abs(start - time.time())

def get_time_diff_ms(start):

    return get_time_diff(start) * 1000

