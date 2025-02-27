import re

# Load scam-related keywords from the text file
def load_scam_keywords(filename="scam_keywords.txt"):
    try:
        with open(filename, "r") as file:
            keywords = [line.strip().lower() for line in file.readlines()]
        return keywords
    except FileNotFoundError:
        print("Error: Scam keywords file not found!")
        return []

# Function to check if an email contains scam-related words
def check_scam_email(email_text, scam_keywords):
    email_text = email_text.lower()  # Convert email to lowercase
    for keyword in scam_keywords:
        # Using regex to match whole words
        if re.search(r"\b" + re.escape(keyword) + r"\b", email_text):
            return True, keyword  # Scam keyword found
    return False, None  # No scam words found

#  Running the scam detection program
if __name__ == "__main__":
    scam_keywords = load_scam_keywords()

    email_text = input("Paste your email content here:\n")  # Take user input

    is_scam, found_keyword = check_scam_email(email_text, scam_keywords)

    if is_scam:
        print(f" Scam Alert! The email contains a suspicious keyword: '{found_keyword}'")
    else:
        print("This email looks safe.")
