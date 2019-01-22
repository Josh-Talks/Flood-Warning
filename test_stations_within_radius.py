from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

stations = build_station_list()
centre = (52.2053, 0.1218)
r = 10
stations_within_distance = stations_within_radius(stations, centre, r)
stations_within_distance.sort()

assert stations_within_distance == ['Bin Brook', 'Cambridge Baits Bite', 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
print("passed")