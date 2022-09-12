import random
import math
# Exercise 5

# Question 1

num_dice = int(input("Enter how many dice you want to roll? "))
sum_roll = 0
for i in range(num_dice):
    sum_roll = sum_roll + random.randint(1, 6)
print("The out put sum of all dice is: ", sum_roll)

# Question 2
listnum = []
num = input("Enter at list five numbers you want?  ")
while num != "":
    listnum.append(num)
    num = input("Enter a numbers you want")
    listnum.sort(reverse=True)
print("the first five greatest number are ")
for i in range(5):
    print(listnum[i], end="")

#Question 3

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


# Question 4

city_list = []
user = str("Pleas enter any five cites you like? ")
print(user)
for i in range(5):
    city_list.append(input("Name of cities: "))
for i in range(5):
    print(city_list[i])

# Exercise 6

# Question 1
import random
import math
def roll_dice():
    return random.randint(1, 6)
x = roll_dice()
while x != 6:
    print(x)
    x = roll_dice()
print(x)

#Question 2

def roll_dice(sides):
    return random.randint(1, sides)
num_sides = int(input("Enter how many sides the dice has? "))
x = roll_dice(num_sides)
while x != num_sides:
    print(x)
    x = roll_dice(num_sides)
print(num_sides)

#Question 3

def gallon_litter(gallon):
    return gallon * 3.785
num_gallon = float(input("Enter the gallon:- "))
while num_gallon >=0:
   print("equal to ", + gallon_litter(num_gallon),  "litters")
   num_gallon = float(input("Enter the gallon:- "))

#Question 4

def sumlist(integers):
    total_sum = 0
    for i in integers:
        total_sum = i + 1
    return total_sum
print("The sum of the list is:-", + sum((1, 2, 4, 6, 8, 10)))


#Question 5

def list(integer_list):
    sec_list = []
    for i in integer_list:
        if i % 2 == 0:
            sec_list.append(i)
    print("first list: ", integer_list)
    print("second list: ", sec_list)
first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 23,22]
list(first_list)

#Question 6

def cal_pizza_price(diameter, price, pizza):
    area_pizza = math.pi * diameter * diameter / 4
    print("the price of the pizza-", pizza, "per square meter is:-",  price / area_pizza)
    return price / area_pizza
pizza1 = float(input("Enter the diameter of the pizza1 in cm: "))
price_pizza1 = float(input("Enter the price of pizza1 in euro: "))
pizza2 = float(input("Enter the diameter of the pizza2 in cm: "))
price_pizza2 = float(input("Enter the price of pizza2 in euro: "))
if cal_pizza_price(pizza1, price_pizza1, 1) < cal_pizza_price(pizza2, price_pizza2, 2):
    print("pizza1 is cheaper than pizza2")
elif cal_pizza_price(pizza1, price_pizza1, 1) > cal_pizza_price(pizza2, price_pizza2, 2):
    print("pizza2 is cheaper than pizza1")
else:
    print("pizza1 has same price as pizza2")
