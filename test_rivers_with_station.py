from floodsystem.sampledata import build_sample_data
from floodsystem.geo import rivers_with_station

river_with_station = rivers_with_station(build_sample_data())
river_top_three = []
for n in range(3):
    river_top_three.append(river_with_station[n])
assert river_top_three == ['river1', 'river2', 'river3']