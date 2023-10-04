##########################################################################################
#
# See: https://docs.python.org/3/library/concurrent.futures.html?highlight=concurrency%20future#concurrent.futures.ThreadPoolExecutor
#
##########################################################################################


from concurrent.futures import ThreadPoolExecutor


def wait_on_future():
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    print(f.result())
    # return 0


if __name__ == "__main__":
    # If number of workers are 2, there are enough threads to run the computation and
    # the main thread.
    # executor = ThreadPoolExecutor(max_workers=2)
    executor = ThreadPoolExecutor(max_workers=1)
    m_future = executor.submit(wait_on_future)
    # There is a need for a print() call in the main thread to get output from the
    # worker thread. Maybe this is to trigger the thread scheduler.
    print("__main__ exiting...")
    # print(f'Result: {m_future.result()}')
