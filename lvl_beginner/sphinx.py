class Vehicle:
    def stop_engine():
        pass
    def run_engine():
        pass

class Car(Vehicle):
    def stop_engine() -> str:
        return "Car is stopped"
    def run_engine() -> str:
        return "Car is running"


         