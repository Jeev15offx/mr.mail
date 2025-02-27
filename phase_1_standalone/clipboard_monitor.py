import pyperclip
import time
import firebase_admin
from firebase_admin import credentials, firestore
from email_validator import validate_email, EmailNotValidError

# Initialize Firebase
cred = credentials.Certificate("mr-mailxpert-16b28-firebase-adminsdk-fbsvc-3b01e5afb0.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Function to check if text is a valid email
def is_valid_email(text):
    try:
        validate_email(text)  # Validates email format
        return True
    except EmailNotValidError as e:
        print(f"🚫 Email validation error: {e}")  # Debugging error
        return False

# Function to store email in Firestore
def save_email_to_firebase(email):
    doc_ref = db.collection("emails").document()  # Auto-generate ID
    doc_ref.set({"email": email, "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")})
    print(f" Saved to Firebase: {email}")

# Clipboard monitoring loop
print(" Clipboard Monitor Running... Copy some text!")

last_text = ""
while True:
    copied_text = pyperclip.paste()
    
    if copied_text != last_text:  
        last_text = copied_text
        print(f" Copied Text: {copied_text}")  # Debug print
        
        if is_valid_email(copied_text):
            save_email_to_firebase(copied_text)
        else:
            print(f" Not a valid email: {copied_text}")
    
    time.sleep(2)  # Check every 2 seconds
