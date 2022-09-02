ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# sorting the list
ages.sort()
print(ages)
# Printing minimum age
print("minimum : ", min(ages))
# Printing maximum age
print("maximum : ", max(ages))
# Adding minimum age to the list using insert
ages.insert(0,19)
# Adding maximum value to the list using append
ages.append(26)
print(ages)

# Calculating the median of the given list
from statistics import median
print("Median of ages is %d" % (median(ages)))

# Calculating the average of the given list
average = sum(ages)/len(ages)
print(average)

# Calculating Range of maximum and minimum age
range = max(ages)-min(ages)
print(range)