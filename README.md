# MySQL-Database-Tkinter
A Python desktop application implementing user registration and authentication through a Tkinter-based GUI, integrated with a MySQL database backend.

# Tkinter User Registration & Login App

A simple Python desktop application with a clean Tkinter GUI for user registration and login. User data is securely stored in a MySQL database.

---

## Features

- Register new users with details like name, email, password, gender, age, and address.
- Login with email and password.
- Basic input validation and unique email enforcement.
- Easy-to-understand GUI built with Tkinter.
- MySQL database integration for persistent user data.

---

## Getting Started

### Prerequisites

- Python 3.x
- MySQL server installed and running
- `pymysql` Python package

### Installation

1. Clone this repository:
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
2. Install required Python packages: pip install pymysql
3. Configure your MySQL connection settings in database.py (or wherever your connection is initialized):
     conn = pymysql.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    autocommit=True
    )  
4. Run the application:
   python UI.py

### Usage
When you start the app, you’ll see options to Login or Register.

Register a new account by filling in the details.

Login using your email and password.

After login, you’ll see the main window where you can expand functionality.

### Future Improvements
Add password hashing for better security.

Input validation and error handling.

User profile management.

Additional GUI features and navigation.


### Contact
Created by ravarnax3.14 — feel free to reach out!
