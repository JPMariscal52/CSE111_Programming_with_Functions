# 01 Checkpoint Review Python
# First exercise of this semester
# Heart Rate

age = int(input("Please enter your age: "))

heart_rate = 220 - age

print(f"When you exercise to strengthen your heart, you should \nkeep your heart rate between {heart_rate*0.65:.0f} and {heart_rate*0.85:.0f} beats per minute.")