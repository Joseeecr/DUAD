class Person:
    def __init__(self, passenger):
        self.passenger = passenger


class Bus:
    max_passengers = 5

    def __init__(self):
        self.current_passengers = 0

    def get_on_bus(self, person):
        if self.current_passengers < Bus.max_passengers:
            self.current_passengers += 1
            print(f"Current passengers: {self.current_passengers}")
        else:
            print("The bus is completely full")

    def get_off_bus(self):
        if self.current_passengers > 0:
            self.current_passengers -= 1
            print(f"Current passengers: {self.current_passengers}")
        else:
            print("The bus is already empty")


my_person = Person(1)
my_bus = Bus()

my_bus.get_on_bus(my_person.passenger)
my_bus.get_on_bus(my_person.passenger)

my_bus.get_off_bus()
my_bus.get_off_bus()
my_bus.get_on_bus(my_person.passenger)
my_bus.get_on_bus(my_person.passenger)
my_bus.get_on_bus(my_person.passenger)
my_bus.get_on_bus(my_person.passenger)
my_bus.get_on_bus(my_person.passenger)
my_bus.get_on_bus(my_person.passenger)
my_bus.get_off_bus()
my_bus.get_off_bus()
my_bus.get_off_bus()
my_bus.get_off_bus()
my_bus.get_off_bus()
my_bus.get_off_bus()