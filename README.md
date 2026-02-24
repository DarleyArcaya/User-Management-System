# 👤 User Management App
This project is a desktop application designed to efficiently manage user records. It implements a modular architecture that separates the graphical interface, business logic, and data persistence, ensuring clean and scalable code.

**>>⚠️ Important Note:** The current Flet-based version (**v2.2.3**) is located in the `feature/v2.2.3-flet-migration` branch. The legacy Tkinter version remains in the `main` branch.

## 🛠️ How it is built
The application uses a layered workflow to ensure that each part of the code has a single responsibility:

* -User Interface (GUI): Rebuilt with Flet (Flutter-based framework) to provide a modern, responsive, and cross-platform experience.

* -Data Management: Uses SQLite3 as a relational database engine, allowing information to be retained even after closing the app.

* -Validation and Security: A Regular Expressions (Regex) engine is integrated to ensure that email addresses have a valid format before being processed.

* -Normalization: Includes automatic processes to clean the text (removing spaces and converting to lowercase), preventing errors due to duplication or spelling differences.

## 📂 Repository Structure
-main.py: The entry point that sets up the database and launches the application.

-models/: Contains the database logic and the definition of the User object.

-gui/: Houses the main window configuration and button events.

-utils/: Support functions for email validation and text cleaning.

-db/: Folder where the persistent database file is stored.

## 🚀 Installation and Setup
1. **Clone the repository:**
   `git clone https://github.com/YourUser/User-Management-System.git`
2. **Install dependencies:**
   `pip install -r requirements.txt`
3. **Run the application:**
   `python main.py`

## ✅ Main Features
* Error Prevention: Alert messages if you try to save empty fields or invalid emails.

* Smart Database: Prevents duplicate emails thanks to SQL technical constraints.

* Clean Code: Organized structure that makes it easier to add new features in the future.

## 🗄️ Database Management
The application is completely self-contained:

* **Automatic Creation:** When the program is opened, the `db/` folder and the `users.db` file are created automatically.

* **Portability:** The database always accompanies the executable in the same folder.

## 👨‍💻 Authorship and License
* **Developer:** Darley Omar Silot Arcaya
* **License:** MIT (see LICENSE file)
* **Resources:** Custom icons included in the `resources/` folder.

## 🛠️ Developer Requirements
If you clone the code, make sure to keep the `resources/` folder with the `app_icon.ico` file so that the project compiles correctly.


## 📦 Download Executable (Windows - Android)
If you just want to use the application without installing Python or running any code, you can download the standalone version here:

* [**Download UserManagementApp.exe**](https://github.com/DarleyArcaya/User-Management-System/releases/download/v2.2.3/UserManagementApp.V2.2.3.exe) 
* [**Download UserManagementApp.apk**](https://github.com/DarleyArcaya/User-Management-System/releases/download/v2.2.3/UserManagementApp.V2.2.3.apk)
> **Note:** Some browsers or antiviruses may flag the file as "unrecognized" because it is a custom-built executable. You can safely run it by clicking "More info" -> "Run anyway"