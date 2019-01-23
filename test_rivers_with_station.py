from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

river_with_station = rivers_with_station(build_station_list())
river_top_ten = []
for n in range(10):
    river_top_ten.append(river_with_station[n])
assert river_top_ten == ['Addlestone Bourne', 'Aire Washlands', 'Alconbury Brook', 'Aldingbourne Rife', 'Aller Brook', 'Alverthorpe Beck', 'Ampney Brook', 'Amwell Loop', 'Arkle Beck', 'Arrowe Brook']
print("passed")