from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.flood import *

sta_list = ["Windyridge Road 1.5529411764705883",
"Cam 1.3921568627450978",
"Whaddon 1.0724137931034479",
"Riverside Park 1.005",
"Boulters Lock 0.9733333333333333",
"Bell Weir 0.9681818181818181",
"Graylingwell 0.964",
"Sherborne Lake 0.9222222222222222",
"Poyle 0.9205753595997498",
"Surfleet Sluice 0.9046979865771811",
"Mountnessing 0.8803418803418804",
"Allbrook weir 0.8657534246575341",
"Hythe Weir 0.8481012658227847",
"Hayes Basin 0.833333333333333",
"Arundel 0.8203377650017967",
"Thirlmere Reservoir (Spillway level = 16.55m) 0.8191747572815534",
"Ilfracombe Lambda 0.8156996587030716",
"Charlton Kings 0.8106508875739643",
"Provender Mill 0.8029629629629592"]
stations = build_station_list()
update_water_levels(stations)
stations_at_risk = station_level_over_threshold(stations, 0.8)
for i in range(len(stations_at_risk)):
    assert(str(stations_at_risk[i][0]) + " " + str(stations_at_risk[i][1]) == sta_list[i])