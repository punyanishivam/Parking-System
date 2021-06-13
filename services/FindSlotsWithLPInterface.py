from abc import ABC, abstractmethod


class FindSlotsWithLPInterface(ABC):

    @abstractmethod
    def slot_number_for_car_with_number(self, parking_lot, license_plate):
        pass
