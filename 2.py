dog = {}
print(dog)
dog = {'name' : 'hash',
       'color' : 'black',
       'breed' : 'shitzu',
       'legs' : 4,
       'age' : 5}
print(dog)
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
print(len(student))
print(student.get('skills'))
print(type(student['skills']))
student['skills'].append("Leadership")
print(student)
print(student.keys())
print(student.values())