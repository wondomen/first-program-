#Exersice 8

#Question 1:- Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints
# out the corresponding airport name and location (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.

import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
     )

def get_airport_names():
    sql = "SELECT name from airport order by name desc"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(row)
print(get_airport_names())

#Question 2:-Write a program that asks the user to enter the area code (for example FI) and prints out the airports located
# in that country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.

areaCode = input("Input the area code (i.e. FI): ")
cursor = connection.cursor()
cursor.execute(f"select country.name as 'country name', airport.name as 'airport name', airport.type as 'airport type' from country, airport where country.iso_country = airport.iso_country and airport.iso_country = '{areaCode}' order by airport.type;")
result = cursor.fetchall()
print(result)

#Question 3:-Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance
# between the two airports in kilometers. The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. Install the library by selecting
# View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the installation.

from geopy import distance
cursor = connection.cursor()
icao1 = input("Input the first ICAO code: ")
cursor.execute(f"select name from airport where ident = '{icao1}';")
result = cursor.fetchall()
print(result)
icao2 = input("Input the second ICAO code: ")
cursor.execute(f"select name from airport where ident = '{icao2}';")
result = cursor.fetchall()
print(result)
cursor.execute(f"select latitude_deg, longitude_deg from airport where ident = '{icao1}' or ident = '{icao2}';")
listDeg = []
for x in cursor:
    listDeg.append(x)
print(f"The distance between 2 airports is", f"{distance.distance(listDeg[0], listDeg[1]).km:.2f} km")
