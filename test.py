import speech_recognition as sr
import pyautogui
import pyttsx3
import time
import webbrowser
import requests
import os
import google.generativeai as genai
import subprocess
import threading
from Backend.TextToSpeech import TextToSpeech
from Backend.SpeechToText import SpeechRecognition
from dotenv import load_dotenv
from Backend.ImageGeneration import gen_image
from groq import Groq
from pywhatkit import search, playonyt
from AppOpener import close, open as appopen, give_appnames
from dotenv import dotenv_values
import keyboard
from Backend.Chatbot import ChatBot
import asyncio
import difflib
# from Frontend.GUI import GraphicalUserInterface

import gspread
from oauth2client.service_account import ServiceAccountCredentials





def send_whatsapp_message_by_name(contact_name, message):
    """
    Sends a WhatsApp message to a saved contact name using pywhatkit.
    :param contact_name: Name of the contact as saved in your phone (e.g., "John Doe")
    :param message: The message to send
    """
    try:
        # Open WhatsApp using AppOpener
        appopen("whatsapp")
        time.sleep(3)
        # pyautogui.hotkey("win", "up")
        
        # Click on the Search icon in WhatsApp
        pyautogui.hotkey("ctrl", "f")  # This works for web WhatsApp
        time.sleep(1)
        # Type the contact name and press Enter
        pyautogui.write(contact_name)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        
        pyautogui.click(291,220)
        time.sleep(2)
        # Type the message and send it
        pyautogui.write(message)
        time.sleep(1)
        pyautogui.press("enter")
        print(f"Message sent to {contact_name}!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
# def massage_prompt(command):
#     contact_name = input("Enter the contact name as saved in your phone: ")
#     message = input("Enter the message you want to send: ")
#     send_whatsapp_message_by_name(contact_name, message)
    




def split_prompt(prompt):
    # Convert the prompt to lowercase to handle case insensitivity
    prompt = prompt.lower()
    
    # Check if the prompt follows the expected pattern
    if "send a message to" in prompt and "that" in prompt:
        # Split the prompt to get name and message
        name = prompt.split("send a message to")[1].split("that")[0].strip()

        message = prompt.split("that")[1].strip()
        return(name,message)
    else:
        return None, "Invalid prompt format"

# Example input

def whats_msg(command):
    massage_ai = "i will give to prompt and send a  friendly keep massage short as it can , do not give discription"
    new_msg=ChatBot(f"{command}{massage_ai}")
    return new_msg



# # Google Sheets API setup
# SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# SERVICE_ACCOUNT_FILE = "service_account.json"  # Ensure this file exists in the same directory

# # Authenticate and connect to Google Sheets
# creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)
# client = gspread.authorize(creds)

# # Open the Google Sheet by ID instead of URL (more reliable)
# SPREADSHEET_ID = "1le6lB88dVifxDBmgZ0lXSADvQlCl4kcs5-ZbPv-qjWU"  # Extracted from your URL
# sheet = client.open_by_key(SPREADSHEET_ID).sheet1  # Access the first sheet

# # Function to add a new entry
# def add_entry(first_name, last_name, company_name, email, phone):
#     row = [first_name, last_name, company_name, email, phone]
#     sheet.append_row(row)
#     print(f"Added: {row}")

# # Function to get input via voice
# def get_voice_input(prompt):
#     TextToSpeech(prompt)
#     return SpeechRecognition()

# # Function to interactively fill and add data
# def spread_sheet():
#     first_name = get_voice_input("Enter first name")
#     last_name = get_voice_input("Enter last name")
#     company_name = get_voice_input("Enter company name")
#     email = get_voice_input("Enter Email")
#     phone = get_voice_input("Enter phone number")

#     add_entry(first_name, last_name, company_name, email, phone)
#     print("Data added successfully!")

# # Main program execution

 




# Load API keys from .env
load_dotenv()
api_key = os.getenv("GroqAPIKey")
newsapi = os.getenv("NEWS_API_KEY")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize AI models
client = Groq(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

Username = "Dhruv Bishnoi"
Assistantname = "friday"

System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which also has real-time up-to-date information from the internet.
*** Do not tell time until I ask, do not talk too much, just answer the question.***
*** Reply in only English, even if the question is in Hindi, reply in English.***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
"""


mute_prompt = ["mute","Mute", "mute the system"]
unmute_prompt=["unmute","Unmute", "un mute", "Un mute","unmute the system"]
volume_up =["volume up","increase the volume","increase volume"]
volume_down =["volume down","decrease the volume","decrease volume"]



exit_commands = [
    "exit",
    "quit",
    "shutdown",
    "close",
    "terminate",
    "turn off",
    "deactivate",
    "log off",
    "power down",
    "disconnect",
    "I'm done",
    "leave",
    "abort",
    "halt",
    "sign out"
]

good_bye = [
        "see you later",
        "stop",

         "goodbye",

         "good bye",

        "end session",

         "bye",


      
]


def call_groq(command):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "system", "content": System}, {"role": "user", "content": command}],
            model="llama-3.3-70b-versatile",
        )
        if chat_completion.choices:
            TextToSpeech(chat_completion.choices[0].message.content)
    except Exception as e:
        print(f"Error: {e}")

def generate_paragraph(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "system", "content": System}, {"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile"
        )
        return chat_completion.choices[0].message.content if chat_completion.choices else None
    except Exception as e:
        return None

def save_to_notepad(text):
    file_path = "generated_paragraph.txt"
    with open(file_path, "w") as f:
        f.write(text)
    subprocess.run(["notepad", file_path])

def CloseApp(app):
    try:
        app = app.strip()  # Ensure it's a clean string
        close(app, match_closest=True, output=True, throw_error=False)  # Avoid breaking execution
        TextToSpeech(f"Closing {app}.")
        return True
    except Exception as e:
        print(f"Error: Could not close '{app}'. {e}")
        TextToSpeech(f"Sorry, I couldn't close {app}.")
        return False
    


# def mute():
#     keyboard.press_and_release("volume mute")

# def unmute():
#     keyboard.press_and_release("volume mute")  # Same as mute

# def volume_up():
#     for _ in range(50):  # Press "volume down" 50 times
#         keyboard.press_and_release("volume up")
#         time.sleep(0.05)
# def volume_down():
#     for _ in range(50):  # Press "volume down" 50 times
#         keyboard.press_and_release("volume down")
#         time.sleep(0.05)
  # Small delay to prevent system overload

# def System(command):
#     actions = {
#         "mute": mute,
#         "unmute": unmute,
#         "volume_up": volume_up,
#         "volume_down": volume_down,
#     }

#     if command in actions:
#         try:
#             actions[command]()  # Call the corresponding function
#             print(f"Executed: {command}")
#         except Exception as e:
#             print(f"Error executing {command}: {e}")
#     else:
#         print("Invalid command")
def aiProcess(command):
    response = ChatBot(command)
    TextToSpeech(response)


def open_website(url):
    webbrowser.open(url)
    TextToSpeech(f"Opening.")

def search_query(command):
    search_url = f"https://www.google.com/search?q={command}"
    open_website(search_url)

def search_youtube_music(song):
    search_url = f"https://music.youtube.com/search?q={song}"
    webbrowser.open(search_url)
    TextToSpeech(f"Searching for {song} on YouTube Music.")
    time.sleep(1)
    pyautogui.click(803, 526)

def open_system_app(app_name):
    apps = {"notepad": "notepad", "calculator": "calc", "cmd": "cmd", "spotify": os.getenv("SPOTIFY_PATH")}
    if app_name.lower() in apps:
        subprocess.run(["start", apps[app_name.lower()]], shell=True)
        TextToSpeech(f"Opening {app_name}.")

def get_news():
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
    if r.status_code == 200:
        articles = r.json().get('articles', [])
        headlines = [article['title'] for article in articles[:5]]
        TextToSpeech(f"Here are the top headlines: {', '.join(headlines)}")

def generate_image_async(command):
    def generate():
        TextToSpeech(" plese wait sir , image  is Generating.")
        gen_image(command)
        TextToSpeech("Image generation complete.")
    
    image_thread = threading.Thread(target=generate)
    image_thread.start()

def PlayYoutube(query):
    playonyt(query)
    return True



msg_send_prompt=[
"send a message to"
"send a message"
"send message"

]


spread_s_promt = [
    "open spreadsheet",
    "start spreadsheet",
    "launch spreadsheet",
    "access spreadsheet",
    "activate spreadsheet",
    "initiate spreadsheet",
    "spreadsheet open",
    "spreadsheet start",
    "spreadsheet launch",
    "spreadsheet access",
    "spreadsheet activate",
    "spreadsheet initiate",
    "open google sheet",
    "start google sheet",
    "launch google sheet",
    "access google sheet",
    "activate google sheet",
    "initiate google sheet",
    "open sheet",
    "start sheet",
    "launch sheet",
    "access sheet",
    "activate sheet",
    "initiate sheet",
    "let's work on spreadsheet",
    "work on spreadsheet",
    "work on google sheet",
    "let's work on google sheet",
    "add some data in sheet",
    "update data in spreadsheet",
    "add data to google sheet",
    "update sheet",
    "fill the spreadsheet",
    "fill google sheet",
    "edit spreadsheet",
    "edit google sheet",
    "start data entry",
    "begin data entry in sheet",
    "let's update the spreadsheet",
    "update google sheet",
    "modify spreadsheet",
    "modify google sheet",
    "record data in spreadsheet",
    "record data in google sheet",
    "input data in sheet",
    "input data in google sheet",
    "hey, open the spreadsheet",
    "can you open the sheet?",
    "let's add some stuff to the sheet",
    "let's update the sheet",
    "let's organize some data",
    "I need to add something to the sheet",
    "let's put some data in the spreadsheet",
    "let's get to work on the sheet",
    "can you help me with the spreadsheet?",
    "let's do some data entry",
    "I want to update the sheet",
    "help me with the spreadsheet",
    "let's edit the google sheet",
    "let's manage some data",
    "time to update the sheet",
    "let's get to work on the spreadsheet",
    "I need to enter some data",
    "let's sort out the spreadsheet"
]



def activate_jarvis():
    print("friday is listening...")
    TextToSpeech("Welcome back sir.")
    funcs =[]

    while True:
        command = SpeechRecognition()
        if command and "friday" in command.lower():
            TextToSpeech("Hello, how can I assist you?")
            print("Listening for task commands...")

            while True:
                command = SpeechRecognition().lower()

                # if command.startswith("open "):
                #     fun = asyncio.to_(OpenApp, command.removeprefix("open "))
                #     funcs.append(fun)
                # elif command.startswith("play "):
                #     fun = asyncio.to_thread(PlayYoutube, command.removeprefix("play "))
                #     funcs.append(fun)
                # elif command.startswith("close "):
                #     fun = asyncio.to_thread(CloseApp, command.removeprefix("close "))
                #     funcs.append(fun)
            
                if "open youtube" in command:
                    
                    open_website("https://www.youtube.com")

                # elif difflib.get_close_matches(command,spread_s_promt,cutoff=0.8):
                #                             spread_sheet()


                elif(difflib.get_close_matches(command, mute_prompt, cutoff=1) ):
                                            keyboard.press_and_release("volume mute")


                elif(difflib.get_close_matches(command,volume_up ,cutoff=0.9)):
                                    for _ in range(25):  # Press "volume down" 50 times
                                        keyboard.press_and_release("volume up")
                                        time.sleep(0.05)
                elif(difflib.get_close_matches(command,volume_down, cutoff=0.9)):
                                for _ in range(25):  # Press "volume down" 50 times
                                        keyboard.press_and_release("volume down")
                                        time.sleep(0.05)
                elif difflib.get_close_matches(command, unmute_prompt, cutoff=1):
                                            keyboard.press_and_release("volume mute")  
                elif difflib.get_close_matches(command,msg_send_prompt, cutoff=0.8):
                      
                    name, message = split_prompt(command)
                    new_msg=whats_msg(command)
                    send_whatsapp_message_by_name(name,new_msg)

                elif "open notepad" in command:
                    open_system_app("notepad")


                elif "play" in command:
                    yt_play=(command.replace("play", "").strip())
                    PlayYoutube(yt_play)


                elif "open whatsapp" in command:
                    open_website("https://web.whatsapp.com")


                elif "search for" in command:
                    search_query(command.replace("search for", "").strip())


                elif "news" in command:
                    get_news()


                elif "write" in command:
                    TextToSpeech("Generating text...")
                    generated_text = generate_paragraph(command)
                    if generated_text:
                        save_to_notepad(generated_text)
                elif "make" in command:
                    generate_image_async(command)
                elif "open" in command:
                    open_system_app(command.replace("open", "").strip())
                elif "stop talking" in command:
                    TextToSpeech("Stopping as requested.")
                    break
                elif "close" in command:
                    app_name = command.replace("close", "").strip()  # Extract the app name
                    CloseApp(app_name)
                    TextToSpeech("Goodbye! See you later.")
                    print("Goodbye! Deactivating friday.")
                    return
                elif difflib.get_close_matches(command,exit_commands,cutoff=0.9):
                      
                      TextToSpeech("see you later")
                      print("Deactivating friday.....")
                      return

                elif difflib.get_close_matches(command,good_bye,cutoff=0.9):
                      TextToSpeech("see you later....")
                      print("friday is listening...")
                      break
                
                elif "screenshot" in command:
                            screenshot = pyautogui.screenshot()            
                            screenshot.save("screenshot.png")
                
                elif "pose" in command:
                      keyboard.press_and_release("space")
                      
                elif "resume" in command:
                      keyboard.press_and_release("space")

                
                else:
                    aiProcess(command)

if __name__ == "__main__":
    activate_jarvis()
