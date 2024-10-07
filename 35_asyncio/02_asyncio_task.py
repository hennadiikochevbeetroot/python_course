import asyncio
import datetime


# simulate fetching of data which is I/O operation taking time
async def fetch_data(delay: int, result: str):
    await asyncio.sleep(delay)
    return result


async def main():
    tasks = [
        asyncio.create_task(fetch_data(1, 'Result 1')),
        asyncio.create_task(fetch_data(2, 'Result 2')),
        asyncio.create_task(fetch_data(3, 'Result 3'))
    ]

    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    asyncio.run(main())
    end_time = datetime.datetime.now()
    print('Diff time: ', end_time - start_time)
