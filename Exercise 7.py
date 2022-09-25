#Exersice 7

#Question 1:-Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.

season = ("Spring", "Summer", "Autumn", "Winter")
month = [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 1, 2]
user_input = int(input("Enter the month in number (1..12:)"))
for i in range(len(month)):
    if user_input in month[i]:
        print(season[i])

#Question 2:-Write a program that asks the user to enter names until he/she enters an empty string. After each name is read
# the program either prints out New name or Existing name depending on whether the name was entered for the first time.
# Finally, the program lists out the input names one by one, one below another in any order. Use the set data structure
# to store the names.

name = set()
namelist = []
user_input = str(input("Enter the names: "))
while user_input != "":
    namelist.append(user_input)
    if user_input not in name:
        namelist.append(user_input)
        name.update(namelist)
        print("New name")
    else:
        print("Existing name")
    user_input = str(input("Enter the names: "))
for i in name:
    print(i)


#Question 3:-Write a program for fetching and storing airport data. The program asks the user if they want to enter a new
# airport,fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program
# asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead,
# the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit,
# the program execution ends. The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport
# is EFHK. You can easily find the ICAO codes of different airports online.)
# https://www.airport-data.com/world-airports/countries/FI-Finland-Airports.html

airport_data = {}
def asking_info():
    print("Choose what you want to do:")
    print("n: add new airport")
    print("f: fetch airport name")
    print("ENTER to quit program")
    return input()

query = asking_info()
while query == "n" or query == "f":
    if query == "n":
        new_icao = input("input ICAO code: ")
        new_name = input("input name of airport: ")
        airport_data.update({new_icao: new_name})
    else:
        icao = input("input ICAO code: ")
        if icao in airport_data:
            print("Airport name:", airport_data[icao])
        else:
            print("Sorry! Airport not found")
    query = asking_info()
print("Thank you! Bye!")