# ---------------------------------------------------------
# Project: User Management App
# Author: Darley Omar Silot Arcaya
# Date: February 2026
# Description: CRUD application with Tkinter and SQLite
# ---------------------------------------------------------
import flet as ft
from models.users import  save_user, get_all_users, delete_user
from utils.helpers import is_valid_email, normalize_text


def main(page: ft.Page):

    # --- UI Configuration ---
    page.title = "User Managment App"
    page.window.width = 470
    page.window.height = 600
    page.window.icon = "app_icon.ico" # Set the app window icon
    
    # --- UI Components ---
    text_welcome = ft.Text(
        "Welcome", 
        size=20,
        color = "lightblue"
        )
    
    # Display area for messages and user lists
    message_showm = ft.TextField(
        label="",
        width=390,
        height=100,
        multiline=True,
        read_only=True
    )

    # Input fields for user data
    user_name = ft.TextField(
        label="User Name",
        width=300,
        height=50
    )
    
    user_email = ft.TextField(
        label="User Email",
        width=300,
        height=50
    )

    user_role = ft.TextField(
        label="User Role",
        width=300,
        height=50
    )

    # Input fields for operations like delete and search
    remove_user = ft.TextField(
        label="Enter Name to Delete User",
        width=150,
        height=50
    )

    # This is the search field where users finds users by name
    search_user = ft.TextField(
        label="Enter Name to Search User",
        width=150,
        height=50
    )

    # Pop up dialog for the "ABOUT"
    pup_up = ft.AlertDialog(
        title=ft.Text("About"),
        content=ft.Text("User Management App v2.2.3\n\n"
                        "Originally developed by: Darley Omar Silot Arcaya\n"
                        "© 2026 - Original Work"),
    )

    page.overlay.append(pup_up) # Required to show the dialog later

    def handle_delete(e): # --- Event to delete users (Functions) ---
        delete_name = normalize_text(remove_user.value)
        
        if not delete_name:
            message_showm.value = "Please enter a name to delete."
            page.update()
            return
        
        try:
            delete_user(delete_name)
        except Exception as err:
            message_showm.value = f"Error deleting user: {err}"
            page.update()
            return


        message_showm.value = f"User '{delete_name}' deleted successfully!"
        show_users(e)
        page.update()
        
        remove_user.value = "" # Clear input
    # Delete Button (Red to warn of danger)
    button_delete = ft.Button(
        "Delete",
        width=100,
        height=50,
        color="red",
        on_click=handle_delete
    )
    

    def save(e):
        # Validate and save a new user to the database
        name = normalize_text(user_name.value)
        email = normalize_text(user_email.value)
        role = normalize_text(user_role.value)

        # Basic validation: We don't allow empty fields
        if not name or not email or not role:
            message_showm.value = "Please fill in all fields."
            page.update()
            return
        
        else: # We also validate the email format to prevent misspelled emails
            if not is_valid_email(email):
                message_showm.value = "Invalid email format!"
                page.update()
                return
        
        try:
            save_user(name, email, role)
            message_showm.value = "User saved successfully!"
        except Exception as err:
            message_showm.value = f"Error saving user: {err}"
        show_users(e) # We automatically update the view after saving a new user
        page.update()

        # Clear input fields after saving for user convenience
        name = user_name.value = ""
        email = user_email.value = ""
        role = user_role.value = ""
    # Save Button (Green)
    button_submit = ft.Button(
        "Submit",
        width=100,
        height=50,
        color="green",
        on_click=save
    )

    def show_users(e):
        # Fetches all users and show them in the text area.
        users = get_all_users()
        users_lists = "\n".join([f"{u.name} - {u.email} - {u.role}" for u in users])
        if not users:
            message_showm.value = "The database is currently empty."
        else:
            message_showm.value = f"All Users:\n{users_lists}"
        page.update()
    # Show Button (Blue)
    button_show_users = ft.Button(
        "Show Users",
        width=100,
        height=50,
        color="blue",
        on_click=show_users
    )

    def search(e):
        # Search for users matching the query for name
        query = normalize_text(search_user.value)
        if not query:
            message_showm.value = "Please enter a search query."
            page.update()
            return
        users = get_all_users()

        #Filtres users by name, email or role matching the search query
        matched_users = [u for u in users if query in u.name or query in u.email or query in u.role]
        if not matched_users:
            message_showm.value = "No users found matching the search query."
        else: # We display the matched users in the text area
            matched_users_lists = "\n".join([f"{u.name} - {u.email} - {u.role}" for u in matched_users])
            message_showm.value = f"Search Results:\n{matched_users_lists}"
            page.update()

        
        search_user.value = "" # Clear search field after searching for user convenience
    # Search Button (Orange)
    button_search_user = ft.Button(
        "Search User",
        width=100,
        height=50,
        color="orange",
        on_click=search
    )

    def show_about(e):
        # Open the "About" pop-up dialog
        pup_up.open = True
        page.update()

    # We create the "About" button and link it to the show_about function to display the pop-up dialog when clicked.
    button_about = ft.Button(
        "About",
        width=100,
        height=50,
        color="purple",
        on_click= show_about
    )

    # --- Layout ---
    # We arrange all the components in the page using containers and rows for better organization and aesthetics
    page.add(
        ft.Container(
            text_welcome,
            alignment=ft.alignment.Alignment.CENTER,
        ),
        ft.Container(
            message_showm,
            alignment=ft.alignment.Alignment.CENTER,
        ),
        ft.Container(
            user_name,
            alignment=ft.alignment.Alignment.CENTER,
        ),
        ft.Container(
            user_email,
            alignment=ft.alignment.Alignment.CENTER,
        ),
        ft.Container(
            user_role,
            alignment=ft.alignment.Alignment.CENTER,
        ),
        ft.Row([ # We group the input fields for delete and search in a row for better layout
            remove_user,
            search_user
            ], alignment=ft.MainAxisAlignment.CENTER # We center the row of input fields for better aesthetics
            
        ),
        ft.Row([ # We group the main action buttons in a row for better layout
            button_submit,
            button_show_users,
            button_search_user,
            button_delete
        ], ft.MainAxisAlignment.CENTER
        ),
        ft.Container( # We place the "About" button separately at the bottom for better visibility
            button_about,
            alignment=ft.alignment.Alignment.CENTER_LEFT # We align the "About" button to the left for better aesthetics
        )
    )