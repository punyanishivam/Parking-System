from abc import ABC, abstractmethod


class LicenceNumberWithAgeInterface(ABC):

    @abstractmethod
    def vehicle_registration_number_for_driver_of_age(self, parking_lot, age):
        pass
