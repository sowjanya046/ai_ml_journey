import numpy as np

EAR = np.array([0.25,0.23,0.28,0.35,0.30,0.22])

print("!!!!!!!!!!!!!Drowsiness Detector!!!!!!!!!!!!!")
for i in range(len(EAR)):
    if EAR[i] <= 0.25:
        print(f"frame{i+1}: Eye Closed - Drowsy")
    else:
        print(f"frame{i+1}: Eye Open - Alert")

#Drowsy count
drowsy_count = np.sum(EAR<=0.25)
#Drowsy Wrost Movement
worst_movement = np.min(EAR)

#Avg Drowsy  Detection
avg_ear = np.mean(EAR)
print("Worst Movement: ", worst_movement)
print("Average EAR: ", avg_ear)
print("Total Drowsy Frames: ", drowsy_count)
