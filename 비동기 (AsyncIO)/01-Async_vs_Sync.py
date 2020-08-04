# -- coding: utf-8 --
import asyncio
from time import time, sleep


# 동기식 sleep 호출
def sleep_test(i):
    print("start sleep {}".format(i))
    sleep(1.0)


begin = time()
for i in range(0, 5):
    sleep_test(i)
end = time()
print("동기로 실행 시간: {0:.3f}초\n\n".format(end - begin))


# 비동기식 sleep 호출
async def async_sleep_test(i):
    print("start sleep {}".format(i))
    await asyncio.sleep(1.0)


async def main():
    aws = [async_sleep_test(i) for i in range(0, 5)]
    await asyncio.gather(*aws)


begin = time()
loop = asyncio.get_event_loop()  # 이벤트 루프를 얻음
loop.run_until_complete(main())  # main이 끝날 때까지 기다림
loop.close()  # 이벤트 루프를 닫음
end = time()
print("비동기로 실행 시간: {0:.3f}초".format(end - begin))

asyncio.all_tasks(asyncio.get_event_loop())
