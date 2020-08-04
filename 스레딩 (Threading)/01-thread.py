# -- coding: utf-8 --
# 파이썬에서 제공하는 고수준 스레드 모듈인 `threading` 을 import하자.
# thread 라는 저수준의 스레드 모듈도 존재하나, 이는 deprecated 상태이며 가급적이면 threading을 사용할 것을 권장한다.
import threading


# 파이썬의 threading 모듈은 두가지 방식으로 사용할 수 있다.
# 첫 번째는, 스레드에서 처리할 작업을 작성해둔 함수를 target으로 지정해 스레드를 생성하는 방식이다.
def my_thread_task(low: int, high: int, name: str = threading.current_thread().getName()):
    print(f"Thread name : {name} is starting the task...")
    sum: int = 0
    for num in range(low, high):
        sum += num
        print(f"[Thread {name}] Current sum : {sum}")
    print(f"Thread name : {name} has finished the task!")


func_style_thread = threading.Thread(target=my_thread_task, args=(0, 10), name="Func Style Thread")


# 두 번째는, threading 모듈 내부의 Thread 클래스를 상속하는 새 클래스를 정의한 후 객체를 생성하는 방식이다.
class MyThread(threading.Thread):
    def __init__(self, low: int, high: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.low = low
        self.high = high

    def run(self):
        """
        Thread 클래스를 상속해 만든 새 스레드 클래스는 스레드가 동작하는 동안 진행할 작업을 담은 run() 함수를 정의해야 한다.
        허나 스레드를 실행할 때 직접 run()함수를 호출하지는 않고, {(? extends Thread)의 객체}.start() 를 사용할 때 스레드가 내부의 run()함수를 찾아 실행하게 된다.
        """
        print()
        my_thread_task(low=self.low, high=self.high, name=self.getName())


class_style_thread = MyThread(low=0, high=10, name="Class Style Thread")

# 생성한 스레드는 start() 메소드를 사용해 실행한다.
func_style_thread.start()
class_style_thread.start()
# join() 메소드를 사용하면 메인 프로세스가 이 스레드가 종료될 때 까지 기다리도록 할 수 있다.
func_style_thread.join()
class_style_thread.join()
