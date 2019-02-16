"""Code dealing with flood response"""

def station_level_over_threshold(stations, tol):
    stations_above_tol = []
    for station in stations:
        if type(station.relative_water_level()) != float:
            continue 
        elif station.relative_water_level() >= tol:
            stations_above_tol.append((station.name, station.relative_water_level()))
    return sorted(stations_above_tol, reverse=True, key=lambda level: level[1])

def stations_highest_rel_level(stations, N):
    unsorted_stations = []
    for station in stations:
        if type(station.relative_water_level()) != float:
            continue
        else:
            unsorted_stations.append((station.name, station.relative_water_level()))
    stations_by_level = sorted(unsorted_stations, reverse=True, key=lambda level: level[1])
    first_N = stations_by_level[0:N]
    return first_N