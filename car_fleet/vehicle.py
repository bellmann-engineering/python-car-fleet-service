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


@dataclass
class Car(Vehicle):
    doors: int = field(default=3, compare=False)


@dataclass
class Truck(Vehicle):
    maximum_payload: float = field(default=0, compare=False)


@dataclass
class Motorcycle(Vehicle):
    fuel_tank: float = field(default=0, compare=False)
