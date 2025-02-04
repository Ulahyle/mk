from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_name, user_type):
        self.user_name = user_name
        self.user_type = user_type
    
    @abstractmethod
    def add_user(self):
        pass
    
    @abstractmethod
    def delete_user(self):
        pass

class Client(User):
    def __init__(self, user_name, user_type):
        super().__init__(user_name, user_type)


    def add_user(self):
        pass

    def delete_user(self):
        pass


class Driver(User):
    def __init__(self, user_name, user_type):
        super().__init__(user_name, user_type)


    def add_user(self):
        pass

    def delete_user(self):
        pass
        

class Vehicle(ABC):
    def __init__(self, vehicle_id, driver, is_available = None):
        self.vehicle_id = vehicle_id
        self.driver = driver
        self.is_available = is_available

    @abstractmethod
    def add_vehicle(self):
        pass

    @abstractmethod
    def delete_vehicle(self):
        pass

class Truck(Vehicle):
    def __init__(self, vehicle_id, driver, is_available):
        super().__init__(vehicle_id, driver, is_available)

    def add_vehicle(self):
        pass

    def delete_vehicle(self):
        pass

class Sedan(Vehicle):
    def __init__(self, vehicle_id, driver, is_available):
        super().__init__(vehicle_id, driver, is_available)

    def add_vehicle(self):
        pass

    def delete_vehicle(self):
        pass

class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, driver, is_available):
        super().__init__(vehicle_id, driver, is_available)

    def add_vehicle(self):
        pass

    def delete_vehicle(self):
        pass


class TaxiAgency(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def add_taxi(self, vehicle: Vehicle):
        pass

    @abstractmethod
    def delete_taxi(self, vehicle: Vehicle):
        pass

class TelTaxi(TaxiAgency):
    def __init__(self, name):
        super().__init__(name)

    def add_taxi(self, vehicle: Vehicle):
        pass

    def delete_taxi(self, vehicle):
        pass

class InternetTaxi(TaxiAgency):
    def __init__(self, name):
        super().__init__(name)

    def add_taxi(self, vehicle: Vehicle):
        pass

    def delete_taxi(self, vehicle):
        pass

class ClassicTaxi(TaxiAgency):
    def __init__(self, name):
        super().__init__(name)

    def add_taxi(self, vehicle: Vehicle):
        pass

    def delete_taxi(self, vehicle):
        pass

class Booking:
    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def assign(self, client: Client):
        self.vehicle.is_available = client
        
    def release(self):
        self.vehicle.is_available = None

