import requests


# Your FastAPI server URL

API_URL = "http://127.0.0.1:8000/save-email/"  



def send_email(content):
    
"""Send email content to FastAPI and get response."""
   
 data = {"content": content} # Email data
 
   response = requests.post(API_URL, json=data)
  # Sending POST request
    
return response.json()  
# Returning API response

# Example usage

if __name__ == "__main__":

    email_content = """Dear Candidate,


    We are pleased to offer you a job at our company. Please send your details to xyz@gmail.com for further processing.


    Regards,

    HR Team
    """

    result = send_email(email_content)  # Sending email content to API
    print(result)  # Output API response