##########################################################################################
#
# See: https://docs.python.org/3/library/concurrent.futures.html?highlight=concurrency%20future#concurrent.futures.ThreadPoolExecutor
#
##########################################################################################

import time
from concurrent.futures import ThreadPoolExecutor


def wait_on_b():
    time.sleep(5)
    print(b.result())  # b will never complete because it is waiting on a.
    return 5


def wait_on_a():
    time.sleep(5)
    print(a.result())  # a will never complete because it is waiting on b.
    return 6


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    a = executor.submit(wait_on_b)
    b = executor.submit(wait_on_a)
    # There is a need for a print() call in the main thread to get output from the
    # worker thread.
    print('__main__ exiting...')
