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

