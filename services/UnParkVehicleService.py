from services.UnParkVehicleInterface import UnParkVehicleInterface


class UnParkVehicleService(UnParkVehicleInterface):

    def leave(self, parking_lot, spot_number):

        spot = parking_lot.leave_spot(spot_number-1)

        spot_no = spot.spot_number
        license_number = spot.vehicle.license_plate
        age = spot.vehicle.driver_age

        spot.leave_spot()

        avs = parking_lot.available_spots
        avs = sorted(
            avs, key=lambda x: x.spot_number)
        parking_lot.available_spots = avs

        return "Slot number {} vacated, the car with vehicle registration number {} left the space, the driver of the car was of age {}".format(
            spot_no, license_number, age)
