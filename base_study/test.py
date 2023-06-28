import multiprocessing
import multiprocessing.pool
import time


class NoDaemonProcess(multiprocessing.Process):
    # make 'daemon' attribute always return False
    def _get_daemon(self):
        return False

    def _set_daemon(self, value):
        pass

    daemon = property(_get_daemon, _set_daemon)


# We sub-class multiprocessing.pool.Pool instead of multiprocessing.Pool
# because the latter is only a wrapper function, not a proper class.
class NoDaemonProcessPool(multiprocessing.pool.Pool):
    Process = NoDaemonProcess


def work(index):
    count = 5
    while (count > 0):
        print("Process %s is running in round %d..." % (index, 6 - count))
        time.sleep(1)
        count -= 1


def foo(index):
    worker_number = 4
    process_pool = multiprocessing.Pool(worker_number)

    for i in range(worker_number):
        worker_index = "%s.%s" % (index, i)
        process_pool.apply_async(work, (worker_index,))

    process_pool.close()
    process_pool.join()


def test_pool():
    process_number = 2
    process_pool = NoDaemonProcessPool(process_number)

    process_pool.map(foo, range(process_number))

    process_pool.close()
    process_pool.join()

    print("Test ends")


def main():
    test_pool()


if __name__ == '__main__':
    main()
