import random
import math
# Exercise 5


# Question 1:
# Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the the sum of the numbers. Use a for loop.

num_dice = int(input("Enter how many dice you want to roll? "))
sum_roll = 0
for i in range(num_dice):
    #Note: dice = random.randint(1,6) if we use this one the next line will be "sum_roll = sum_roll + dice"
    sum_roll = sum_roll + random.randint(1, 6)
print("The out put sum of all dice is: ", sum_roll)

#Note: alternative solution foe question number 1, and if you want to print each roll values

num_dice = int(input("Enter how many dice you want to roll? "))
sum_roll = 0
for i in range(num_dice):
    dice = random.randint(1,6)
    print(str(dice), end="")
    sum_roll = sum_roll + dice
print("The out put sum of all dice is: ", sum_roll)

# Question 2
#Write a program that asks the user to enter numbers until they input an empty string to quit. At the end,
# the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

listnum = []
num = input("Enter at list five numbers you want?  ")
while num != "":
    listnum.append(num)
    num = input("Enter a numbers you want")
    listnum.sort(reverse=True)
print("the first five greatest number are ")
for i in range(5):
    print(listnum[i], end="")

# alternative solution for Question number 2
numbers = []
prompt = "Give me the number"
s= input(prompt)
while s != "":
    numbers.append(float(s))
    s = input(prompt)
numbers.sort(reverse=True)
print(numbers[0:5])


#Question 3

#Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.

x = int(input("Enter an integer number"))
x_half = x // 2
divisible = False
for i in range(2, x_half + 1):
    if x % i == 0:
        divisible = True
        break
if divisible == False:

    print("This is a prime number")
else:
    print("This is not a prime number")

# Alternative answer for question #

n= int(input("Give me the number"))
for i in range(2, int(math.sqrt(n))+1): # this is found on wikipedia
    if n%i == 0:
        print(f"Dividable by {i} it is not prime")
        break
else:
    print("It is a prime number")


# Question 4
#Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names) and stores them into a list structure.
# Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.

city_list = []
user = str("Pleas enter any five cites you like? ")
print(user)
for i in range(5):
    city_list.append(input("Name of cities: "))
for i in range(5):
    print(city_list[i])

# Exercise 6

# Question 1

#Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6. T
# he main program should print out the result of each roll.

import random
import math
def roll_dice():
    return random.randint(1, 6)
x = roll_dice()
while x != 6:
    print(x)
    x = roll_dice()
print(x)

#Alternative solution for question 1


#Question 2

#Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.The
# difference to the last exercise is that the dice rolling in the main program continues until the
# program gets the maximum number on the dice, which is asked from the user at the beginning.

def roll_dice(sides):
    return random.randint(1, sides)
num_sides = int(input("Enter how many sides the dice has? "))
x = roll_dice(num_sides)
while x != num_sides:
    print(x)
    x = roll_dice(num_sides)
print(num_sides)

#alternative solution for question 2
 def dice_roll_max(n):
     return random.randint(1, n)

 n = int(input("How many sides in your dice? "))
 while True:
     dice = dice_roll_max(n)
     print(f"Dice {dice}")
     if dice == n
         not finnished
#Question 3

#Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

def gallon_litter(gallon):
    return gallon * 3.785
num_gallon = float(input("Enter the gallon:- "))
while num_gallon >=0:
   print("equal to ", + gallon_litter(num_gallon),  "litters")
   num_gallon = float(input("Enter the gallon:- "))

#Alternative solution question 3
def gallon_litter(gallon):
    return gallon * 3.785
while True:
    num_gallon = float(input("Enter the gallon:- "))
    if num_gallon < 0:
        break
   print(f"{num_gallon} gallons are {gallon_litter(num_gallon):.1f} litres, ")

#Question 4

#Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list.
#For testing, write a main program where you create a list, call the function, and print out the value it returned.

def sumlist(integers):
    total_sum = 0
    for i in integers:
        total_sum = i + 1
    return total_sum
print("The sum of the list is:-", + sum((1, 2, 4, 6, 8, 10)))


#Question 5

#Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise
# the same as the original list except that all uneven numbers have been removed. For testing, write a main program
# where you create a list, call the function, and then print out both the original as well as the cut-down list.

def list(integer_list):
    sec_list = []
    for i in integer_list:
        if i % 2 == 0:
            sec_list.append(i)
    print("first list: ", integer_list)
    print("second list: ", sec_list)
first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 23,22]
list(first_list)

#Alternative solution for 5
def make_even(l):
    result = []
    for i in range(len(l)):
        if l[i]% 2 == 0:
            result.append(l[i])
    return result
def print_list(prompt, l):
    print(prompt, end=":")
    for i in range(len(l)):
        print(l[i], end="")

numberlist = []
for n in range(10):
    numberlist.append(random.randint(1, 99)) # generate a test sequence
print_list("original list", numberlist)
newlist = make_even(numberlist)
print_list("\nModified list", newlist)
print()

#Question 6

#Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros.
# The function calculates and returns the unit price of the pizza per square meter. The main program asks the user
# to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money (which of them has a
# lower unit price). You must use the function you wrote for calculating the unit prices.

def cal_pizza_price(diameter, price, pizza):
    area_pizza = math.pi * (diameter / 200) ** 2
    print("the price of the pizza-", pizza, "per square meter is:-",  price / area_pizza)
    return price / area_pizza
pizza1 = float(input("Enter the diameter of the pizza1 in cm: "))
price_pizza1 = float(input("Enter the price of pizza1 in euro: "))
pizza2 = float(input("Enter the diameter of the pizza2 in cm: "))
price_pizza2 = float(input("Enter the price of pizza2 in euro: "))
c1 = cal_pizza_price(pizza1, price_pizza1, 1)
c2 = cal_pizza_price(pizza2, price_pizza2, 2)
if c1 < c2:
    print("pizza1 is cheaper than pizza2")
elif c1 > c2:
    print("pizza2 is cheaper than pizza1")
else:
    print("pizza1 has same price as pizza2")

