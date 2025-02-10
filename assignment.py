#A programme to check whether a year is a leap year or not

year = 2020
if ((year % 4 == 0 and year % 100 != 0)
        or (year % 400 == 0)):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#A programme to check whether a letter is a consonant or a vowel
vowel1 = "AEIOUaeiou"
letter = "t"
if letter in vowel1 :
    print(letter,"letter is Vowel")
else:
    print(letter,"letter is consonant")