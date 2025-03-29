
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# from Backend.SpeechToText import SpeechRecognition
# from Backend.TextToSpeech import TextToSpeech
# # Google Sheets API setup
# SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# SERVICE_ACCOUNT_FILE = "service_account.json"  # Replace with your JSON key file

# # Authenticate and connect to Google Sheets
# creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)
# client = gspread.authorize(creds)

# # Open the Google Sheet by URL or Name
# SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1le6lB88dVifxDBmgZ0lXSADvQlCl4kcs5-ZbPv-qjWU/edit?usp=sharing"  # Replace with your actual Google Sheet URL
# sheet = client.open_by_url(SPREADSHEET_URL).sheet1  # Access the first sheet

# # Function to add a new entry
# def add_entry(first_name, last_name, company_name, email, phone):
#     row = [first_name, last_name, company_name, email, phone]
#     sheet.append_row(row)
#     print(f"Added: {row}")

# # Example Usage
    
# def spread_sheet(self):
#         TextToSpeech(self)
#         TextToSpeech("enter first name")
#         command = SpeechRecognition()
        
#         first_name = command
#         TextToSpeech("enter last name")
#         command_last=SpeechRecognition()
#         last_name = command_last

#         TextToSpeech("enter comapany name")
#         command_com = SpeechRecognition()
#         company_name = command_com

#         TextToSpeech("enter Email")
#         command_email = SpeechRecognition()
#         email = command_email

#         TextToSpeech("enter phone number")
#         command_num  = SpeechRecognition()
#         phone = command_num

#         add_entry(first_name, last_name, company_name, email, phone)
#         print("Data added successfully!")

 

# if __name__ == "__main__":\
# command = SpeechRecognition()
# if("open" in command):
#         spread_sheet(command)



import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Backend.SpeechToText import SpeechRecognition
from Backend.TextToSpeech import TextToSpeech

# Google Sheets API setup
SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "service_account.json"  # Ensure this file exists in the same directory

# Authenticate and connect to Google Sheets
creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)
client = gspread.authorize(creds)

# Open the Google Sheet by ID instead of URL (more reliable)
SPREADSHEET_ID = "1le6lB88dVifxDBmgZ0lXSADvQlCl4kcs5-ZbPv-qjWU"  # Extracted from your URL
sheet = client.open_by_key(SPREADSHEET_ID).sheet1  # Access the first sheet

# Function to add a new entry
def add_entry(first_name, last_name, company_name, email, phone):
    row = [first_name, last_name, company_name, email, phone]
    sheet.append_row(row)
    print(f"Added: {row}")

# Function to get input via voice
def get_voice_input(prompt):
    TextToSpeech(prompt)
    return SpeechRecognition()

# Function to interactively fill and add data
def spread_sheet():
    first_name = get_voice_input("Enter first name")
    last_name = get_voice_input("Enter last name")
    company_name = get_voice_input("Enter company name")
    email = get_voice_input("Enter Email")
    phone = get_voice_input("Enter phone number")

    add_entry(first_name, last_name, company_name, email, phone)
    print("Data added successfully!")

# Main program execution
if __name__ == "__main__":
    command = SpeechRecognition()
    if "open" in command.lower():
        spread_sheet()
