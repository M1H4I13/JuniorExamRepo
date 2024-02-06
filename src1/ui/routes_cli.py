from fastapi import FastAPI, HTTPException, APIRouter
from controllers.airport_controller import AirportController
from models.airplane import Airplane
from typing import List

app = FastAPI()
airport_controller = AirportController()

router = APIRouter()

@router.post("/airport_cli_menu")
def airport_cli_menu(option: str, registration_number: str = None, reason: str = None, runway_used: int = None, gate: int = None):
    if option == '1':
        # Register Airplane
        if registration_number is None:
            raise HTTPException(status_code=400, detail="Registration number is required for airplane registration.")
        model = input("Enter Model: ")
        flight_type = input("Enter Flight Type (DOM/INT): ")
        source = input("Enter Source: ")
        destination = input("Enter Destination: ")

        airplane = Airplane(
            registration_number=registration_number,
            model=model,
            flight_type=flight_type,
            source=source,
            destination=destination
        )

        airport_controller.register_airplane(airplane)
        return {"message": "Airplane registered successfully"}

    elif option == '2':
        # Log Landing
        if registration_number is None or reason is None or runway_used is None:
            raise HTTPException(status_code=400, detail="Registration number, reason, and runway used are required for landing logging.")

        success = airport_controller.log_landing(registration_number, reason, runway_used)

        if success:
            return {"message": "Landing logged successfully"}
        else:
            raise HTTPException(status_code=404, detail="Airplane not found or landing failed.")

    elif option == '3':
        # Log Departure
        if registration_number is None or gate is None or runway_used is None:
            raise HTTPException(status_code=400, detail="Registration number, gate, and runway used are required for departure logging.")

        airport_controller.log_departure(registration_number, gate, runway_used)
        return {"message": "Departure logged successfully"}

    elif option == '4':
        # List All Objects
        objects = airport_controller.list_all_objects()
        return objects

    elif option == '5':
        # List Single Object
        if registration_number is None:
            raise HTTPException(status_code=400, detail="Registration number is required to list single object.")
        airplane = airport_controller.get_airplane_by_id(registration_number)
        if airplane:
            return airplane
        else:
            raise HTTPException(status_code=404, detail=f"Airplane with registration number {registration_number} not found")

    elif option == '6':
        # Add New Object (Airplane, Landing, or Departure)
        if registration_number is None:
            raise HTTPException(status_code=400, detail="Registration number is required to add new object.")

        if gate is not None:
            # Log Departure
            if runway_used is None:
                raise HTTPException(status_code=400, detail="Runway used is required for departure logging.")
            airport_controller.log_departure(registration_number, gate, runway_used)
            return {"message": "Departure logged successfully"}

        elif reason is not None:
            # Log Landing
            if runway_used is None:
                raise HTTPException(status_code=400, detail="Runway used is required for landing logging.")
            success = airport_controller.log_landing(registration_number, reason, runway_used)
            if success:
                return {"message": "Landing logged successfully"}
            else:
                raise HTTPException(status_code=404, detail="Airplane not found or landing failed.")

        else:
            # Register Airplane
            if model is None or flight_type is None or source is None or destination is None:
                raise HTTPException(status_code=400, detail="Model, flight type, source, and destination are required for airplane registration.")
            airplane = Airplane(
                registration_number=registration_number,
                model=model,
                flight_type=flight_type,
                source=source,
                destination=destination
            )
            airport_controller.register_airplane(airplane)
            return {"message": "Airplane registered successfully"}

    elif option == '7':
        # Delete Object
        if registration_number is None:
            raise HTTPException(status_code=400, detail="Registration number is required to delete object.")
        if airport_controller.delete_object('airplanes', registration_number):
            return {"message": f"Airplane with registration number {registration_number} deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail=f"Airplane with registration number {registration_number} not found")

    else:
        raise HTTPException(status_code=400, detail="Invalid option! Try again.")

app.include_router(router)
