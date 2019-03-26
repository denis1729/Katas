import asyncio


class Operations:
    def __init__(self, numbers: [int] = []):
        self.numbers = numbers

    async def multiply(self, number):
        result = number * number
        await asyncio.sleep(number)
        print('The suma is =', self.sumar(number))
        return result

    async def steps(self, number):
        result = await self.multiply(number)
        print("result: %s" % result)

    async def run_all(self, numbers: [int] = []):
        if len(numbers) > 0:
            self.numbers = numbers

        if len(self.numbers) <= 0:
            raise ValueError('No transactions to be ran')
        tasks = []
        for tnx in self.numbers:
            tasks.append(self.steps(tnx))
        results = await asyncio.gather(*tasks)

    def sumar(self, number):
        result = number + number
        return result


if __name__ == '__main__':
    data = [2, 4, 5, 1, 6]
    tnx = Operations(data)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tnx.run_all())
    loop.close()
