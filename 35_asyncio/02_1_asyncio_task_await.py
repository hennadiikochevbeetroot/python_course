import asyncio
import datetime


# simulate fetching of data which is I/O operation taking time
async def fetch_data(delay: int, result: str):
    await asyncio.sleep(delay)
    return result


async def main():
    task1 = asyncio.create_task(fetch_data(1, 'Result 1'))
    task2 = asyncio.create_task(fetch_data(2, 'Result 2'))
    task3 = asyncio.create_task(fetch_data(3, 'Result 3'))

    # results = await asyncio.gather(*tasks)
    result1 = await task1
    result2 = await task2
    result3 = await task3
    print(result1)
    print(result2)
    print(result3)


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    asyncio.run(main())
    end_time = datetime.datetime.now()
    print('Diff time: ', end_time - start_time)
