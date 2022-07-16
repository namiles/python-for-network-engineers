import asyncio

"""
Asyncio is a built-in module that cann be used for concurrency. 
- Ideal for I/O bound tasks.
- Based on coroutines, which are essentially a wrapped version of functions that enable them to be ran aynchronously
- Uses async / await keywords.
- Async is wrapped around functions, and returns a coroutine object
- await keyword can only be used inside of an async function
- asyncio.run() is used to run the main coroutine, which creates the lower level event loop and adds items to it
- asyncio.create_task() is used to create tasks and run them, but continues running other parts of code while the task is waiting
- tasks can be awaited with the await keyword
"""


async def fetch_data():
    print("Start fetch")
    await asyncio.sleep(2)
    print("Done Fetching")
    return {"data": 1}


async def print_numbers():
    for i in range(11):
        print(i)
        await asyncio.sleep(0.50)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    # When a task is created for a coroutine that returns a value, {'data': 1} in this example, that is known as a future.
    # a future is like a placeholder for a value that will exist once ready
    task1_value = await task1
    print(task1_value)
    await task2


if __name__ == "__main__":
    asyncio.run(main())
