# ---------------------------------------------------------
# Project: User Management App
# Author: Darley Omar Silot Arcaya
# Date: February 2026
# Description: CRUD application with Tkinter and SQLite
# ---------------------------------------------------------
import tkinter as tk
import os
import sys
from models.users import save_user, get_all_users, delete_user
from tkinter import messagebox
from utils.helpers import is_valid_email, normalize_text

def resource_path(relative_path):

    # This feature is a lifesaver. When PyInstaller packages everything into an .exe, files like the icon are extracted 
    # to a temporary folder (_MEIPASS). Without this, 
    # the app wouldn't find the icon and would crash.
    # We use library os and sys here. 
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

def main():
    # Main window settings
    root = tk.Tk()
    root.title("User Management App")
    root.geometry("450x600")

    # Color palette so it doesn't look like a Windows 95 program
    background_color = "#F5F6F7"
    root.configure(bg=background_color)
    fg_color = "#2C3E50"
    entry_bg_color = "white"

    # We tried to load the icon we retrieved from the resources folder
    rute_icono = resource_path("resources/app_icon.ico")

    if os.path.exists(rute_icono):
        root.iconbitmap(rute_icono)
    else:
    
    # If for some reason it's not there, we print to the console but we don't let the app crash
        print("Icon file not found. Using default icon.")

    # --- Interface Elements (Labels and Inputs) ---
    text = tk.Label(root, text="Welcome to your User Management App", font=("Arial", 14, "bold"), bg=background_color, fg=fg_color)
    text.pack(pady=20)

    # Text field settings (Name, Email, Role)
    text_name = tk.Label(root, text="User Name", font=("Arial",  12, "bold"), bg=background_color)
    text_name.pack(pady=5)

    write_name = tk.Entry(root, width=30, bg=entry_bg_color, fg="black", relief="sunken", font=("Arial", 10, "bold"))
    write_name.pack(pady=1)

    text_email = tk.Label(root, text="User Email", font=("Arial",  12, "bold"), bg=background_color)
    text_email.pack(pady=5)

    write_email = tk.Entry(root, width=30, bg=entry_bg_color, fg="black", relief="sunken", font=("Arial", 10, "bold"))
    write_email.pack(pady=1)

    text_role = tk.Label(root, text="User Role", font=("Arial",  12, "bold"), bg=background_color)
    text_role.pack(pady=5)

    write_role = tk.Entry(root, width=30, bg=entry_bg_color, fg="black", relief="sunken", font=("Arial", 10, "bold"))
    write_role.pack(pady=1)


    # Section for deleting users
    text_delete = tk.Label(root, text="Enter ID of user to delete", font=("Arial",  12, "bold"), bg=background_color)
    text_delete.pack(pady=(30, 5))

    write_delete = tk.Entry(root, width=30, bg=entry_bg_color, fg="black", relief="sunken", font=("Arial", 10, "bold"))
    write_delete.pack(pady=1)

    # --- Button Functions ---
    def save():
        name = normalize_text(write_name.get())
        email = normalize_text(write_email.get())
        role = normalize_text(write_role.get())

        # Basic validation: We don't allow misspelled emails
        if not is_valid_email(email):
            messagebox.showerror("Error", "Invalid email format!")
            return

        save_user(name, email, role) # This call the function from the model to save the user in the database

        # We clear the fields after saving for user convenience
        write_name.delete(0, tk.END)
        write_email.delete(0, tk.END)
        write_role.delete(0, tk.END)

        messagebox.showinfo("Success", "User saved successfully!")
        show_users() # We automatically update the view after saving a new user

    
    save_button = tk.Button(root, text="Save User", command=save, bg="#2ECC71", fg="white", font=("Arial", 10, "bold"), width=15, relief="flat")
    save_button.pack(pady=(20, 5))

    def show_users():

        #Retrieves all users from the database and displays them in a popup
        users = get_all_users()
        users_lists = "\n".join([f"{u.name} - {u.email} - {u.role}" for u in users])

        if not users_lists:
            messagebox.showinfo("No users found", "The database is currently empty.")
        else:
            messagebox.showinfo("All Users", users_lists)

    # Show Button (Blue)
    show_button = tk.Button(root, text="Show Users", command=show_users, bg="#3498DB", fg="white", font=("Arial", 10, "bold"), width=15, relief="flat")
    show_button.pack(pady=(20, 5))

    def delete_users():

        #Deletes the user by name. If the name field is empty, displays a warning
        user_name = normalize_text(write_delete.get())
        if not user_name:
            messagebox.showerror("Error", "Please enter a user name to delete.")
            return
        else:
            delete_user(user_name)
            write_delete.delete(0, tk.END)
            messagebox.showinfo("Success", f"User {user_name} deleted successfully!")
            
    # Delete button (Red to warn of danger)
    delete_button = tk.Button(root, text="Delete User", command=delete_users, bg="#E74C3C", fg="white", font=("Arial", 10, "bold"), width=15, relief="flat")
    delete_button.pack(pady=(20, 5))

    def show_about():

        #The personal touch: Authorship and watermark
        messagebox.showinfo("About", 
                            "User Management App v1.0\n\n"
                            "Originally developed by: Darley Omar Silot Arcaya\n"
                            "© 2026 - Original Work")
        
    # About Button (Purple) - Located in the corner so as not to obstruct 
    show_about_button = tk.Button(root, text="About", command=show_about, bg="#9B59B6", fg="white", font=("Arial", 10, "bold"), width=15, relief="flat")
    show_about_button.place(relx=0.0, rely=1.0, x=10, y=-10, anchor="sw")


    root.mainloop()