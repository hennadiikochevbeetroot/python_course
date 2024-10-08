import asyncio

# coroutine
# await
async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')
    return "YES"


if __name__ == "__main__":
    coro = main()
    asyncio.run(coro)
