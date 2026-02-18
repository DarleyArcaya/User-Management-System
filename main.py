# ---------------------------------------------------------
# Project: User Management App
# Author: Darley Omar Silot Arcaya
# Date: February 2026
# Description: CRUD application with Tkinter and SQLite
# ---------------------------------------------------------
from models.users import create_table
from gui.main_window import main

# This is the official entry point to our application and the only file that should be executed directly.
if __name__ == "__main__":

    # First: We prepare the ground.
    # Before displaying the interface, we ensure that the database
    # and tables exist. If they are already created, it does nothing.
    create_table()

    # Second: We start the graphical interface (Main).
    # Once the database is ready, we call the main GUI loop.
    main()