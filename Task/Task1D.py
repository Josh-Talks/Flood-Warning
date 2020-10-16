from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    """Requirements for Task 1D"""

    # Build list of tuples of station names and distance 
    stations = build_station_list()
   
    river_with_station = rivers_with_station(stations)
    river_top_ten = []
    for n in range(10):
        river_top_ten.append(river_with_station[n])
    print(river_top_ten)
    print(len(river_with_station))
 
    stations_on_river = stations_by_river(stations)
    print(sorted(stations_on_river["River Aire"]))
    print(sorted(stations_on_river["River Cam"]))
    print(sorted(stations_on_river["River Thames"]))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()