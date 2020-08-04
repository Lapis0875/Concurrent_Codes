import asyncio


# async def 로 선언한 함수는 호출시 함수(function 객체)가 아닌 코루틴(Coroutine 객체)가 됩니다.
async def coroutine(n: int):
    print("This is Coroutine!")
    return n

def callback_func(task: asyncio.Task) -> str:
    print(f"number is {task.result()}")
    return str(task.result())


async def main():
    task: asyncio.Task = asyncio.create_task(coro=coroutine(n=30))

    print(f"Is the `task` done? {task.done()}")
    task.add_done_callback(callback_func)
    await task
    print(f"Is the `task` done? {task.done()}")

asyncio.run(main())