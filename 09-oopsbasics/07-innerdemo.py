class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    class Engine:
        def __init__(self, number):
            self.number = number
        def start(self):
            print("Engine Started")

c = Car("BMW", 2019)
e = c.Engine(123)
e.start()