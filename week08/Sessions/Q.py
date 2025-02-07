class Flight:
    def __init__(self, flight_number: str, destination: str, departure_time: str, available_seats: int):
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.available_seats = available_seats
        self.booked_passengers = []

    def is_seat_available(self):
        return self.availabel_seats > 0

    def book_ticket(self, passenger):
        if self.available_seats == 0:
            return "Sorry! No other seats are available!"
        else:
            self.booked_passengers.append(passenger)
            self.available_seats -= 1
            return self.booked_passengers

    def get_details(self):
        return f"flight number: {self.flight_number}, departure time: {self.departure_timer}"


class Passenger:
    def __init__(self, name: str, passport_number: str, contact_info: str):
        self.name = name
        self.passport_number = passport_number
        self.contact_info = contact_info

    def get_details(self):
        return f"name: {self.name}, passport number: {self.passport_number}, contact information: {self.contact_info}"


class Booking:
    def __init__(self, flight: Flight, passenger: Passenger, seat_number: str):
        self.flight = flight
        self.passenger = passenger
        self.seat_number = seat_number

    def get_booking_info(self):
        return self.passenger.get_details(), self.flight.get_details()



flight1 = Flight(flight_number="A123", destination="Paris",
                 departure_time="15:30", available_seats=2)
flight2 = Flight(flight_number="B456", destination="London",
                 departure_time="18:45", available_seats=1)

passenger1 = Passenger(
    name="John Doe", passport_number="J1234567", contact_info="john@example.com")
passenger2 = Passenger(
    name="Alice Smith", passport_number="A9876543", contact_info="alice@example.com")

flight1.book_ticket(passenger1)
flight1.book_ticket(passenger2)
book3 = flight1.book_ticket(Passenger(
    name="Bob White", passport_number="B6543210", contact_info="bob@example.com"))
print(book3)
for passenger in flight1.booked_passengers:
    print(passenger.name)
