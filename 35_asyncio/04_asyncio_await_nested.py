import asyncio
import datetime


async def inner(delay: int) -> str:
    await asyncio.sleep(delay)
    return f'inner result {delay}'


async def outer(delay: int) -> str:
    tasks = [
        asyncio.create_task(inner(delay)),
        asyncio.create_task(asyncio.sleep(delay)),
    ]
    results = await asyncio.gather(*tasks)
    inner_result = results[0]
    outer_result = f'outer result: {inner_result}'
    return outer_result


async def main():
    final_result = await outer(2)
    print('Final result:', final_result)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    asyncio.run(main())
    end_time = datetime.datetime.now()
    print('Diff time: ', end_time - start_time)
