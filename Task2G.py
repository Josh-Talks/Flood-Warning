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
    
    dt = 2
    p = 4
    level_tol = 0.9
    gradient_tol = -1.0
    at_risk = station_level_over_thresh(stations, level_tol)
    gonna_flood = []
    for station in at_risk:
        dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))
        if polyfit(dates, levels, p) != None:
            poly, x, poly_deriv = polyfit(dates, levels, p)
            current_grad = current_gradient(poly, dates, levels, p)
            print(current_grad)
            if station_at_risk(current_grad, gradient_tol) == True:
                gonna_flood.append(station.town)
    
#towns at risk off flooding          
    print(gonna_flood)
        

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()