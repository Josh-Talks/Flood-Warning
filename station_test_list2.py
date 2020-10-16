class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

station_id = ['sid1', 'sid2', 'sid3', 'sid4', 'sid5']
measure_id = ['id1', 'id2', 'id3', 'id4', 'id5']
label = ['label1', 'label2', 'label3', 'label4', 'label5']
coord = [(1,1),(2,2), (3,3), (4,4), (5,5)]
typical_range = [(0.1,0.2), (0.2,0.3), (0.3,0.4), (0.4,0.5), (0.5,0.6)]
river = ['river1', 'river2', 'river3', 'river4', 'river5']
town = ['town1', 'town2', 'town3', 'town4', 'town5']

station_data = []
data = []
for n in range(len(town)):
    data.append((station_id[n], 
    measure_id[n], 
    label[n], 
    coord[n], 
    typical_range[n], 
    river[n], 
    town[n]))
station_data.append(data)

stations = []
for e in station_data['items']:
     # Extract town string (not always available)
    town = None
    if 'town' in e:
        town = e['town']

    # Extract river name (not always available)
    river = None
    if 'riverName' in e:
        river = e['riverName']

    # Attempt to extract typical range (low, high)
    try:
        typical_range = (float(e['stageScale']['typicalRangeLow']),
                            float(e['stageScale']['typicalRangeHigh']))
    except Exception:
        typical_range = None

    try:
        # Create mesure station object if all required data is
        # available, and add to list
        s = MonitoringStation(
            station_id=e['@id'],
            measure_id=e['measures'][-1]['@id'],
            label=e['label'],
            coord=(float(e['lat']), float(e['long'])),
            typical_range=typical_range,
            river=river,
            town=town)
        stations.append(s)
    except Exception:
        # Not all required data on the station was available, so
        # skip over
        pass



print(stations)