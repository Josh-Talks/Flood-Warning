test_station_id = ['sid1', 'sid2', 'sid3', 'sid4', 'sid5']
test_measure_id = ['id1', 'id2', 'id3', 'id4', 'id5']
test_label = ['label1', 'label2', 'label3', 'label4', 'label5']
test_coord = [(1,1),(2,2), (3,3), (4,4), (5,5)]
test_typical_range = [(0.1,0.2), (0.2,0.3), (0.3,0.4), (0.4,0.5), (0.5,0.6)]
test_river = ['river1', 'river2', 'river3', 'river4', 'river5']
test_town = ['town1', 'town2', 'town3', 'town4', 'town5']

station_data = []
data = []
for n in range(len(test_town)):
    data.append((test_station_id[n], 
    test_measure_id[n], 
    test_label[n], 
    test_coord[n], 
    test_typical_range[n], 
    test_river[n], 
    test_town[n]))
station_data.append(data)


print(station_data)

    