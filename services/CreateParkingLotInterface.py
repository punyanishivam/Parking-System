from abc import ABC, abstractmethod


class CreateParkingLotInterface(ABC):

    @abstractmethod
    def create_parking_lot(self, size):
        pass
