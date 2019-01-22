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



def rivers_with_station(stations):   
    rivers = set()
    for station in stations:
       rivers.add(station.river)
    rivers_list = list(rivers)
    rivers_list.sort()

    return rivers_list

def stations_by_river(stations):
    station_dict = {}
    for station in stations:
        if station.river in station_dict:
            station_dict[station.river].append(station.name)
        else:
            station_dict[station.river] = [station.name]
    
    return station_dict

def rivers_by_station_number(stations, N):
    rivers = []
    num_stations = []
    for station in stations:
        if station.river in rivers:
            num_stations[rivers.index(station.river)] += 1
        else:
            rivers.append(station.river)
            num_stations.append(1)
    num_stations_on_river = []        
    for i in range(len(rivers)):
        num_stations_on_river.append((rivers[i], num_stations[i]))
    
    num_stations_on_river = sorted_by_key(num_stations_on_river, 1, reverse=True)

    return num_stations_on_river
            
