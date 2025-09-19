#! /usr/bin/env python3

# Polymorphism challenge

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def vehicle_info(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def vehicle_info(self):
        return f"{self.year} {self.brand} {self.model} - Doors: {self.doors}"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type

    def vehicle_info(self):
        return f"{self.year} {self.brand} {self.model} - Type: {self.type}"

Vehicles = [Car("Toyota", "Land Cruiser", 2020, 4), Motorcycle("Ducati", "Street 750", 2019, "Cruiser")]

for v in Vehicles:
    print(v.vehicle_info())
