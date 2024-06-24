def hi():
    """Hey this is documentation"""
    print("hello")

class Car:
    """this is car class"""
    def run_engine():
        """this is the method inside car class"""
        print("rum..rum...")

if __name__ == "__main__":
    print(hi.__doc__)
    help(hi)
    
    help(Car)
    help(Car.run_engine)