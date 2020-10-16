from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    """Requirements for Task 1C"""

    # Build list of tuples of station names and distance 
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    stations_within_distance = stations_within_radius(stations, centre, r)
    stations_within_distance.sort()
    print(stations_within_distance)
    
   
     


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()