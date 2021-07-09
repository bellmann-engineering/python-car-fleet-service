from car_fleet.driver_license import DriverLicense
from datetime import date
from dataclasses import dataclass, field


@dataclass
class Vehicle:
    # Vehicle identification number ISO3779, ISO4030
    vin: str
    license_plate: str = field(default=None, compare=False)
    manufacturer: str = field(default=None, compare=False)
    manufacture_date: date = field(default=None, compare=False)
    model_name: str = field(default=None, compare=False)
    driver_license: DriverLicense = field(default=None, compare=False)

    def can_drive(self, drivers_license: DriverLicense) -> bool:
        print(type(self))
        print(type(self.driver_license))
        print(type(drivers_license))

        return (self.driver_license in drivers_license)


@dataclass
class Car(Vehicle):
    pass


@dataclass
class Truck(Vehicle):
    maximum_payload: float = field(default=0, compare=False)


@dataclass
class Motorcycle(Vehicle):
    fuel_tank: float = field(default=0, compare=False)
