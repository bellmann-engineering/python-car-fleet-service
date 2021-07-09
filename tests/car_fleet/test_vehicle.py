import unittest
from datetime import date

from car_fleet.driver_license import DriverLicense
from car_fleet.person import Person
from car_fleet.vehicle import *


def _get_person() -> Person:
    driver_licenses = DriverLicense.A | DriverLicense.B | DriverLicense.C

    return Person(
        first_name="Vorname",
        last_name="Nachname",
        birth_date=date(1970, 1, 1),
        driver_license=driver_licenses
    )


class VehicleTests(unittest.TestCase):
    def test_a_valid_vehicle_type_should_be_set(self):
        self.assertRaises(
            InvaildVehicleTypeError,
            Vehicle,
            "123123",
            4
        )

    def test_driver_license_should_be_set(self):
        self.assertRaises(
            DriverLicenseRequiredError,
            Vehicle,
            "011233495839845",
            3
        )

    def test_can_drive_should_return_true_when_driver_has_license(self):
        person = _get_person()

        car = Vehicle(
            vin="1234567890",
            vehicle_type=VehicleType.Car,
            driver_license=DriverLicense.B
        )

        self.assertTrue(car.can_drive(person.driver_license))

    def test_can_drive_should_return_true_when_driver_has_license(self):
        person = _get_person()

        car = Vehicle(
            vin="1234567890",
            vehicle_type=VehicleType.Car,
            driver_license=DriverLicense.C1E,
            manufacturer="Volkswagen"
        )

        self.assertFalse(car.can_drive(person.driver_license))

    def test_should_be_equal_when_vin_is_equal(self):
        audi = Vehicle(
            vin="1234567890",
            vehicle_type=VehicleType.Car,
            driver_license=DriverLicense.B,
            manufacturer="Audi"
        )

        vw = Vehicle(
            vin="1234567890",
            vehicle_type=VehicleType.Truck,
            driver_license=DriverLicense.C,
            manufacturer="Volkswagen"
        )

        self.assertEqual(audi, vw)
        self.assertTrue(audi == vw)
