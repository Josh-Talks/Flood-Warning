from floodsystem.sampledata import *
from floodsystem.geo import *


stations = build_sample_data()
    
N = 1
rivers_by_num_stations = rivers_by_station_number(stations, N)
    
assert(rivers_by_num_stations == [('river1', 2), ('river2', 1), ('river3', 1), ('river4', 1)])