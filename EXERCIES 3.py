#Question 1

length_zander = int(input("Enter the length of the zander in centimeter "))
if length_zander < 42:
    print("release the fish back into the lake" + "the lenght of the fish is below", abs(length_zander - 42))
else:
    print("Enjoy the fish ")

# Question 2

Cabin_class = str(input("Enter the cabin class:- "))
lux = Cabin_class
A = Cabin_class
B = Cabin_class
C = Cabin_class
if 'lux' == lux:
    print("upper deck cabin with a balcony")
elif 'A'== A:
    print("above the car deck, equipped with a window")
elif 'B' == B:
    print("windowless cabin above the car deck")
elif 'C' == C:
    print("windowless cabin below the car deck")
else:
     print("Invalid cabin class")

 #Question 3

Gender = input("Enter your gender M if you are male and F if you are female:-  ")
hemoglobin_value = int(input("Enter your hemoglobin value in g/l"))
if Gender == "F":
   if 117 <= hemoglobin_value <= 155:
        print("your hemoglobin level is normal")
   if hemoglobin_value > 155:
        print("your hemoglobin level is high ")
   else:
       print("your hemoglobin level is low ")
if Gender == "M":
   if 134 <= hemoglobin_value <= 167:
       print("your hemoglobin level is normal")
   if hemoglobin_value > 167:
       print("your hemoglobin level is high ")
   else:
       print("your hemoglobin level is low ")

#question 4

year = int(input("Enter the year:- "))

if(year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(str("this year is a leap year".format(year)))
        else:
            print(str("this year is not a leap year".format(year)))
    else:
        print(str("this year is a leap year".format(year)))
else:
    print(str("this year is not a leap year".format(year)))
