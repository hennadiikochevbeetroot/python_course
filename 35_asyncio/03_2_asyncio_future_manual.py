import asyncio


async def set_future_value(future: asyncio.Future):
    await asyncio.sleep(1)  # Simulate some delay
    future.set_result("Task is complete!")  # Manually setting result


async def main():
    # Create an empty Future object
    future = asyncio.Future()

    # Start the task that will set the future's result
    _ = asyncio.create_task(set_future_value(future))

    print("Waiting for the future to complete...")
    result = await future  # Wait until the future has a result
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
