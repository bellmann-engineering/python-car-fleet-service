import unittest
from datetime import date
from dateutil.relativedelta import relativedelta
from car_fleet.person import Person
from car_fleet.driver_license import DriverLicense


class PersonTests(unittest.TestCase):
    def test_age(self):
        expected = 40
        expected_first_name = "Max"
        expected_last_name = "Mustermann"
        expected_license = DriverLicense.B

        fourty_years_ago = (date.today() - relativedelta(years=40))
        license = DriverLicense.B

        max_mustermann = Person("Max", "Mustermann", fourty_years_ago, license)

        self.assertEqual(expected, max_mustermann.age)
        self.assertEqual(expected_first_name, max_mustermann.first_name)
        self.assertEqual(expected_last_name, max_mustermann.last_name)
        self.assertEqual(expected_license, max_mustermann.driver_license)
