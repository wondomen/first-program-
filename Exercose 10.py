"""
Exercise 10
1.Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. The elevator
has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor. If you make elevator h
for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times
as it needs to get to the fifth floor. The methods run the elevator one floor up or down and tell what floor the elevator
is after each move. Test the class by creating an elevator in the main program, tell it to move to a floor of your choice
and then back to the bottom floor.
"""

class Elevator:
    def __init__(self,bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
    def floor_up(self):
        if self.current < self.top:
            print(f"The elevator is moving up from {self.current} to {self.current + 1}")
            self.current +=1
            return True

        else:
            return False
    def floor_down(self):
        if self.current > self.bottom:
            print(f"The elevator is moving down from {self.current} to {self.current - 1}")
            self.current -=1
            return True
        else:
            return False
    def go_to_floor(self, floor):

        if floor > self.current:
            for i in range (floor - self.current):
                if not self.floor_up():
                    break
        elif floor < self.current:
            for i in range(self.current - floor):
                if not self.floor_down():
                    break
        else:
            print(f"You are already at this floor: {self.current}")

h = Elevator(1,5)
target_floor = int(input("which floor would you like to go? "))
h.go_to_floor(target_floor)
h.go_to_floor(1)
"""
2.Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers of 
the bottom and top floors and the number of elevators in the building. When a building is created, the building creates 
the required number of elevators. The list of elevators is stored as a property of the building. Write a method called 
run_elevator that accepts the number of the elevator and the destination floor as its parameters. In the main program, 
write the statements for creating a new building and running the elevators of the building.
"""

class Building:
    def __init__(self,bottom, top, elevator_list):
        self.elevator_list = []
        for i in range (elevator_list):
            self.elevator_list.append(Elevator(bottom,top))
    def run_elevator(self, elevator_no, floor):
        print()
        print(f"The elevator number {elevator_no} is running")
        self.elevator_list[elevator_no - 1].go_to_floor(floor)



print("Elevators in the building:")
building = Building(1, 7 , 3)
building.run_elevator(1,4)


"""
3.Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to 
the bottom floor. Continue the main program by causing a fire alarm in your building.
"""
class Building:
    def __init__(self,bottom, top, elevator_list):
        self.elevator_list = []
        for i in range (elevator_list):
            self.elevator_list.append(Elevator(bottom,top))
    def run_elevator(self, elevator_no, floor):
        print()
        print(f"The elevator number {elevator_no} is running")
        self.elevator_list[elevator_no - 1].go_to_floor(floor)

    def fire_alarm(self):
        print("--------------")
        print("FIRE!!!!")
        for i in self.elevator_list:
            i.go_to_floor(i.bottom)

print("Elevators in the building:")
building.run_elevator(1,4)
building = Building(1, 7, 3)
building.fire_alarm()

"""
4. This exercise continues the previous car race exercise from the last exercise set. Write a Race class that has the 
following properties: name, distance in kilometers and a list of cars participating in the race. The class has an 
initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding 
properties in the class. The class has the following methods:
hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of 
speed for each car and calls their drive method.
print_status, which prints out the current information of each car as a clear, formatted table.
race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire 
distance of the race.
Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list of 
ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the hour_passes
in a loop, after which it uses the race_finished method to check if the race has finished. The current status is printed 
out using the print_status method every ten hours and then once more at the end of the race.
"""

import random
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


class Race:
    def __init__(self, name, distance, cars_list):
        self.name = name
        self.distance = distance
        self.cars_list = cars_list
    def hour_passes(self):
        for new_car in self.cars_list:
            new_car.acceleration(random.randint(-10, 15))
            new_car.drive(1.)
    def print_status(self):
        print(self.name + ":")
        for new_car in self.cars_list:
            print(f"{new_car.registration_number:6s}: {new_car.current_speed:3d}, {new_car.travelled_distance} km")

    def race_finished(self):
        for new_car in self.cars_list:
            if new_car.travelled_distance >= self.distance:
                return True
        return False
cars_list = []
for i in range(10):
    cars_list.append(Car("ABC-" + str(i+1), random.randint(100,200)))
race = Race("Grand Demolition Derby", 8000, cars_list)
n = 0
while not race.race_finished():
    race.hour_passes()
    n +=1
    if n%10 == 0:
        print(f"After {n} hours")
        race.print_status()
print(f"The final result after {n} hours is:")
race.print_status()
