import numpy as np

camera_distance = np.array([58,40,35,48,52])
radar_distance = np.array([52,47,44,41,36])

Camera_Weight = 0.4
Radar_Weight = 0.6
mismatch_events = 0
fused_distance = []

for i in range (len(camera_distance)):
    fused_distance_Array = ((camera_distance[i] * Camera_Weight) + (radar_distance[i] * Radar_Weight))
    fused_distance.append(fused_distance_Array)
    print(f"Fused Distance between camera frame {i + 1} : {camera_distance[i]}m and Radar {radar_distance[i]}m : {fused_distance[i]}")
    #Sensor Mismatch
    Disagreement = np.abs(camera_distance[i] - radar_distance[i])
    if(Disagreement > 5):
        mismatch_events = mismatch_events + 1

print(f"mismatched events : {mismatch_events}")

average_fused_distance = np.mean((np.abs(fused_distance)))
print(f"average fused distance : {average_fused_distance}")

closest_fused_distance = np.min((np.abs(fused_distance)))
print(f"Closest fused distance : {closest_fused_distance}")

for i in range (len(fused_distance)):
    if(fused_distance[i] >= 50):
        print("ACC Status: Safe")
    elif(fused_distance[i] >= 30):
        print("ACC STatus: Warning!!")
    else:
        print("Acc Status: Brake")
    