from floodsystem.stationdata import build_station_list
from floodsystem.geo import *
from floodsystem.station import *

stations = build_station_list()
assert(sorted(inconsistent_typical_range_stations(stations))) == ['Addlestone', 'Airmyn', 'Allerford', 'Blacktoft', 'Braunton', 'Brentford', 'Broomfleet Weighton Lock', 'East Hull Hedon Road', 'Fleetwood', 'Goole', 'Hedon Thorn Road Bridge', 'Hedon Westlands Drain', 'Hull Barrier Victoria Pier', 'Hull High Flaggs, Lincoln Street', "King's Lynn", 'Littlehampton', 'Paull', 'Salt end', 'Silloth Docks', 'Sindlesham Mill', 'Stone Creek', 'Templers Road', 'Topsham', 'Totnes', 'Truro Harbour', 'Wilfholme PS', 'Wilfholme PS Hull Level']

print("passed")