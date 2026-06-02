import numpy as np

speed = np.array([0,35,45,55,75,100,125,95,85,60,30,0])

Speed_Threshold = 100
Sudden_Dec_Speed_Threshold = -20
Sudden_Acc_Speed_Threshold = 20

for i in range (len(speed)):
    if speed[i] > Speed_Threshold:
        print("Speed is above the threshold at index", i, "with speed", speed[i])
    else:
        print("Speed is below the threshold at index", i, "with speed", speed[i])
speed_diff = np.diff(speed)

Max_Speed = np.max(speed)
print("Maximum speed recorded is", Max_Speed)

Average_Speed = np.mean(speed)
print("Average speed recorded is", Average_Speed)

count_Speeding_events = np.sum(speed > Speed_Threshold)
print("Number of speeding events recorded is", count_Speeding_events)

Hard_Braking_events = np.sum(speed_diff < Sudden_Dec_Speed_Threshold)
print("Number of hard braking events recorded is", Hard_Braking_events) 

Rapid_Acceleration_events = np.sum(speed_diff > Sudden_Acc_Speed_Threshold)
print("Number of rapid acceleration events recorded is", Rapid_Acceleration_events)

Trip_Rating = (Average_Speed / Max_Speed) * 100
print("Trip rating based on speed is", Trip_Rating, "%")