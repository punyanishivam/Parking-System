from abc import ABC, abstractmethod


class UnParkVehicleInterface(ABC):

    @abstractmethod
    def leave(self, spot_number):
        pass
