import asyncio
import datetime


async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")
    return "Task 1 result"


async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")
    return "Task 2 result"


async def main():
    future1 = asyncio.ensure_future(task1())
    future2 = asyncio.ensure_future(task2())

    result1 = await future1
    print('proceed to next line')
    result2 = await future2

    print(result1)
    print(result2)


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    asyncio.run(main())
    end_time = datetime.datetime.now()
    print('Diff time: ', end_time - start_time)
