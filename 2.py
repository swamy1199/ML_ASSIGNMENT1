# Creating an empty dictionary
dog = {}
print(dog)

# Creating a dictionary and adding keys and values
dog = {'name' : 'hash',
       'color' : 'black',
       'breed' : 'shitzu',
       'legs' : 4,
       'age' : 5}
print(dog)
# Creating a dictionary and adding keys and values
student = {'first_name' : 'VENKATAGURUSWAMY',
           'last_name' : 'GODHA',
           'gender' : 'Male',
           'age' : 23,
           'martial_status' : 'Single',
           "skills" : ["C", "Python", "Java"],
           'country' : 'India',
           'city' : 'Vissannapeta',
           'address' : '9-117/6E Dwarakanagar Vissannapeta'}
print(student)
# Printing the length of the dictionary
print(len(student))
# Getting the value of skills and printing them
print(student.get('skills'))
# Printing the data type of Skills
print(type(student['skills']))
# Modifying the skills by adding one value
student['skills'].append("Leadership")
print(student)
# Getting dictionary keys as list and printing keys as list
print(student.keys())
# Getting dictionary values as list and printing keys as list
print(student.values())