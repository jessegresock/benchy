import time


def measure_time(func, *args, **kwargs):
    """
    Executes `func` with the provided arguments and measures the time of execution in seconds

    Parameters:
        :func: Function to be executed
        :*args: Arguments to be passed to the function
        :**kwargs: Keyword arguments to be passed to the function
    
    Returns:
        :result, elapsted_time_in_seconds tuple:
    """
    start_time = time.time()
    func_return = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time_in_seconds = end_time - start_time

    return func_return, elapsed_time_in_seconds
