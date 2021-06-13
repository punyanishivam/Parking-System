from services.ParkVehicleInterface import ParkVehicleInterface
from models.Vehicle import Vehicle


class ParkVehicleService(ParkVehicleInterface):

    def park(self, license_plate, driver_age, parking_lot):

        vehicle = Vehicle(license_plate, driver_age)

        if parking_lot.is_available():
            spot = parking_lot.park_vehicle()

        spot.park_vehicle(vehicle)

        return "Car with vehicle registration number {} has been parked at slot number {}".format(license_plate, spot.spot_number)
