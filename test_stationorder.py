from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

assert stations_by_distance(build_station_list(), (52.2053, 0.1218))[0] == ('Cambridge Jesus Lock', 0.840237595667494)
print("passed")