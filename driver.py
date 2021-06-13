from services.LicenceNumberWithAgeInterface import LicenceNumberWithAgeInterface
from services.UnParkVehicleService import UnParkVehicleService
from services.CreateParkingLotService import CreateParkingLotService
from services.ParkVehicleService import ParkVehicleService
from services.FindSlotsWithAgeService import FindSlotsWithAgeService
from services.FindSlotsWithLPService import FindSlotsWithLPService
from services.UnParkVehicleService import UnParkVehicleService
from services.LicenseNumberWithAgeService import LicenseNumberWithAgeService

file = open("output.txt", "w")

create_parking_lot_service = CreateParkingLotService()
parking_lot = create_parking_lot_service.create_parking_lot(6)

# available_slots = parking_lot.available_spots

# for i in available_slots:
#     print(i.spot_number, i.vehicle)

park_vehicle_service = ParkVehicleService()

file.write(park_vehicle_service.park("KA-01-HH-1234", 21, parking_lot))
file.write(park_vehicle_service.park("PB-01-HH-1234", 21, parking_lot))

find_slots_with_age_service = FindSlotsWithAgeService()

file.write(
    str(find_slots_with_age_service.slot_numbers_for_driver_of_age(parking_lot, 21)))
file.write(
    str(find_slots_with_age_service.slot_numbers_for_driver_of_age(parking_lot, 18)))

file.write(park_vehicle_service.park("PB-01-TG-2341", 21, parking_lot))

find_slots_with_lp_service = FindSlotsWithLPService()

file.write(str(find_slots_with_lp_service.slot_number_for_car_with_number(
    parking_lot, "PB-01-HH-1234")))

unpark_vehicle_service = UnParkVehicleService()
file.write(unpark_vehicle_service.leave(parking_lot, 2))

file.write(park_vehicle_service.park("HR-29-TG-3098", 39, parking_lot))

file.write(str(find_slots_with_lp_service.slot_number_for_car_with_number(
    parking_lot, "PB-01-HH-6789")))


licence_number_with_age_service = LicenseNumberWithAgeService()

file.write(str(licence_number_with_age_service.vehicle_registration_number_for_driver_of_age(
    parking_lot, 18)))

file.close()