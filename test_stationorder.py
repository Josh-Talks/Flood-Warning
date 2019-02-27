from floodsystem.geo import *
from floodsystem.stationdata import build_station_list
from floodsystem.sampledata import build_sample_data

assert stations_by_distance(build_sample_data(), (0.0, 0.0)) == [('label1', 157.2495984740402), ('label2', 314.47523947196964), ('label3', 471.65293997288967), ('label4', 628.7586658391518), ('label5', 785.7683061901735)]