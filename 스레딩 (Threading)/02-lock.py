import time
import threading

count = 0

def increase():
    global count
    while count < 10:
        count += 1
        print("count increase 1")
        time.sleep(1)


def decrease():
    global count
    while count > -10:
        count -= 1
        print("count decrease 1")
        time.sleep(1)

def main():
    pass