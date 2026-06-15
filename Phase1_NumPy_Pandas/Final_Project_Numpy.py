import numpy as np

ear_Values = np.array([0.25,0.23,0.28,0.35,0.30,0.22,0.20,0.25])
radar_distance_acc = np.array([100,120,80,55,25,30,60,40])
vehicle_speed = np.array([0,55,75,100,125,95,85,0])
lane_offset = np.array([0,5,18,25,30,12,15,11])
camera_distance = np.array([58,40,35,48,52,50,45,30])
radar_distance_fusion = np.array([52,47,44,41,36,50,38,40])


def check_drowsiness(ear_Values):
    drowsy_count = np.sum(ear_Values <= 0.25)
    return drowsy_count

def Braking_zone_ACC(radar_distance_acc):
    Braking_count = np.sum(radar_distance_acc < 40)
    return Braking_count

drowsiness_result = check_drowsiness(ear_Values)
Braking_zone_result =Braking_zone_ACC(radar_distance_acc)
print(f"Driver Drowsy Count: {drowsiness_result}")
print(f"Driver Braking Count: {Braking_zone_result}")