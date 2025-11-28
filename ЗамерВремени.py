import time

def timer(func):
    def obertka(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} выполнена за {end - start:.5f} сек")
        return result
    return obertka

@timer
def test_func(n):
    time.sleep(n)
    return n * 2

test_func(1)