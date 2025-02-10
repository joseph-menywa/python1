# Built-in functions/Standard library functions

y = max(67, 45,64, 74,83,34,100,455,67,90)
print("the maximum value is", y)

x = min(30,85,79,67,90,38,12,50,11)
print("The minimum value is", x)


#User-defined functions
def name():
    print("joseph")
name() # calling a function

def product():
    a = 10
    b = 2
    print(a * b)
product()


#Parameter/Variable and Argument/Value
def add(t, f):
     print(t+f)
add(7,6)

def employee(Name,Gender,Position,Salary,Age):
    print(Name,Gender,Position,Salary,Age)
employee("John","Male","CEO",40900,50)
employee("Mark","Male","Manager",30000,30)
employee("Phillip","Male","Secritery Director",32500,60)
employee("Clare","Female","Organiser",32500,60)


print("")
print("")
print("")


# A Programme that displays details of five students
# Use a user-defined function with the help of parameter and argument
#display : Fullname, Age, Gender

def student(Fullname,Age,Gender):
    print(Fullname, Age, Gender)
student("Frankline Okwonko",20,"Male")
student("Jackline Cate",18,"Female")
student("Farida Judy",17,"Female")
student("Bruno Faizal",22,"Male")
student("Hamisi Abdala",19,"Male")

