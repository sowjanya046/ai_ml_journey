import numpy as np

print("....................Lane DEVAITAION Detctor............................")

Safe_Zone = 10
Warning_Zone = 15
Warning_count = 0
Critical_Count = 0

Lane_offset = np.array([0,5,18,25,30,12,15,11,20,8,6,0])

for i in range (len(Lane_offset)):
    if (Lane_offset[i] <= Safe_Zone):
        print(f"Frame {i+1}: {Lane_offset[i]} kmph → Safe!")
    elif (Lane_offset[i] <= Warning_Zone):
        print(f"Frame {i+1}: {Lane_offset[i]} kmph → Warning!!")
        Warning_count = Warning_count + 1
    else:
        print(f"Frame {i+1}: {Lane_offset[i]} kmph → Critical!!!!")
        Critical_Count = Critical_Count + 1

Maximum_Deviation = np.max(np.abs(Lane_offset))
print(f"Maximum Deviation of the Lane_offset - {Maximum_Deviation}")

Average_Deviation = np.mean(np.abs(Lane_offset))
print(f"Average Deviation of the Lane_offset - {Average_Deviation}")

print(f"Warning event count of the Lane_Offset - {Warning_count}")
print(f"Critical event count of the Lane_Offset - {Critical_Count}")

if (Critical_Count >= 3):
    print("Lane_Leeping: Dangerous Lane Keeping")
elif (Warning_count >= 2):
    print("Lane_Leeping: Poor Lane Keeping")
else:
    print("Lane_Leeping: Safe Lane Keeping")