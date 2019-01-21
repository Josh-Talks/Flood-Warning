# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine   # formula to calculate distance between two coordinates

def stations_by_distance(stations, p):  
    names = []   #list station names
    for station in stations:
        d = haversine(station.coord, p, unit='km')
        names.append((station.name, d))
    names = sorted_by_key(names, 1)
    
    return names

def stations_within_radius(stations, centre, r):
    stations_within_r = []
    for station in stations:
        d = haversine(station.coord, centre, unit='km')
        
        if d < r:
            stations_within_r.append(station.name)
        
    return stations_within_r

            