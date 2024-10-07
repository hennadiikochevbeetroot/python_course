import asyncio


async def long_task():
    print("Task started, doing some work...")
    try:
        await asyncio.sleep(5)
        print("Task completed successfully!")
        return "Long task is finished"
    except asyncio.CancelledError:
        print("Task was cancelled!")
        raise


async def main():
    task = asyncio.create_task(long_task())

    # Do something while the task is running
    await asyncio.sleep(2)
    print("Main function doing other work...")
    if task.done():
        result = task.result()
        print('Result:', result)
    else:
        task.cancel()

    try:
        result = await task
    except asyncio.CancelledError:
        print("The task was cancelled and could not complete.")
    else:
        print(f"Task completed with result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
