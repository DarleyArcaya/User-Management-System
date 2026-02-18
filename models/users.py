# ---------------------------------------------------------
# Project: User Management App
# Author: Darley Omar Silot Arcaya
# Date: February 2026
# Description: CRUD application with Tkinter and SQLite
# ---------------------------------------------------------
import sqlite3 as sql
import pathlib as pl 
import sys
from tkinter import messagebox

# --- Dynamic Route Configuration ---
# This block is vital to prevent the app from crashing when converted to an .exe file.
if getattr(sys, 'frozen', False):

# If we are running from the .exe file, we look for the folder where the executable is located.
    BASE_DIR = pl.Path(sys.executable).parent
else:
# If we are in development (VS Code), we go up two levels to reach the project root
    BASE_DIR = pl.Path(__file__).resolve().parent.parent

# We define where the database will live: 'db' folder and 'users.db' file
DB_PATH = BASE_DIR / 'db' / 'users.db'

# Magic: If the 'db' folder doesn't exist, we create it automatically on startup
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


class User: # We represent each user as an objcet with these attributes
    def __init__(self, id, name, email, role):
        self.id = id
        self.name = name
        self.email = email
        self.role = role



def create_table():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   role TEXT NOT NULL
        )
''') 
    conn.commit()
    conn.close()


def save_user(name, email, role):
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO users (name, email, role) VALUES (?, ?, ?)''', (name, email, role))
        conn.commit()
    except sql.IntegrityError:
     # If the email already exists (is UNIQUE), we notify the user with an alert
        messagebox.showerror("Error", "Email already exists. Please use a different email.")
    finally:
        conn.close()

def get_all_users():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM users''')
    rows = cursor.fetchall()
    conn.close()


   # We return a list of User objects using tuple unpacking (*)
    return [User(*user) for user in rows]

def delete_user(user_name):
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM users WHERE name = ?''', (user_name,))
    conn.commit()
    conn.close()