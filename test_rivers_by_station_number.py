from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

stations = build_station_list()
    
N = 9
rivers_by_num_stations = rivers_by_station_number(stations, N)
for river in rivers_by_num_stations[9:]:
    if river[1] == rivers_by_num_stations[9][1]:
        position = rivers_by_num_stations.index(river)
    
assert(rivers_by_num_stations[:position]) == [('River Thames', 55), ('River Avon', 32), ('River Great Ouse', 31), ('River Aire', 23), ('River Test', 22), ('River Calder', 21), ('River Severn', 21), ('River Derwent', 20), ('River Stour', 18)]
print("passed")