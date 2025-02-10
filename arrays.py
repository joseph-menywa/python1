from graphlib import CycleError

courses = ["MIT","Cybersecurity","Datascience"]
print(courses)


#accesing an element from an array
print(courses[2])

#loopingh through an array
for a in courses:
    print("Course is",a)

#Adding a new element into an array
courses.append("Laravel")
print(courses)

#Deleting an element from an Array
courses.remove("Cybersecurity")
print(courses)