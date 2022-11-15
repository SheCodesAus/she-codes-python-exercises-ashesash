class Vehicle:
    def __init__(self, make, model, colour, seat_capacity, max_speed):
        self.make = make
        self.model = model
        self.colour = colour
        self.seat_capacity = seat_capacity
        self.max_speed = max_speed

    def __str__(self):
        return f"The make of the car is {self.make} \n The model of the car is {self.model} \n The colour of the car is {self.colour} \n The seating capacity of the car is {self.seat_capacity} \n The maximum speed of the car is {self.max_speed} km/h \n"

    def rev_engine(self):
        print("VRRRMMMMMMMMMMMMMMMMMM")

    def fuel(self):
        #units in litres
        max_fuel_capacity = 300
        fuel_consumption_per_km = 10
        distance_travelled = int(input("how much have you travelled in kms? "))
        fuel_left = max_fuel_capacity - (distance_travelled * fuel_consumption_per_km)
        #adding int in front of distance travelled gives me weird values
        print(f"the fuel left is {fuel_left}")
        if fuel_left < 30:
            print("refuel ASAP")
        else:
            print("you're good")


car = Vehicle("Toyota", "Corolla", "Grey", 5, 200)
print(car)
car.rev_engine()
#WHY DOES print(car.rev_engine()) give None
car.fuel()
