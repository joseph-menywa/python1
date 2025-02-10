"""""
Simple calculator programme with 
enter first number,operator,second number esl "entered an invalid operator"
"""""
from random import choice


#This function adds two numbers
def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2

print("please enter the operations -/n"
      "1. addition/n"
      "2. subtraction/n"
      "3. multiplication/n"
      "4. division/n")

selection = int(input("please select operator: "))
num1 = int(input("please enter first number: "))
num2 = int(input("please enter second number: "))

if selection == "+":
    print(num1,"+", num2,"=", addition(num1, num2))
elif selection == "-":
    print(num1,"-", num2,"=", subtraction(num1, num2))
elif selection == "*":
    print(num1,"*", num2,"=", multiplication(num1, num2))
elif selection == "/":
    print(num1,"/", num2,"=", division(num1, num2))
else:
    print("please enter a valid number")





