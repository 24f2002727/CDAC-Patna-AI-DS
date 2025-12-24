"""
WAP to create a class called Reservation with attributes for reservatiion ID, customer name, 
and date.Create subclass "ResortReservation" and "RailwayReservation" that add specific attribute
like room number for hotels and seat number for rail. Implement methods to check reservation status 
and modify reservation details.

"""
class Reservation:
    def __init__(self, reservation_id: int, customer_name: str, date: str):
        self.reservation_id = reservation_id
        self.customer_name = customer_name
        self.date = date

    def check_reservation(self):
        return "Reservation status unknown"

    def update_reservation(self):
        pass


class ResortReservation(Reservation):
    def __init__(self, reservation_id, customer_name, date, room_no: int):
        super().__init__(reservation_id, customer_name, date)
        self.room_no = room_no  # -1 means waiting

    def check_reservation(self):
        if self.room_no < 0:
            return "Resort reservation is waiting"
        return "Resort reservation is confirmed"

    def update_reservation(self, room_no):
        self.room_no = room_no


class RailwayReservation(Reservation):
    def __init__(self, reservation_id, customer_name, date, seat_no: int):
        super().__init__(reservation_id, customer_name, date)
        self.seat_no = seat_no  # -1 means waiting

    def check_reservation(self):
        if self.seat_no < 0:
            return "Railway reservation is waiting"
        return "Railway reservation is confirmed"

    def update_reservation(self, seat_no):
        self.seat_no = seat_no


# ---- Testing ----
resort = ResortReservation(1, "Ram", "25/12/2026", -1)
print(resort.check_reservation())
resort.update_reservation(101)
print(resort.check_reservation())

rail = RailwayReservation(2, "Shyam", "30/12/2026", -1)
print(rail.check_reservation())
rail.update_reservation(45)
print(rail.check_reservation())