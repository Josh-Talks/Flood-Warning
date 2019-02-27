# function which builds sample data that can be used in testing

from .station import MonitoringStation

def build_sample_data():
    s_id = ['sid1', 'sid2', 'sid3', 'sid4', 'sid5']
    m_id = ['id1', 'id2', 'id3', 'id4', 'id5']
    label = ['label1', 'label2', 'label3', 'label4', 'label5']
    coord = [(1,1),(2,2), (3,3), (4,4), (5,5)]
    trange = [(0.1,0.2), (0.2,0.3), (0.3,0.4), (0.5,0.4), (None)]
    river = ['river1', 'river2', 'river3', 'river4', 'river1']
    town = ['town1', 'town2', 'town3', 'town4', 'town5']

    station_data = []
    for n in range(len(town)):
        s = MonitoringStation(s_id[n], m_id[n], label[n], coord[n], trange[n], river[n], town[n])
        station_data.append(s)

    return station_data