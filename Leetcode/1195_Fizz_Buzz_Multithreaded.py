from threading import Lock
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.counter = 1
        self.lock = Lock()
    def fizz(self, printFizz):
        while self.counter <= self.n:
            with self.lock:
                if self.counter <= self.n and self.counter %3 == 0 and self.counter %5 != 0:
                    printFizz()
                    self.counter +=1
    def buzz(self, printBuzz):
        while self.counter <= self.n:
            with self.lock:
                if self.counter <= self.n and self.counter %3 != 0 and self.counter %5 == 0:
                    printBuzz()
                    self.counter +=1
    def fizzbuzz(self, printFizzBuzz):
        while self.counter <= self.n:
            with self.lock:
                if self.counter <= self.n and self.counter % 15 == 0:
                    printFizzBuzz()
                    self.counter +=1
    def number(self, printNumber):        
        while self.counter <= self.n:
            with self.lock:
                if self.counter <= self.n and self.counter %3 > 0 and self.counter %5 > 0:
                    printNumber(self.counter)
                    self.counter +=1