import random
import math
# Question 1

n = 1
while  n <= 1000:
    if n%3 == 0:
       print(int(n))
    n = n + 1
# Question 2

length_inch = float(input("Enter the length in inch "))
length_cm = 2.54 * length_inch
while length_inch >= 0:
    print(length_cm)
    length_inch = float(input("Enter the length in inch "))


# Question number 3 alternative
prompt = "Give a number?"
s= input(prompt)
if s != "":
    smallest = int(s)
    largest = smallest
while s != "":
    n = int(s)
    if n < smallest:
        smallest = n
    if n > largest:
        largest = n
    s = input(prompt)
else:
    print("the largest is " , largest)
    print('smallest is ', smallest)


 # Question 4

import random
number = random.randint(1, 10)
attempts = 0
guess = 0
while guess != number:
    guess = eval(input("Guess a number: "))
    attempts = 1 + attempts
    if guess == number:
        print("Correct")
        break
    elif guess > number:
        print("Too high")
    else:
        print("Too low")

# Question 5

print("username and password")
count = 0
while count < 5:
    username = input("Enter username ")
    password = input("Enter pass word ")
    if username == "python" and password == "rules" and count < 5:
        print("Welcome")
        break
    else:
        print("Access denied ")
        count = 1 + count

#Question 6

import random
n = 0
count = float(input("Enter how many random points to generate?  "))
inside = 0
while n != count:
    rand_x = random.uniform(-1,1)
    rand_y = random.uniform(-1,1)
    n = n + 1

    if (rand_x**2) + (rand_y**2) < 1:
        inside = inside + 1
pi = float
Pi = 4 * inside / count
print("the approximate value of pi is:" ,pi)