#Clockblocks solves the first of these problems by defining CREDIT TO CLODEBLOCKS
# a sleep_precisely function which repeatedly sleeps
# for half the remaining duration until fewer than 500μs
# are left, at which point it implements a busy wait for the
# remaining time. 

import time
def _sleep_precisely_until(stop_time):
    time_remaining = stop_time - time.time()
    if time_remaining <= 0:
        return
    elif time_remaining < 0.0005:
        # when there's not much left, just burn cpu cycles and hit it exactly
        while time.time() < stop_time:
            pass
    else:
        time.sleep(time_remaining / 2)
        _sleep_precisely_until(stop_time)


def sleep_precisely(secs):
    _sleep_precisely_until(time.time() + secs)

def until_sleep(secs):
    now = time.perf_counter()
    end = now + secs
    while now < end:
        now = time.perf_counter()