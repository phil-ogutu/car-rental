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

def delete_car():
    list_cars()
    id = int(input("Enter car ID:"))
    car = session.get(Car, id)
    if car:
        session.delete(car)
        session.commit()
        print("Car deleted")
    else:
        print("Customer not found")

def update_car():
    id = int(input("Enter car ID to update: "))
    car = session.get(Car, id)
    if car:
        new_name = input("Enter new name: ")
        car.name = new_name
        session.commit()
        print("Car updated.")
    else:
        print("Car not found.")

def list_customers():
    customers = session.query(Customer).all()
    print("Customers:")
    for customer in customers:
        print(f"ID: {customer.id} | Name: {customer.name}")
    print()

def delete_customer():
    list_customers()
    id = int(input("Enter customer ID:"))
    customer = session.get(Customer, id)
    if customer:
        session.delete(customer)
        session.commit()
        print("Customer deleted")
    else:
        print("Customer not found")

def update_customer():
    id = int(input("Enter customer ID to update: "))
    customer = session.get(Customer, id)
    if customer:
        new_name = input("Enter new name: ")
        customer.name = new_name
        session.commit()
        print("Car updated.")
    else:
        print("Car not found.")

def rent_car():
    list_customers()
    customer_id = int(input("Select customer by ID: "))
    list_cars(available=True)
    car_id = int(input("Select car by ID:"))
    start_date = datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d").date()
    end_date = datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d").date()

    car = session.get(Car, car_id)
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

def car_management():
    while True:
        print("Car Management")
        print("1. Add Car")
        print("2. Update Car")
        print("3. Delete Car")
        print("4. List Cars")
        print("0. Back to Main Menu")

        choice = input("Choose an option:")
        if choice == '1':
            add_car()
        if choice == '2':
            update_car()
        if choice == '3':
            delete_car()
        if choice == '4':
            list_cars()
        if choice == '0':
            break

def customer_management():
    while True:
        print("Customer Management")
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. List Customers")
        print("0. Back to Main Menu")

        choice = input("Choose an option:")
        if choice == '1':
            add_customer()
        if choice == '2':
            update_customer()
        if choice == '3':
            delete_customer()
        if choice == '4':
            list_customers()
        if choice == '0':
            break

def main():
    while True:
        print("Welcome to the Car Rental System")
        print("1. Car Management")
        print("2. Customer Management")
        print("3. Rent a Car")
        print("4. List Rented Cars")
        print("0. Exit")
        choice = input("Choose an option: ")


        if choice == '1':
            car_management()
        if choice == '2':
            customer_management()
        if choice == '3':
            rent_car()
        if choice == '4':
            list_rentals()
        if choice == '0':
            print("Goodbye")
            break

if __name__ == "__main__":
    main()
