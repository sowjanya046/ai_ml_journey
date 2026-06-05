import numpy as np

distance_array = np.array([100,120,80,55,25,30,60,70,40])

safe_threshold = 80
Warning_Threshold = 40

for i in range (len(distance_array)):
    if distance_array[i] >= safe_threshold:
        print(f"frame{i+1} - ACC — maintain speed")
    elif ((distance_array[i] >= Warning_Threshold) and (distance_array[i] < safe_threshold)):
        print(f"frame{i+1} - WARNING — prepare to slow")
    else:
         print(f"frame{i+1} - BRAKE — immediate action")
         
#Brake events
Brake_events_count = np.sum(distance_array<=Warning_Threshold)

#Warning movements
Warning_movement_count = np.sum((distance_array >= Warning_Threshold) & (distance_array < safe_threshold))


#Closest Distance
Closest_Distance = np.min(distance_array)

#Avg distance
avg_distance = np.mean(distance_array)

print("Brake_events_count  ", Brake_events_count)
print("Warning_movement_count: ", Warning_movement_count)
print("Closest_Distance: ", Closest_Distance)
print("avg_distance: ", avg_distance)
