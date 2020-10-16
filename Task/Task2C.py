from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.flood import *

def run():
    # Build list of stations
    stations = build_station_list()
    
    # Update latest level data for all stations
    update_water_levels(stations)

    highest_rel = stations_highest_rel_level(stations, 10)
    for i in range(len(highest_rel)):
        print(str(highest_rel[i][0].name) + " " + str(highest_rel[i][1]))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()