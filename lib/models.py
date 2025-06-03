from sqlalchemy import (Column, Integer, String, DateTime, Boolean, ForeignKey)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    rentals = relationship("Rental", back_populates="customer")

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer(), primary_key=True)
    make = Column(String())
    model = Column(String())
    price_per_day = Column(Integer())
    available = Column(Boolean, default=True)

    rentals = relationship("Rental", back_populates="car")


class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    car_id = Column(Integer, ForeignKey("cars.id"))
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    customer = relationship("Customer", back_populates="rentals")
    car = relationship("Car", back_populates="rentals")

