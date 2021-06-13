from services.LicenceNumberWithAgeInterface import LicenceNumberWithAgeInterface


class LicenseNumberWithAgeService(LicenceNumberWithAgeInterface):

    def vehicle_registration_number_for_driver_of_age(self, parking_lot, driver_age):

        result = []

        for spot in parking_lot.taken_spots:
            if spot.vehicle.driver_age == driver_age:
                result.append(str(spot.vehicle.license_number))

        if result == []:
            return "No parked car matches the query"
        return ",".join(result)
