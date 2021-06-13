from services.CreateParkingLotInterface import CreateParkingLotInterface
from models.ParkingLot import ParkingLot, ParkingSpot


class CreateParkingLotService(CreateParkingLotInterface):

    def create_parking_lot(self, lot_size):

        parking_lot = ParkingLot(lot_size)

        for i in range(1, lot_size+1):
            parking_lot.available_spots.append(ParkingSpot(i))

        print("Created parking of {} slots".format(lot_size))
        return parking_lot
