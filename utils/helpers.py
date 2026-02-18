import re
from tkinter import messagebox

def is_valid_email(email):
# We don't want junk in our database. This function uses a 'Regular Expression'
# (Regex) to verify that the email has a real structure (something@domain.com).


    # The pattern looks for: letters/numbers + @ + domain + extension of at least 2 letters
    pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'

    # We use .strip() in case the user accidentally left a space at the end
    return re.match(pattern, email.strip()) is not None

def normalize_text(text):
    #To ensure searches and deletions always work correctly,
    #we clean the text: we remove extra spaces and convert it to lowercase.
    #This way, 'User' and 'user' will be treated as the same user.
    return text.strip().lower()
