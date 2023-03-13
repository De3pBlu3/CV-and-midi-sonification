import time

def run_function_at_time(func, t):
    """
    Runs the given function at the specified time.

    Arguments:
    func -- the function to run
    t -- the time at which to run the function, in seconds since the epoch
    """
    now = time.time()
    delay = max(0, t - now)
    time.sleep(delay)
    func()

def create_timeline(duration, function_times):
    """
    Creates a timeline of when to run functions within the specified duration.

    Arguments:
    duration -- the duration of the timeline, in seconds
    function_times -- a list of tuples containing functions and the times at which to run them,
                      where each time is in seconds since the epoch

    Returns:
    A list of tuples containing the function, the time at which it was run, and the duration of the function
    """
    timeline = []
    start_time = time.time()

    for func, time_to_run in function_times:
        timeline.append((func.__name__, time_to_run, 0))
        run_function_at_time(func, time_to_run)

        # Calculate duration of the function
        end_time = time.time()
        duration = end_time - start_time
        timeline[-1] = (func.__name__, time_to_run, duration)

    return timeline

# Example usage:
def func1():
    print("Function 1 ran.")

def func2():
    print("Function 2 ran.")

function_times = [
    (func1, time.time() + 5),  # Run func1 in 5 seconds from now
    (func2, time.time() + 5),  # Run func2 in 5 seconds from now
    (func2, time.time() + 10), # Run func2 in 10 seconds from now
]

timeline = create_timeline(20, function_times)
print(timeline)
