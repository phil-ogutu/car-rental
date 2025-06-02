# Car Rental System (CLI) 🚗

This is a simple Car Rental System built with Python, SQLAlchemy, and SQLite. The system allows you to manage customers, cars, and rental transactions from a terminal interface.

---

## Features ✨

✅ Add and manage customers  
✅ Add and manage cars  
✅ View available cars for rent  
✅ Create rentals 
✅ View all rentals  
✅ View rentals by customer  

---

## Technologies Used 🛠️

- **Python 3.8+**
- **SQLAlchemy ORM**
- **SQLite** 

---

## Setup Instructions 🚀

### 1️⃣ Clone the repository

```bash
git clone https://github.com/phil-ogutu/car-rental.git
cd car-rental
```

### 2️⃣ Create and run the virtual environment
```bash
pipenv install
pipenv shell
```

### 3️⃣ Run the application
```bash
python lib/main.py
```

## Example Usage 📖
```plaintext
Welcome to the Car Rental System
1. Add a new customer
2. Add a new car
3. View all cars
4. View available cars
5. Create a rental
6. View all rentals
7. View rentals by customer
0. Exit
Choose an option:
```

## File Structure 📂
```
└── 📁car-rental
    └── 📁lib
        └── main.py
        └── models.py
    └── car_rental.db
    └── Pipfile
    └── Pipfile.lock
    └── README.md
```

