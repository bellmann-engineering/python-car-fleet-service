from car_fleet.driver_license import DriverLicense
import unittest
from datetime import date

from car_fleet.vehicle import Vehicle, Car, Truck, Motorcycle
from car_fleet.person import Person


def _get_person() -> Person:
    driver_licenses = DriverLicense.A | DriverLicense.B | DriverLicense.C

    return Person(
        first_name="Vorname",
        last_name="Nachname",
        birth_date=date(1970, 1, 1),
        driver_license=driver_licenses
    )


class VehicleTests(unittest.TestCase):
    def test_should_be_equal_when_vin_is_equal(self):
        expected = Vehicle(vin="1234567890", manufacturer="Test")

        actual = Vehicle(vin="1234567890", manufacturer="123")

        self.assertEqual(expected, actual)
        self.assertTrue(expected == actual)


class CarTests(unittest.TestCase):
    def test_should_be_equal_when_vin_is_equal(self):
        expected = Car(vin="1234567890", manufacturer="Test")

        actual = Car(vin="1234567890", manufacturer="123")

        self.assertEqual(expected, actual)
        self.assertTrue(expected == actual)

    def test_should_require_driver_license(self):
        person = _get_person()

        actual = Car(
            vin="1234567890",
            driver_license=DriverLicense.B
        )

        self.assertTrue(actual.can_drive(person.driver_license))


class TruckTests(unittest.TestCase):
    def test_should_be_equal_when_vin_is_equal(self):
        expected = Truck(vin="1234567890", manufacturer="Test")

        actual = Truck(
            vin="1234567890",
            driver_license=DriverLicense.C1
        )

        self.assertEqual(expected, actual)
        self.assertTrue(expected == actual)

    def test_should_require_driver_license(self):
        person = _get_person()

        actual = Truck(
            vin="1234567890",
            driver_license=DriverLicense.C
        )

        self.assertTrue(actual.can_drive(person.driver_license))


class MotorcycleTests(unittest.TestCase):
    def test_should_be_equal_when_vin_is_equal(self):
        expected = Motorcycle(
            vin="1234567890",
            manufacturer="Test"
        )

        actual = Motorcycle(
            vin="1234567890",
            manufacturer="Brumm Brumm GmbH"
        )

        self.assertEqual(expected, actual)
        self.assertTrue(expected == actual)

    def test_should_require_driver_license(self):
        person = _get_person()

        actual = Motorcycle(
            vin="1234567890",
            driver_license=DriverLicense.A
        )

        self.assertTrue(actual.can_drive(person.driver_license))
