from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    """Requirements for Task 1C"""

    # Build list of tuples of station names and distance 
    stations = build_station_list()
    
    N = 9
    rivers_by_num_stations = rivers_by_station_number(stations, N)
    for river in rivers_by_num_stations[9:]:
        if river[1] == rivers_by_num_stations[9][1]:
            position = rivers_by_num_stations.index(river)
    
    print(rivers_by_num_stations[:position])
    
   

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()