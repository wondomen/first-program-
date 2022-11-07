"""
Exercise 11
1.Implement the following class hierarchy using Python: A publication can be either a book or a magazine. Each
publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor.
Also write the required initializers to both classes. Create a print_information method to both subclasses for printing
out all information of the publication in question. In the main program, create publications Donald Duck (chief editor
Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of both publications using
the methods you implemented.
"""


class Publication:

    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        print(f"The Book  {self.name}, (Author: {self.author}, {self.page_count},pages)")


class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        print(f"The Magazine {self.name},Chief editor is {self.editor}")


magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No.6", "Rosa Liksom", 192)
magazine.print_info()
book.print_info()

"""
2.Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric cars have the 
capacity of the battery in kilowatt-hours as their property. Gasoline cars have the volume of the tank in liters as their 
property. Write initializers for the subclasses. For example, the initializer of electric cars receives the registration 
number, maximum speed and battery capacity as its parameter. It calls the initializer of the base class to set the first 
two properties and then sets its capacity. Write a main program where you create one electric car (ABC-15, 180 km/h, 
52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars, make them drive for three hours 
and print out the values of their kilometer counters.
"""


class Car:


    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
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


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(registration_number, max_speed)

    def print_travel_distance(self):
        print(f"Travel distance of electric car, {self.registration_number}, is, {self.travelled_distance},km")


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, volume_tank):
        self.volume_tank = volume_tank
        super().__init__(registration_number, max_speed)

    def print_travel_distance(self):
        print(f"Travel distance of gasoline car, {self.registration_number}, is, {self.travelled_distance},km")


Ele_car = ElectricCar("ABC-15", 180, 52.5)
Gas_Car = GasolineCar("ABC-123", 165, 32.3)
Ele_car.acceleration(100)
Gas_Car.acceleration(100)
Ele_car.drive(3)
Gas_Car.drive(3)
Ele_car.print_travel_distance()
Gas_Car.print_travel_distance()
