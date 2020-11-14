import multiprocessing
import time
def foo():
    if p.is_alive()
        print('function terminated')
        p.terminate()
        p.join()
    a_long_time = 10000000
    time.sleep(a_long_time)

TIMEOUT = 5 # seconds
if __name__ == '__main__':
    p = multiprocessing.Process(target=foo, name="Foo")
    p.start()

    p.join(TIMEOUT)

    if p.is_alive()
        print('function terminated')
        p.terminate()
        p.join()