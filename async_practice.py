import asyncio


# async def main():
#     print("Started")
#     task = asyncio.create_task(foo("Hello"))
#     await asyncio.sleep(3)
#     print("Almost Finished...")
#     await asyncio.sleep(1)
#     print("Finished")
#
#
#
# async def foo(text: str):
#     print(text)
#     await asyncio.sleep(2)
#     print("Semi finished")
#     await asyncio.sleep(3)
#     print("Still going...")


async def fetch_data():
    print("Start fetching...")
    await asyncio.sleep(2)
    print("Done fetching!")
    return {"data": 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2


asyncio.run(main())
