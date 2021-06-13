class ParkingLot(object):

    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.available_spots = []
        self.taken_spots = []

    def is_available(self):
        return self.available_spots != []

    def park_vehicle(self):
        spot = self.available_spots.pop(0)
        self.taken_spots.append(spot)
        return spot

    def leave_spot(self, spot_number):
        spot = self.taken_spots.pop(spot_number)
        self.available_spots.append(spot)
        return spot


class ParkingSpot(object):

    def __init__(self, spot_number):
        self.spot_number = spot_number
        self.vehicle = None

    def park_vehicle(self, vehicle):
        self.vehicle = vehicle

    def leave_spot(self):
        self.vehicle = None
