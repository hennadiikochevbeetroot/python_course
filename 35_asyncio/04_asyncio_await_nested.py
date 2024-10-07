import asyncio
import datetime


async def inner(delay: int) -> str:
    await asyncio.sleep(delay)
    return f'inner result {delay}'


async def outer(delay: int) -> str:
    inner_result = await inner(delay)
    await asyncio.sleep(delay)
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
