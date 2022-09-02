# Initialising lbs and kg as empty list
lbs = []
kg = []

# Getting number of students from user
N = int(input("Enter number of Students : "))

# Using for loop to insert the user data to lbs list
for i in range(0, N):
    ele = int(input())
    lbs.append(ele)
print(lbs)

# Using for loop to convert lbs to kilograms and store it in kg list
for i in range(len(lbs)):
    lb=0.45359237
    ele1 = round(lbs[i]*lb,2)
    kg.append(ele1)
print(kg)