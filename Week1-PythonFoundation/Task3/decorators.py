import time

def execution_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution Time: {end - start:.4f} seconds")
    return wrapper


@execution_time
def sample_function():
    total = 0
    for i in range(1000000):
        total += i
    print("Function executed")


sample_function()
