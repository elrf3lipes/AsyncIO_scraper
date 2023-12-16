import asyncio

async def main():
    task = asyncio.create_task(other_function()) # once we have some idle time it will call 'other_function'
    print("A") # print this first
    await asyncio.sleep(1) # give idle time to execute 'other_function'
    print("B")
    return_value = await task
    print(f"Return value was {return_value}")

async def other_function():
    print("1")
    await asyncio.sleep(2) # give idle time to execute 'main'
    print("2")
    return 10

asyncio.run(main()) # calling the function