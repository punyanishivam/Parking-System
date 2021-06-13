from services.FindSlotsWithLPInterface import FindSlotsWithLPInterface


class FindSlotsWithLPService(FindSlotsWithLPInterface):

    def slot_number_for_car_with_number(self, parking_lot, license_plate):

        for spot in parking_lot.taken_spots:
            if spot.vehicle.license_plate == license_plate:
                return spot.spot_number

        return "No parked car matches the query"
