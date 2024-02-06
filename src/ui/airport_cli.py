from controllers.airport_controller import AirportController
from models.airplane import Airplane
from datetime import datetime

class AirportCLI:
    def __init__(self, airport_controller: AirportController):
        self.airport_controller = airport_controller


    def menu(self):
        print("\nAirport Monitoring System")
        print("1. Register Airplane")
        print("2. Log Landing")
        print("3. Log Departure")
        print("4. List All Objects")
        print("5. List Single Object")
        print("6. Add New Object")
        print("7. Delete Object")
        print("x. Exit")

    def register_airplane(self):
        registration_number = input("Enter Registration Number: ")
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

        self.airport_controller.register_airplane(airplane)
        print("Airplane registered successfully!")

    def log_landing(self):
        registration_number = input("Enter Registration Number: ")
        reason = input("Enter Landing Reason: ")
        runway_used = int(input("Enter Runway Used: "))

        success = self.airport_controller.log_landing(registration_number, reason, runway_used)

        if success:
            print("Landing logged successfully!")
        else:
            print("Airplane not found or landing failed.")

    def log_departure(self):
        registration_number = input("Enter Registration Number: ")
        gate = int(input("Enter Gate: "))
        runway_used = int(input("Enter Runway Used: "))

        self.airport_controller.log_departure(registration_number, gate, runway_used)
        print("Departure logged successfully!")

    def list_all_objects(self):
        objects = self.airport_controller.list_all_objects()

        print("List of Airplanes:")
        for airplane in objects['airplanes']:
            print(airplane)

        print("\nList of Landings:")
        for landing in objects['landings']:
            print(landing)

        print("\nList of Departures:")
        for departure in objects['departures']:
            print(departure)

    def list_single_object(self):
        print("Choose object type:")
        print("1. Airplanes")
        print("2. Landings")
        print("3. Departures")
        option = input("Enter option: ")

        table_name = None
        if option == '1':
            table_name = 'airplanes'
        elif option == '2':
            table_name = 'landings'
        elif option == '3':
            table_name = 'departures'
        else:
            print("Invalid option")
            return

        identification_number = input("Enter Identification Number: ")
        objects = self.airport_controller.list_single_object(table_name, identification_number)

        if objects:
            print(f"List of {table_name.capitalize()}:")
            for obj in objects:
                print(obj)
        else:
            print("Object not found.")
            

    def add_new_object(self):
        option = input("Choose object type (1. Airplane, 2. Landing, 3. Departure): ")
        if option == '1':
            self.register_airplane()
        elif option == '2':
            self.log_landing()
        elif option == '3':
            self.log_departure()
        else:
            print("Invalid option! Try again.")

    def delete_object(self):
        print("Choose object type to delete:")
        print("1. Airplanes")
        print("2. Landings")
        print("3. Departures")
        object_type_option = input("Enter option: ")

        object_type = None
        if object_type_option == '1':
            object_type = 'airplanes'
        elif object_type_option == '2':
            object_type = 'landings'
        elif object_type_option == '3':
            object_type = 'departures'
        else:
            print("Invalid option! Try again.")
            return

        identification_number = input("Enter Identification Number: ")
        if self.airport_controller.delete_object(object_type, identification_number):
            print("Object deleted successfully.")
        else:
            print("Object not found.")

    def run(self):
        while True:
            self.menu()
            option = input("Enter your choice: ")

            if option == '1':
                self.register_airplane()
            elif option == '2':
                self.log_landing()
            elif option == '3':
                self.log_departure()
            elif option == '4':
                self.list_all_objects()
            elif option == '5':
                self.list_single_object()
            elif option == '6':
                self.add_new_object()
            elif option == '7':
                self.delete_object()
            elif option.lower() == 'x':
                break
            else:
                print("Invalid option! Try again.")
