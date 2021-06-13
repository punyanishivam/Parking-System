from services.FindSlotsWithAgeInterface import FindSlotsWithAgeInterface


class FindSlotsWithAgeService(FindSlotsWithAgeInterface):

    def slot_numbers_for_driver_of_age(self, parking_lot, driver_age):

        result = []

        for spot in parking_lot.taken_spots:
            if spot.vehicle.driver_age == driver_age:
                result.append(str(spot.spot_number))

        if result == []:
            return "No parked car matches the query"
        return ",".join(result)
