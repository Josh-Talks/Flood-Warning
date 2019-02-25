from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.flood import *
from floodsystem.plot import *
from floodsystem.analysis import *
from floodsystem.datafetcher import *

def run():
    # Build list of stations
    stations = build_station_list()
    
    # Update latest level data for all stations
    update_water_levels(stations)
    highest_rel = stations_highest_rel_level(stations, 5)
    for data in highest_rel:
        station = data[0]
        dt = 2
        p = 4
        dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))
        polyfit(dates, levels, p)
        

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
