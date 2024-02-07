# JuniorExamRepo
Python Challenge Junior

To start the API use this command in terminal on the "JuniorExamRepo" folder = "uvicorn src1.routes_app:app --reload"
To start the WEB use this command in terminal on the "JuniorExamRepo" folder = "py src1/dash_app.py"

To start both use 2 terminals and run the commands.

API:
    • listing all objects
    • listing a single object
    • adding a new object
    • deleting an existing object
    • storing all these objects in a SQL or NoSQL database

For API I used: 
    -Poetry
    -FastAPI
    -NoSQL - MongoDB


For test API use this URL = "http://127.0.0.1:8000/docs#/":

/register_airplane/ 

    {
    "registration_number": "ABC123",
    "model": "Boeing 737",
    "flight_type": "DOM",                 //DOM/INT
    "source": "Boston",
    "destination": "Springvale"
    }

/log_landing/

    registration_number = "ABC123"
    reason = "Motor"
    runway_used = 1 

/log_departure/

    registration_number = "ABC123"
    gate = 2
    runway_used = 3

/list_all_objects/ 

    Just cick on "Execute"



Web Application:
    • displaying all objects in a list or table format
    • searching for a specific object in this list or table
    • deleting an object from this list or table
    • creating a new object and viewing it in the list/table


For WEB I used:
    -Poetry
    -Plotly dash

For test it use = "http://127.0.0.1:8050/"

To view all the tables with all the values, just click on the "CLICK HERE TO SEE THE TABLE" button.

Below are 3 checkbox (Airplanes, Landings, Departures), select 1 or more to search for id, registration_number, source (for airplanes table), destination (for airplanes table)
and in the text box write what you want to search.

Below is the "ADD OBJECT" button for adding in airplanes table
Just complete the fields with the new values and click on "ADD OBJECT"

For delete -> "Delete rows from Airplanes": to action this you must click on "Click here to see the table" to show the table "Airplanes", select the rows that you want to delete andd then click on the button "Delete rows from Airplanes".

Values that I used:
    .json file for airplanes table:
            [{
              "_id": 1,
              "registration_number": "asd",
              "model": "asdf",
              "flight_type": "ASD",
              "source": "SAD",
              "destination": "ASD"
            },
            {
              "_id": 4,
              "registration_number": "qqq",
              "model": "asdf",
              "flight_type": "asd",
              "source": "asd",
              "destination": "asd"
            },
            {
              "_id": 5,
              "registration_number": "aaa",
              "model": "aaa",
              "flight_type": "aaa",
              "source": "aaa",
              "destination": "aaa"
            },
            {
              "_id": 7,
              "registration_number": "aasxc1",
              "model": "asd",
              "flight_type": "int",
              "source": "sdf",
              "destination": "asd"
            },
            {
              "_id": 10,
              "registration_number": "ASDFG",
              "model": "SAD",
              "flight_type": "SADF",
              "source": "SADsdf",
              "destination": "sad"
            },
            {
              "_id": 11,
              "registration_number": "sdf",
              "model": "wdf",
              "flight_type": "wesdf",
              "source": "df",
              "destination": "sdf"
            },
            {
              "_id": 12,
              "registration_number": "asd",
              "model": "asdf",
              "flight_type": "asdf",
              "source": "asd",
              "destination": "swed"
            },
            {
              "_id": 14,
              "registration_number": "asd",
              "model": "asd",
              "flight_type": "asd",
              "source": "asd",
              "destination": "a111"
            },
            {
              "_id": 15,
              "registration_number": "asd",
              "model": "asdfg",
              "flight_type": "asdfg",
              "source": "asdfg",
              "destination": "Springvale"
            },
            {
              "_id": 16,
              "registration_number": "asd",
              "model": "asdfg",
              "flight_type": "asdfg",
              "source": "asdfg",
              "destination": "Springvale"
            },
            {
              "_id": 17,
              "registration_number": "aaaa",
              "model": "bbbb",
              "flight_type": "dom",
              "source": "ccc",
              "destination": "Springvale"
            },
            {
              "_id": 18,
              "registration_number": "abc123",
              "model": "Boeing 737",
              "flight_type": "DOM",
              "source": "New York",
              "destination": "Springvale"
            },
            {
              "_id": 19,
              "registration_number": "qwe",
              "model": "qwe",
              "flight_type": "qwe",
              "source": "qwe",
              "destination": "qwe"
            },
            {
              "_id": 21,
              "registration_number": "a1",
              "model": "a1",
              "flight_type": "a1",
              "source": "a1",
              "destination": "a1"
            },
            {
              "_id": 23,
              "registration_number": "q",
              "model": "q",
              "flight_type": "q",
              "source": "q",
              "destination": "q"
            },
            {
              "_id": 24,
              "registration_number": "w",
              "model": "w",
              "flight_type": "w",
              "source": "w",
              "destination": "w"
            },
            {
              "_id": 26,
              "registration_number": "aaaaa",
              "model": "string",
              "flight_type": "string",
              "source": "string",
              "destination": "Springvale"
            }]

    .json departures:
            [{
              "_id": 1,
              "registration_number": "2",
              "gate": 1,
              "departure_time": {
                "$date": "2024-02-06T14:22:31.055Z"
              },
              "runway_used": 2
            },
            {
              "_id": 2,
              "registration_number": "2",
              "gate": 1,
              "departure_time": {
                "$date": "2024-02-06T14:23:55.174Z"
              },
              "runway_used": 3
            },
            {
              "_id": 3,
              "registration_number": "1",
              "gate": 3,
              "departure_time": {
                "$date": "2024-02-06T15:13:07.365Z"
              },
              "runway_used": 1
            },
            {
              "_id": 4,
              "registration_number": "2",
              "gate": 1,
              "departure_time": {
                "$date": "2024-02-06T19:15:43.638Z"
              },
              "runway_used": 2
            },
            {
              "_id": 5,
              "registration_number": "q",
              "gate": 2,
              "departure_time": {
                "$date": "2024-02-07T16:43:22.801Z"
              },
              "runway_used": 1
            }]

    .json id_counters:
            [{
              "_id": "airplane_counter",
              "seq": 26
            },
            {
              "_id": "landing_counter",
              "seq": 9
            },
            {
              "_id": "departure_counter",
              "seq": 5
            }]

    .json landings:
                [{
              "_id": 1,
              "registration_number": "1",
              "reason": "asdf",
              "landing_time": {
                "$date": "2024-02-06T14:20:31.661Z"
              },
              "runway_used": 2
            },
            {
              "_id": 3,
              "registration_number": "2",
              "reason": "zxc",
              "landing_time": {
                "$date": "2024-02-06T14:27:07.097Z"
              },
              "runway_used": 1
            },
            {
              "_id": 4,
              "registration_number": "asdf",
              "reason": "sd",
              "landing_time": {
                "$date": "2024-02-06T14:46:17.550Z"
              },
              "runway_used": 1
            },
            {
              "_id": 5,
              "registration_number": "2",
              "reason": "xc",
              "landing_time": {
                "$date": "2024-02-06T15:12:57.382Z"
              },
              "runway_used": 2
            },
            {
              "_id": 6,
              "registration_number": "2",
              "reason": "sdf",
              "landing_time": {
                "$date": "2024-02-06T17:19:43.948Z"
              },
              "runway_used": 1
            },
            {
              "_id": 7,
              "registration_number": "2",
              "reason": "asdfgh",
              "landing_time": {
                "$date": "2024-02-06T19:15:06.250Z"
              },
              "runway_used": 2
            },
            {
              "_id": 8,
              "registration_number": "2",
              "reason": "aaaa",
              "landing_time": {
                "$date": "2024-02-06T19:15:22.311Z"
              },
              "runway_used": 2
            },
            {
              "_id": 9,
              "registration_number": "q",
              "reason": "sdf",
              "landing_time": {
                "$date": "2024-02-07T16:43:01.842Z"
              },
              "runway_used": 2
            }]
