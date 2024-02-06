from typing import List
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel

# Define MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['airport']
airplanes_collection = db['airplanes']
landings_collection = db['landings']
departures_collection = db['departures']
counter_collection = db['id_counters']

class Airplane(BaseModel):
    registration_number: str
    model: str
    flight_type: str  # 'DOM' for domestic, 'INT' for international
    source: str
    destination: str = "Springvale"

class Landing(BaseModel):
    registration_number: str
    reason: str
    landing_time: datetime
    runway_used: int

class Departure(BaseModel):
    registration_number: str
    gate: int
    departure_time: datetime
    runway_used: int

app = FastAPI()

@app.post("/register_airplane/")
async def register_airplane(airplane: Airplane):
    counter_doc = counter_collection.find_one_and_update(
        {"_id": "airplane_counter"},
        {"$inc": {"seq": 1}},
        return_document=True
    )
    airplane_id = counter_doc['seq']
    airplane_dict = airplane.dict()
    airplane_dict['_id'] = airplane_id  # Assign the generated ID to the airplane document
    airplanes_collection.insert_one(airplane_dict)
    return {"message": "Airplane registered successfully!"}

@app.post("/log_landing/")
async def log_landing(registration_number: str, reason: str, runway_used: int):
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
    return {"message": "Landing logged successfully!"}

@app.post("/log_departure/")
async def log_departure(registration_number: str, gate: int, runway_used: int):
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
    return {"message": "Departure logged successfully!"}

@app.get("/list_all_objects/")
async def list_all_objects():
    airplanes = list(airplanes_collection.find())
    landings = list(landings_collection.find())
    departures = list(departures_collection.find())
    return {
        'airplanes': airplanes,
        'landings': landings,
        'departures': departures
    }

@app.get("/list_single_object/")
async def list_single_object(object_type: str, identification_number: str):
    if object_type == 'airplanes':
        airplane = airplanes_collection.find_one({"_id": int(identification_number)})
        if airplane:
            return [airplane]
    elif object_type == 'landings':
        landing = landings_collection.find_one({"_id": int(identification_number)})
        if landing:
            return [landing]
    elif object_type == 'departures':
        departure = departures_collection.find_one({"_id": int(identification_number)})
        if departure:
            return [departure]
    raise HTTPException(status_code=404, detail="Object not found")

@app.delete("/delete_object/")
async def delete_object(object_type: str, identification_number: str):
    if object_type == 'airplanes':
        airplane = airplanes_collection.find_one_and_delete({"_id": int(identification_number)})
        if airplane:
            return {"message": "Object deleted successfully."}
    elif object_type == 'landings':
        landing = landings_collection.find_one_and_delete({"_id": int(identification_number)})
        if landing:
            return {"message": "Object deleted successfully."}
    elif object_type == 'departures':
        departure = departures_collection.find_one_and_delete({"_id": int(identification_number)})
        if departure:
            return {"message": "Object deleted successfully."}
    raise HTTPException(status_code=404, detail="Object not found")
