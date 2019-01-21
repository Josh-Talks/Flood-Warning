# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from utils import sorted_by_key  # noqa
from haversine import haversine   # formula to calculate distance between two coordinates

def stations_by_distance(stations, p):  
    station = []   #list station names
    for station in stations:
        station.append(stations.name)
    
    coordinates = []    #list coordinates
    for coordinates in stations:
        coordinates.append(stations.coord)

    distance = []
    for i in range(len(coordinates)):
        d = haversine(coordinates[i], p, unit='km')
        distance.append(d)

    position = []
    for i in range(len(stations)):
        position.append((stations[i], distance[i]))
   
    return(position)

position.sorted_by_keys()

    

            