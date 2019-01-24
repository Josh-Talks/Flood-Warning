from floodsystem.stationdata import build_station_list
from floodsystem.geo import *
from floodsystem.station import *

def run():
    stations = build_station_list()
    print(sorted(inconsistent_typical_range_stations(stations)))


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()