 #Question-1

name = input("What is your name? ")
print("Hello, " + name + "!")

 #Question-2

radius = float(input("give the radius?"))
area = 3.1416* radius** 2
print("Area is " + str(area))

 #Question-3

lenght = float(input("give the length of the rectangle? "))
width = float(input("give the width of the rectangle? "))
perimeter = 2*(lenght + width)
area = lenght * width
print("The perimeter of the rectangle is " + str(perimeter) + " and " + "The area of the rectangle is " + str(area))

 #Question-4

print("Give me three integer numbers than I will give you the sum, the product and the average of the three numbers ")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd  number: "))
num3 = int(input("Enter 3rd number: "))
sum = num1+num2+num3
product = num1*num2*num3
average = sum/3
print("the sum is " + str(sum) + " the product is " + str(product) + " and the average is " + str(average))

 #Question-5

Mass_Talent= float(input("Enter the mass in talents: "))
Talent_kg = 0.8521*Mass_Talent
Talent_g = 8521*Mass_Talent
if Mass_Talent >=0:
    print("The weight in moder units: " + str(Talent_kg) + " kilograms " "and " + str(Talent_g) + " grams")
else:
    print("Sorry! No results for this")

Mass_Pound = float(input("Enter the mass in pounds: "))
Pound_kg = 0.4256*Mass_Pound
Pound_g = 4256*Mass_Pound
if Mass_Pound >=0:
    print("The weight in moder units: " + str(Pound_kg) + " kilograms " "and " + str(Pound_g) + " grams")
else:
    print("Sorry! No solutions for this")

Mass_lots = float(input("Enter the mass in lots: "))
lots_kg = 0.0133*Mass_lots
lots_g = 13.3*Mass_lots
if Mass_lots >=0:
    print("The weight in moder units: " + str(lots_kg) + " kilograms " "and " + str(lots_g) + " grams")
else:
    print("Sorry! No results for this ")

 #Question- 6

import math
import numbers
import random
print(str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)))

import math
import numbers
import random
print(str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)))


#secret_code1 = "NATO"
#secret_code2 = "EU"
#answer = input("what is the secret code?")
#if answer == secret_code1:
#   print("correct!")
#elif answer == secret_code2:
#   print("Also correct")

#else:
 #  print("not correct")


