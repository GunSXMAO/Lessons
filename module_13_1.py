import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        print(f'Силач {name} поднял {power}')
        await asyncio.sleep(5/power)
    print(f'Силач {name} закончил соревнование.')

async def start_tournament():
    one = asyncio.create_task(start_strongman('Pasha', 3))
    two = asyncio.create_task(start_strongman('Denis', 4))
    three = asyncio.create_task(start_strongman('Apollon', 5))
    await one
    await two
    await three

asyncio.run(start_tournament())
