# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    """Requirements for Task 1B"""

    # Build list of tuples of station names and distance 
    stations = build_station_list()
    p = (52.2053, 0.1218)
    by_distance = stations_by_distance(stations, p)
    for n in range(10):
        print(by_distance[n])
    for n in range(10):
        i = len(by_distance) - 10 + n
        print(by_distance[i])   


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()