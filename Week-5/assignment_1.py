#! /usr/bin/env python3

# Base class
class Device:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def device_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Inherited class
class Smartphone(Device):
    def __init__(self, brand, model, year, os, storage, battery):
        super().__init__(brand, model, year)
        self.os = os
        self.storage = storage
        self.battery = battery
        self.is_on = False

    # Encapsulation 
    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.device_info()} is now ON")
        else:
            print(f"{self.device_info()} is already ON")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.device_info()} is now OFF")
        else:
            print(f"{self.device_info()} is already OFF")

    def install_apps(self, app_name):
        if self.is_on:
            return f"Installing {app_name} on {self.device_info()}... Done ✅"
        else:
            return f"Cannot install apps on {self.device_info()} because it is OFF."
