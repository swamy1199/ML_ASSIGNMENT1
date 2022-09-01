ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print("minimum : ", min(ages))
print("maximum : ", max(ages))

ages.insert(0,19)
ages.append(26)
print(ages)

from statistics import median
print("Median of ages is %d" % (median(ages)))

average = sum(ages)/len(ages)
print(average)

range = max(ages)-min(ages)
print(range)