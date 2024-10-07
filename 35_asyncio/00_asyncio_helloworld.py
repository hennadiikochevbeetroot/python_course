import asyncio


async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')
    return "YES"


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main())
    print(result)
