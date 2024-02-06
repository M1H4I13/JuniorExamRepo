from typing import List
from datetime import datetime
from pymongo import MongoClient
from models.airplane import Airplane

# Define MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['airport']
airplanes_collection = db['airplanes']
landings_collection = db['landings']
departures_collection = db['departures']
counter_collection = db['id_counters']

class AirportController:
    def __init__(self):
        # Initialize counters if they don't exist
        if not counter_collection.find_one({"_id": "airplane_counter"}):
            counter_collection.insert_one({"_id": "airplane_counter", "seq": 0})
        if not counter_collection.find_one({"_id": "landing_counter"}):
            counter_collection.insert_one({"_id": "landing_counter", "seq": 0})
        if not counter_collection.find_one({"_id": "departure_counter"}):
            counter_collection.insert_one({"_id": "departure_counter", "seq": 0})

    def register_airplane(self, airplane: Airplane):
        counter_doc = counter_collection.find_one_and_update(
            {"_id": "airplane_counter"},
            {"$inc": {"seq": 1}},
            return_document=True
        )
        airplane_id = counter_doc['seq']
        airplane_dict = airplane.dict()
        airplane_dict['_id'] = airplane_id  # Assign the generated ID to the airplane document
        airplanes_collection.insert_one(airplane_dict)

    def log_landing(self, registration_number: str, reason: str, runway_used: int):
        counter_doc = counter_collection.find_one_and_update(
            {"_id": "landing_counter"},
            {"$inc": {"seq": 1}},
            return_document=True
        )
        landing_id = counter_doc['seq']
        landing_instance = {
            "_id": landing_id,
            "registration_number": registration_number,
            "reason": reason,
            "landing_time": datetime.now(),
            "runway_used": runway_used
        }
        landings_collection.insert_one(landing_instance)
        return True
    
    def log_departure(self, registration_number: str, gate: int, runway_used: int):
        counter_doc = counter_collection.find_one_and_update(
            {"_id": "departure_counter"},
            {"$inc": {"seq": 1}},
            return_document=True
        )
        departure_id = counter_doc['seq']
        departure_instance = {
            "_id": departure_id,
            "registration_number": registration_number,
            "gate": gate,
            "departure_time": datetime.now(),
            "runway_used": runway_used
        }
        departures_collection.insert_one(departure_instance)
        return True

    def list_all_objects(self):
        airplanes = list(airplanes_collection.find())
        landings = list(landings_collection.find())
        departures = list(departures_collection.find())
        return {
            'airplanes': airplanes,
            'landings': landings,
            'departures': departures
        }

    def list_single_object(self, object_type: str, identification_number: str):
        if object_type == 'airplanes':
            # Search for the airplane using the registration number
            airplane = airplanes_collection.find({"_id": int(identification_number)}).limit(1).next()
            return [airplane] if airplane else []
        elif object_type == 'landings':
            # Search for the landing using the _id
            landing = landings_collection.find({"_id": int(identification_number)}).limit(1).next()
            return [landing] if landing else []
        elif object_type == 'departures':
            # Search for the departure using the _id
            departure = departures_collection.find({"_id": int(identification_number)}).limit(1).next()
            return [departure] if departure else []
        else:
            return []

    def delete_object(self, object_type: str, identification_number: str):
        if object_type == 'airplanes':
        # Search for the airplane using the _id
            airplane = airplanes_collection.find_one_and_delete({"_id": int(identification_number)})
            return airplane is not None
        elif object_type == 'landings':
            # Search for the landing using the _id
            landing = landings_collection.find_one_and_delete({"_id": int(identification_number)})
            return landing is not None
        elif object_type == 'departures':
            # Search for the departure using the _id
            departure = departures_collection.find_one_and_delete({"_id": int(identification_number)})
            return departure is not None
        else:
            return False

    def get_airplane_by_id(self, registration_number: str):
        return airplanes_collection.find_one({"registration_number": registration_number})
