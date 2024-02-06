from controllers.airport_controller import AirportController
from ui.airport_cli import AirportCLI

if __name__ == "__main__":
    from controllers import AirportController
    airport_controller = AirportController()
    airport_cli = AirportCLI(airport_controller)
    airport_cli.run()
    
    