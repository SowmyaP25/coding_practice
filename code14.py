H = int(input("Hours: "))
M = int(input("Minutes: "))
angle_hr = (H * 30) + (M * 0.5)
angle_min = M * 6
diff = angle_hr - angle_min
if diff < 0:
    diff = int(-(diff))
print(diff)