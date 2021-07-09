from datetime import date
from enum import Enum

from car_fleet.driver_license import DriverLicense


class DriverLicenseRequiredError(Exception):
    pass


class InvaildVehicleTypeError(Exception):
    pass


class DriverLicenseRequired:
    pass


class VehicleTypeValid:
    pass


class VehicleType(Enum):
    MotorCycle = 0
    Car = 1
    Truck = 2


class Vehicle:
    def __init__(
        self,
        vin: str,
        vehicle_type: VehicleType,
        driver_license: DriverLicense = None,
        license_plate: str = "",
        manufacturer: str = "",
        manufacture_date: date = date.today(),
        model_name: str = ""
    ) -> None:
        # Vehicle identification number ISO3779, ISO4030
        self._vin = vin,
        self._vehicle_type = vehicle_type
        self._driver_license = driver_license,
        self._license_plate = license_plate,
        self._manufacturer = manufacturer,
        self._manufacture_date = manufacture_date,
        self._model_name = model_name

    @property
    def vin(self):
        return self._vin

    @property
    def vehicle_ype(self):
        return self._vehicle_type

    @property
    def driver_license(self):
        return self._driver_license

    @property
    def license_plate(self):
        return self._license_plate

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def manufacture_date(self):
        return self._manufacture_date

    @property
    def model_name(self):
        return self._model_name

    vehicle_type = VehicleTypeValid()
    driver_license = DriverLicenseRequired()

    def can_drive(self, drivers_license: DriverLicense) -> bool:
        return (self.driver_license in drivers_license)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vehicle):
            return self.vin == other.vin

        return False

    def __hash__(self):
        return id(self)
