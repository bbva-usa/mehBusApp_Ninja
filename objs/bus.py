import json
class Bus:
    def get_bus(self):
        bus_default = '''
        {
        "id" : 1,
        "route" : "1A",
        "busNumber" : "1401",
        "address" : "Partridge Ave & Westfield Drive",
        "pickupTime" : "06:45 A.M.",
        "dropoffTime" : "2:56 P.M.",
        "geoLocation": {
          "type":"Point",
          "coordinates": [33.45346,-86.932665]
        }
        }
        '''
        return bus_default
