import random
"""
1,Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled
distance. Add a class initializer that sets the first two of the properties based on parameter values. The current
speed and travelled distance of a new car must be automatically set to zero. Write a main program where you create a new
car (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties of the new car.
"""
class Car:
    def __init__(self,registration_number, maximum_speed):
        self.registration_number= registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def show(self):
        print("Register number of ",self.registration_number, "Its maximum speed is ",self.maximum_speed,"Km/hr",
              "current speed is ",self.current_speed, "current travel distance is ", self.travelled_distance)
new_car = Car("ABC-123",142)
new_car.show()

"""
2.Extend the program by adding an accerelate method into the new class. The method should receive the change of speed 
(km/h) as a parameter. If the change is negative, the car reduces speed. The method must change the value of the speed 
property of the object. The speed of the car must stay below the set maximum and cannot be less than zero. Extend the
main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h. Then print 
out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed and 
then print out the final speed. The travelled distance does not have to be updated yet.

"""
class Car:
    def __init__(self,registration_number, maximum_speed):
        self.registration_number= registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def acceleration(self,change_speed):
        self.current_speed = min(max(self.current_speed + change_speed, 0), self.maximum_speed)

new_car = Car("ABC-123",142)
new_car.acceleration(30)
print(f"current speed is {new_car.current_speed} km/h")
new_car.acceleration(70)
print(f"current speed is {new_car.current_speed} km/h")
new_car.acceleration(50)
print(f"current speed is {new_car.current_speed} km/h")
new_car.acceleration(-200)
print(f"current speed is {new_car.current_speed} km/h")


"""
3.Again, extend the program by adding a new drive method that receives the number of hours as a parameter. The method 
increases the travelled distance by how much the car has travelled in constant speed in the given time. Example: The 
travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5) 
increases the travelled distance to 2090 km.
"""

class Car:
    def __init__(self,registration_number, maximum_speed):
        self.registration_number= registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 200

    def show(self):
        print("Register number of ", self.registration_number, "Its maximum speed is ", self.maximum_speed, "Km/hr",
              "current speed is ", self.current_speed, "current travel distance is ", self.travelled_distance)

    def acceleration(self, change_speed):
        self.current_speed = min(max(self.current_speed + change_speed, 0), self.maximum_speed)

    def drive(self, time):
        self.travelled_distance += self.current_speed * time


new_car = Car("ABC-123",142)
new_car.acceleration(60)
new_car.drive(1.5)
print(f"Distance traveled was {new_car.travelled_distance}km")

"""
4.Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the 
main program, create a list that consists of 10 car objects created using a loop. The maximum speed of each new car is a 
random value between 100 km/h and 200 km/h. The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. 
Now the race begins. One per every hour of the race, the following operations are performed:
The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is 
done using the accelerate method. Each car is made to drive for one hour. This is done with the drive method.The race 
continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each car are 
printed out formatted into a clear table.
"""


class Car:
    def __init__(self,registration_number, maximum_speed):
        self.registration_number= registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 200

    def acceleration(self, change_speed):
        self.current_speed = min(max(self.current_speed + change_speed, 0), self.maximum_speed)

    def drive(self, time):
        self.travelled_distance += self.current_speed * time
car_list =[]
for i in range(10):
    car_list.append(Car("ABC-"+ str(i+1),random.randint(100, 200)))
max_travel = 0
while max_travel < 10000:
    for new_car in car_list:
        new_car.acceleration(random.randint(-10, 15))
        new_car.drive(1)
        max_travel= max(new_car.travelled_distance, max_travel)
for new_car in car_list:
    print(f"{new_car.registration_number :6s}: {new_car.maximum_speed}, {new_car.travelled_distance}")
print(f"The winner covered a total distance of : {max_travel}")
