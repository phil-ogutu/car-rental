from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

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

def list_cars(available=False):
    if available:
        cars = session.query(Car).filter_by(available=True).all()
        print("Cars available for rent:")
    else:
        cars = session.query(Car).all()
        print("All Cars")
    for car in cars:
        print(f"{car.id} | {car.make} {car.model} _______ Hire Price: {car.price_per_day}/day")
    print()

def list_customers():
    customers = session.query(Customer).all()
    print("Customers:")
    for customer in customers:
        print(f"ID: {customer.id} | Name: {customer.name}")
    print()

def rent_car():
    list_customers()
    customer_id = int(input("Select customer by ID: "))
    list_cars(available=True)
    car_id = int(input("Select car by ID:"))
    start_date = datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d").date()
    end_date = datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d").date()

    car = session.query(Car).get(car_id)
    if not car or not car.available:
        print("Car not available")
        return
    
    rental = Rental(customer_id=customer_id, car_id=car_id, start_date=start_date, end_date=end_date, status="Cofirmed")
    session.add(rental)
    car.available = False
    session.commit()

def list_rentals():
    rentals = session.query(Rental).all()
    print("Rentals:")
    for rental in rentals:
        print(f"Rental ID: {rental.id} | Customer: {rental.customer.name} | Car: {rental.car.make} {rental.car.model} | "
              f"{rental.start_date.date()} to {rental.end_date.date()} Status: {rental.status}")
    print()


def main():
    while True:
        print("Welcome to the Car Rental System")
        print("1. Add a new customer")
        print("2. Add a new car")
        print("3. List Cars")
        print("4. List Customers")
        print("5. Rent a Car")
        print("6. List Rented Cars")
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
        if choice == '5':
            rent_car()
        if choice == '6':
            list_rentals()
        if choice == '0':
            print("Goodbye")
            break

if __name__ == "__main__":
    main()
