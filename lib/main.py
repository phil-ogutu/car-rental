from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Customer, Car, Rental

engine = create_engine("sqlite:///car_rental.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_customer():
    name = input("Enter customer name: ")
    customer = Customer(name=name)
    session.add(customer)
    session.commit()
    print(f"Customer {name} added.\n")

def add_car():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    price = int(input("Enter rental price per day: "))
    car = Car(make=make, model=model, price_per_day=price)
    session.add(car)
    session.commit()
    print(f"Car {make} {model} added.\n")

def list_cars():
    cars = session.query(Car).all()
    for car in cars:
        print(f"{car.id} | {car.make} {car.model} _______ Hire Price: {car.price_per_day}/day")
    print()

def list_customers():
    customers = session.query(Customer).all()
    print("Customers:")
    for customer in customers:
        print(f"ID: {customer.id} | Name: {customer.name}")
    print()


def main():
    while True:
        print("Welcome to the Car Rental System")
        print("1. Add a new customer")
        print("2. Add a new car")
        print("3. List Cars")
        print("4. List Customers")
        print("0. Exit")
        choice = input("Choose an option: ")


        if choice == '1':
            add_customer()
        if choice == '2':
            add_car()
        if choice == '3':
            list_cars()
        if choice == '4':
            list_customers()
        if choice == '0':
            print("Goodbye")
            break

if __name__ == "__main__":
    main()
