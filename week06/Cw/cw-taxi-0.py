# class User:
#     def __init__(self, user_id, user_name, user_type):
#         self.user_id = user_id
#         self.user_name = user_name
#         self.user_type = user_type

# class Taxi:
#     def __init__(self, free_taxi, busy_taxi, out_of_service):
#         self.free_taxi = free_taxi
#         self.busy_taxi = busy_taxi
#         self.out_of_service = out_of_service

# class Booking:
#     def __init__(self, )
        


from abc import ABC, abstractmethod
class User:
    def __init__(self, name,user_type):
        self.name = name
        self.user_type = user_type
    
    def __str__(self):
        return f"name: {self.name}, user_type: {self.user_type}"
    

class Taxi(ABC):
    taxies = []
    def __init__(self, taxi_type):
        self.taxi_type = taxi_type
        self._state_taxi = True
        Taxi.taxies.append(self)

    @abstractmethod
    def add_taxi(self):
        pass
    
    @property
    @abstractmethod
    def state_taxi(self):
        #True available
        #False not available
        pass    
    
    
class InternetTaxi(Taxi):
    def __init__(self, name):
        super().__init__("InternetTaxi")
        self.name = name

    def add_taxi(self):
        pass

    def state_taxi(self):
        pass   

class TelTaxi(Taxi):
    def __init__(self):
        super().__init__("TelTaxi")

    def add_taxi(self):
        pass
        
    def state_taxi(self):
        pass       
    
class ClassicTaxi(Taxi):
    def __init__(self):
        super().__init__("ClassicTaxi")

    def add_taxi(self):
        pass

    def state_taxi(self):
        pass                     



class Booking:
    def __init__(self):
        pass

    def reserve(self):
        pass
        
    def release(self): 
        pass
    
    def book_taxi(self, taxi):
        if not taxi.state_taxi:
            raise ValueError("the taxi has booked")
        else:
            taxi.reserve()


# taxi1 = TelTaxi()
# print(Taxi.taxies)
# # taxi1.release()
# # print(taxi1._state_taxi)
# booked_taxi1 = Booking()
# booked_taxi1.book_taxi(taxi1)

t_snapp = InternetTaxi("snapp")
t_snapp.add_taxi()
t_snapp.add_taxi()
t_snapp.add_taxi()
t_snapp.add_taxi()

t_tapsi = InternetTaxi("tapsi")
t_tapsi.add_taxi()
t_tapsi.add_taxi()
t_tapsi.add_taxi()
t_tapsi.add_taxi()


