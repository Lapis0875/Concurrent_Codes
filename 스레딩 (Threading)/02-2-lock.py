from time import time, sleep
from threading import Thread, Lock

count = 0
lock = Lock()


def worker_A():
    global count
    lock.acquire()
    try:
        while count < 10:
            count += 1
            print(f"[worker A] increasing counter to {count}")
            sleep(1)
    finally:
        lock.release()


def worker_B():
    global count
    lock.acquire()
    try:
        while count > -10:
            count -= 1
            print(f"[worker B] decreasing counter to {count}")
            sleep(1)
    finally:
        lock.release()


def main():
    begin = time()
    workerA = Thread(target=worker_A)
    workerB = Thread(target=worker_B)
    workerA.start()
    workerB.start()
    workerA.join()
    workerB.join()
    end = time()
    print(f"execution time {end-begin}s")


if __name__ == '__main__':
    main()
