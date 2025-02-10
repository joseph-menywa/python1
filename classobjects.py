class student:
    #properties/Attributes
    name = "Joe"
    gender = "Male"
    hieght = 165

    #Behavior/Method
    def study(self):
        print("Student is studying")


student1 = student()    #creating an object
student1.study()
print(student1.name)



student2 = student()