# creating tuple sisters and brothers and Printing them
sisters = ("Anu", "Nagini", "Gowri", "Durga")
print(sisters)
brothers = ("Sai","Srinu")
print(brothers)

# Joining brothers and sisters and assigning them to siblings
siblings = sisters + brothers
print(siblings)

# Getting the length of sibilings
print(len(siblings))

# Modifying siblings tuple by adding father and mother and assiging them to family_mem
family_mem = ("Sarveswararao","Ramadevi")
family_mem += siblings
print(family_mem)