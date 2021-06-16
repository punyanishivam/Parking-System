from services.UnParkVehicleService import UnParkVehicleService
from services.CreateParkingLotService import CreateParkingLotService
from services.ParkVehicleService import ParkVehicleService
from services.FindSlotsWithAgeService import FindSlotsWithAgeService
from services.FindSlotsWithLPService import FindSlotsWithLPService
from services.LicenseNumberWithAgeService import LicenseNumberWithAgeService

input_file = open("input.txt")
output_file = open("output.txt", "w")

lines = input_file.readlines()

for line in lines:
    if "Create_parking_lot" in line:
        param1, param2 = line.split()[1], 0
        create_parking_lot_service = CreateParkingLotService()
        parking_lot, message = create_parking_lot_service.create_parking_lot(
            int(param1))
        output_file.write(message)
        output_file.write("\n")
    if "Park" in line:
        param1, param2 = line.split()[1], line.split()[3]
        park_vehicle_service = ParkVehicleService()
        output_file.write(park_vehicle_service.park(
            param1, int(param2), parking_lot))
        output_file.write("\n")
    if "Slot_numbers_for_driver_of_age" in line:
        param1, param2 = line.split()[1], 0
        find_slots_with_age_service = FindSlotsWithAgeService()
        output_file.write(
            str(find_slots_with_age_service.slot_numbers_for_driver_of_age(
                parking_lot, int(param1))))
        output_file.write("\n")
    if "Slot_number_for_car_with_number" in line:
        param1, param2 = line.split()[1], 0
        find_slots_with_lp_service = FindSlotsWithLPService()
        output_file.write(str(find_slots_with_lp_service.slot_number_for_car_with_number(
            parking_lot, param1)))
        output_file.write("\n")
    if "Leave" in line:
        param1, param2 = line.split()[1], 0
        unpark_vehicle_service = UnParkVehicleService()
        output_file.write(unpark_vehicle_service.leave(
            parking_lot, int(param1)))
        output_file.write("\n")
    if "Vehicle_registration_number_for_driver_of_age" in line:
        param1, param2 = line.split()[1], 0
        licence_number_with_age_service = LicenseNumberWithAgeService()
        output_file.write(str(licence_number_with_age_service.vehicle_registration_number_for_driver_of_age(
            parking_lot, 18)))
        output_file.write("\n")

input_file.close()
output_file.close()
