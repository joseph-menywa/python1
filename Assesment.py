#Programm that allow you to check if a number is prime number or not
num = int(input("Enter number: "))
if num > 1:
    for i in range(2, (num // 2) + 1):
        if (num % i) == 0:
            break
    else:
       print(num, "is prime number")
else:
    print(num, "is not prime number")