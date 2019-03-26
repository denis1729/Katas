import threading
import time


class Operations:
    def __init__(self, numbers: [int] = []):
        self.numbers = numbers

    def multiply(self, number):
        result = number * number
        time.sleep(number)
        print('The suma is =', self.sumar(number))
        return result

    def steps(self, number):
        result = self.multiply(number)
        print("result: %s" % result)

    def run_all(self, numbers: [int] = []):
        if len(numbers) > 0:
            self.numbers = numbers

        if len(self.numbers) <= 0:
            raise ValueError('No transactions to be ran')
        for tnx in self.numbers:
            t = threading.Thread(target=self.steps, args=(tnx,))
            t.start()

    def sumar(self, number):
        result = number + number
        return result


if __name__ == '__main__':
    data = [2, 4, 5, 1, 6]
    tnx = Operations(data)
    tnx.run_all()
