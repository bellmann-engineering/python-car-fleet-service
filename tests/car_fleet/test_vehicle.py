import unittest
from datetime import date

from car_fleet.vehicle import Vehicle, Car, Truck, Motorcycle


class VehicleTests(unittest.TestCase):
    def test_vehicle_should_be_equal_when_vin_is_equal(self):
        expected = Vehicle(vin="1234567890", manufacturer="Test")

        actual = Vehicle(vin="1234567890", manufacturer="123")

        self.assertEqual(expected, actual)
        self.assertTrue(expected == actual)

    def test_car_should_be_equal_when_vin_is_equal(self):
        expected = Car(vin="1234567890", manufacturer="Test")

        actual = Car(vin="1234567890", manufacturer="123")

        self.assertEqual(expected, actual)
        self.assertTrue(expected == actual)

    def test_truck_should_be_equal_when_vin_is_equal(self):
        expected = Truck(vin="1234567890", manufacturer="Test")

        actual = Truck(vin="1234567890", manufacturer="123")

        self.assertEqual(expected, actual)
        self.assertTrue(expected == actual)

    def test_motorcycle_should_be_equal_when_vin_is_equal(self):
        expected = Motorcycle(vin="1234567890", manufacturer="Test")

        actual = Motorcycle(vin="1234567890", manufacturer="123")

        self.assertEqual(expected, actual)
        self.assertTrue(expected == actual)
