from abc import ABC, abstractmethod


class ParkVehicleInterface(ABC):

    @abstractmethod
    def park(self, license_plate, driver_age):
        pass
