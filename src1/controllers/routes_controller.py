from fastapi import FastAPI, HTTPException, APIRouter, Depends
from typing import List
from datetime import datetime
from pymongo import MongoClient
from models.airplane import Airplane
from controllers.airport_controller import AirportController

app = FastAPI()
airport_controller = AirportController()

router = APIRouter()

@router.post("/register_airplane")
def register_airplane(airplane: Airplane):
    airport_controller.register_airplane(airplane)
    return {"message": "Airplane registered successfully"}

@router.post("/log_landing")
def log_landing(registration_number: str, reason: str, runway_used: int):
    airport_controller.log_landing(registration_number, reason, runway_used)
    return {"message": "Landing logged successfully"}

@router.post("/log_departure")
def log_departure(registration_number: str, gate: int, runway_used: int):
    airport_controller.log_departure(registration_number, gate, runway_used)
    return {"message": "Departure logged successfully"}

@router.get("/list_all_objects")
def list_all_objects():
    return airport_controller.list_all_objects()

@router.get("/list_single_object/{object_type}/{identification_number}")
def list_single_object(object_type: str, identification_number: str):
    return airport_controller.list_single_object(object_type, identification_number)

@router.delete("/delete_object/{object_type}/{identification_number}")
def delete_object(object_type: str, identification_number: str):
    if airport_controller.delete_object(object_type, identification_number):
        return {"message": f"{object_type.capitalize()} with ID {identification_number} deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"{object_type.capitalize()} with ID {identification_number} not found")

@router.get("/get_airplane_by_id/{registration_number}")
def get_airplane_by_id(registration_number: str):
    airplane = airport_controller.get_airplane_by_id(registration_number)
    if airplane:
        return airplane
    else:
        raise HTTPException(status_code=404, detail=f"Airplane with registration number {registration_number} not found")

app.include_router(router)

