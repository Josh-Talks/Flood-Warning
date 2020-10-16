from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.flood import *

def run():
    # Build list of stations
    stations = build_station_list()
    
    # Update latest level data for all stations
    update_water_levels(stations)

    stations_at_risk = station_level_over_threshold(stations, 0.8)
    for i in range(len(stations_at_risk)):
        print(str(stations_at_risk[i][0]) + " " + str(stations_at_risk[i][1]))






if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()