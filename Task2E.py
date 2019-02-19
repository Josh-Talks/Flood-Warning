from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import *
import datetime
from floodsystem.plot import *

stations = build_station_list()

update_water_levels(stations)
newStations = []
for station in stations:
    if station.latest_level:
        newStations.append(station)
newStations.sort(key=lambda station: station.latest_level, reverse=True)

newStations= newStations[:5]



#dict of name (for top five highest current water level stations) to measure_id
station_top_5 = {}
high = []
low = []

for station in newStations:
    station_top_5[station.name] = station.measure_id
    high.append(station.typical_range[1])
    low.append(station.typical_range[0])

t = []
level = []
dt = 10

for n in station_top_5:
    dates, levels = fetch_measure_levels(station_top_5[n], dt=datetime.timedelta(days=dt))
    t.append(dates)
    level.append(levels)


lengths = []
for levell in level:
    lengths.append(len(levell))

high = [[i]*lengths[idx] for idx,i in enumerate(high)]
low = [[i]*lengths[idx] for idx,i in enumerate(low)]


names = []
for key in station_top_5:
    names.append(key)



plot_water_levels(names[0], t[0], level[0], high[0], low[0])
plot_water_levels(names[1], t[1], level[1], high[1], low[1])
plot_water_levels(names[2], t[2], level[2], high[2], low[2])
plot_water_levels(names[3], t[3], level[3], high[3], low[3])
plot_water_levels(names[4], t[4], level[4], high[4], low[4])
