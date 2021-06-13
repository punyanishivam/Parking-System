from abc import ABC, abstractmethod


class FindSlotsWithAgeInterface(ABC):

    @abstractmethod
    def slot_numbers_for_driver_of_age(self, parking_lot, driver_age):
        pass
