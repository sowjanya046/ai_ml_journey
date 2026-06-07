import numpy as np

speed_readings = np.array([75,80,110,130,90,60,75])
Distance_Target = np.array([30,50,80,60,55,40,20])
Lane_offset = np.array([5,10,15,8,12,18,11])
Speed_Difference = np.diff(speed_readings)

speed_violation = 0
distance_violation = 0
Lane_violation = 0
speed_diff_count = 0
speed_violation_score = -10
Distance_Target_score = -20
Lane_offset_score = -10
Hardbreaking_Score = -15

for i in range(len(speed_readings)):
    if(speed_readings[i] > 100):
        print(f"Frame {i+1}: {speed_readings[i]} kmph → Violation!")
        speed_violation = speed_violation + 1
    else:
        print(f"Frame {i+1}: {speed_readings[i]} kmph → Safe")
        
for i in range(len(Distance_Target)):
    if(Distance_Target[i] < 30):
        print(f"Frame {i+1}: {Distance_Target[i]} kmph → Violation!")
        distance_violation += 1
    else:
        print(f"Frame {i+1}: {speed_readings[i]} kmph → Safe")
        
for i in range(len(Lane_offset)):
    if(Lane_offset[i] > 15):
        print(f"Frame {i+1}: {Lane_offset[i]} kmph → Violation!")
        Lane_violation += 1
    else:
        print(f"Frame {i+1}: {Lane_offset[i]} kmph → Safe")

speed = np.sum(speed_violation)
Distance = np.sum(distance_violation)
Lane = np.sum(Lane_violation)
Hardbreaking = np.sum(Speed_Difference < -20)

speed_violation_penalty = (speed_violation_score * speed)
Distance_Target_penalty = (Distance_Target_score * Distance)
Lane_offset_penalty =    (Lane_offset_score * Lane)
Hardbreaking_penalty = (Hardbreaking_Score * Hardbreaking)

Total_penalties = speed + Distance + Lane + Hardbreaking

Safety_Score = 100 + (speed_violation_penalty + Distance_Target_penalty + Lane_offset_penalty + Hardbreaking_penalty)

print(f"Total penalitiues driver took in the driving: {Total_penalties}")
print(f"Driver safety Score at the end of the trip : {Safety_Score}")

if (Safety_Score >= 80):
    print("Driver rating: Excellent")
elif (Safety_Score >= 60):
    print("Driver rating: Average")
elif (Safety_Score >= 40):
    print("Driver rating: Good")
else:
    print("Driver rating: Dangerous")