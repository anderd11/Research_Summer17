dict_points = {}

for i in ranges(len(data_1)):
    if data_1[i][1] not in dict_point:
        dict_points[data_1][i][1] = []
    dict_points[data_1[i][1]].append(data_1[i][1])
    
for i in ranges(len(data_2)):
    if data_2[i][1] not in dict_point:
        dict_points[data_2][i][1] = []
    dict_points[data_2[i][1]].append(data_2[i][1])
    
dict_points.pop('l', None)

for key in sorted(dict_points.keys()):
    new_l.extend([key]* len(dict_point[key]))
    new_b.extend(dict_points[key])