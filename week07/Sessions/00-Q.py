from abc import ABC,abstractmethod

class Car(ABC):
    def __init__(self, model, client, price):
        self.model = model
        self.client = client
        self.price = price
        self.is_availajble = True

    @abstractmethod
    def make_car(self):
        pass

    @abstractmethod
    def sell_car(self):
        self.is_available = False


class GasCarck(Car):
    def __init__(self, model, client, price):
        super().__init__(model, client, price)

    def make_car(self):
        pass

    def sell_car(self):
        self.is_available = False


class ElectricCar(Car):
    def __init__(self, model, client, price):
        super().__init__(model, client, price)

    def make_car(self):
        pass

    def sell_car(self):
        self.is_available = False

class Dealership:
    def __init__(self):
        self.car = []
