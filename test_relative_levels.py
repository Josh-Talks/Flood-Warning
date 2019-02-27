from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.flood import *
from floodsystem.sampledata import build_sample_data


stations = build_sample_data()
stations_at_risk = station_level_over_threshold(stations, 0.8)
assert stations_at_risk == [('label3', 0.8999999999999999)]