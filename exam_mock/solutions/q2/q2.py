import math

def closest_pair(coord_list):
    min_distance = 999999999
    min_pair = set()

    for i in range(len(coord_list)-1):
        for j in range(i+1, len(coord_list)):
            total = 0
            for k in range(len(coord_list[0])):
                total += (coord_list[i][k] - coord_list[j][k])**2
            
            distance = math.sqrt(total) 
            
            if distance < min_distance:
                min_pair = {coord_list[i], coord_list[j]}
                min_distance = distance

    return min_pair


def closest_pair_v2(coord_list):
    distances = []
    for i in range(len(coord_list)-1):
        for j in range(i+1, len(coord_list)):
            total = 0
            for k in range(len(coord_list[0])):
                total += (coord_list[i][k] - coord_list[j][k])**2
            
            distance = math.sqrt(total) 
            distances.append((coord_list[i], coord_list[j], distance))

    min_instance = min(distances, key=lambda x:x[2])
    return set([min_instance[0], min_instance[1]])

