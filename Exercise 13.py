"""
1. Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not.
Use the prior prime number exercise as a starting point. For example, a GET request for number 31 is given as
: http://127.0.0.1:5000/prime_number/31. The response must be in the format of {"Number":31, "isPrime":true}.
"""

from flask import Flask
import mysql.connector
app = Flask(__name__)


@app.route('/prime_number/<number>')
def prime_number(number):
    number = int(number)
    divisible = True
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                divisible = False
                break

    response = {
        "Number": number,
        "is Prime": divisible
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

"""
2. Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the 
airport in JSON format. The information is fetched from the airport database used on this course. For example, the GET 
request for EFHK would be: http://127.0.0.1:5000/airport/EFHK. The response must be in the format 
of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.
"""


from flask import Flask, Response
import json
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

app = Flask(__name__)


@app.route('/airport/<icao>')
def airport(icao):
    try:
        sql = 'SELECT airport.name, country.name from airport join country using (iso_country)'
        sql += ' WHERE ident = "' + icao + '"'
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                name = row[0]
                location = row[1]

        response = {
            "icao": icao,
            "airport_name": name,
            "Location": location
        }
        return response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

