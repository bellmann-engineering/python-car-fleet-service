from dataclasses import dataclass
from datetime import date
from dateutil.relativedelta import relativedelta

from .driver_license import DriverLicense


@dataclass
class Person:
    first_name: str
    last_name: str
    birth_date: date
    driver_license: DriverLicense

    @property
    def age(self) -> int:
        return relativedelta(date.today(), self.birth_date).years
