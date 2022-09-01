lbs = []
kg = []

N = int(input("Enter number of Students : "))

for i in range(0, N):
    ele = int(input())
    lbs.append(ele)
print(lbs)

for i in range(len(lbs)):
    lb=0.45359237
    ele1 = round(lbs[i]*lb,2)
    kg.append(ele1)
print(kg)