from floodsystem.sampledata import build_sample_data
from floodsystem.geo import *

stations = build_sample_data()
centre = (0.0 , 0.0)
r = 500
stations_within_distance = stations_within_radius(stations, centre, r)
stations_within_distance.sort()

assert stations_within_distance == ['label1', 'label2', 'label3']