import speech_recognition as sr
import pyautogui
import pyttsx3
import time
import webbrowser
import requests
import os
import google.generativeai as genai
import subprocess
from Backend.TextToSpeech import TextToSpeech
from Backend.SpeechToText import SpeechRecognition
from dotenv import load_dotenv
from Backend.ImageGeneration import gen_image
from groq import Groq



api_key = os.environ.get("GroqAPIKey")  # Ensure this environment variable exists

# Initialize the Groq client using the API key
client = Groq(api_key=api_key)

Username = "Dhruv Bishnoi"
Assistantname = "Jarvis"

# Define the system message for the chatbot
System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which also has real-time up-to-date information from the internet.
*** Do not tell time until I ask, do not talk too much, just answer the question.***
*** Reply in only English, even if the question is in Hindi, reply in English.***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
"""

# Ensure the model you're using is correct and supported






def call_groq(command):
    try:
            # Send the query to the Groq API
            chat_completion = client.chat.completions.create(
                messages=[{"role": "system", "content": System}, {"role": "user", "content": command}],
                model="llama-3.3-70b-versatile",  # Ensure this model is available
            )

            # Check if the response contains valid content and print the response
            if chat_completion.choices:
                TextToSpeech(f"{chat_completion.choices[0].message.content}")
            else:
                print("No response received from the Groq API.")
    except Exception as e:
        print(f"Error: {e}")

# Configure Gemini API
# genai.configure(api_key="YOUR_GEMINI_API_KEY")
# model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize the speech engine


def generate_paragraph(prompt):
    """Generate a paragraph using the Groq API."""
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "system", "content": System}, {"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile"
        )
        if chat_completion.choices:
            return chat_completion.choices[0].message.content
        else:
            TextToSpeech("No response received from the Groq API.")
            return None
    except Exception as e:
        TextToSpeech(f"Error while generating text: {e}")
        return None

def save_to_notepad(text):
    """Save generated text to a file and open in Notepad."""
    file_path = "generated_paragraph.txt"
    with open(file_path, "w") as f:
        f.write(text)
    subprocess.run(["notepad", file_path])



newsapi = os.getenv("NEWS_API_KEY")


# Process AI response


# Open website
def open_website(url):
    webbrowser.open(url)
    TextToSpeech(f"Opening {url}.")

# Search Google
def search_query(command):
    search_url = f"https://www.google.com/search?q={command}"
    open_website(search_url)
    TextToSpeech(f"Here are the search results for {command}.")

# Search YouTube Music
def search_youtube_music(song):
    search_url = f"https://music.youtube.com/search?q={song}"
    webbrowser.open(search_url)
    TextToSpeech(f"Searching for {song} on YouTube Music.")
    time.sleep(1)
    pyautogui.click(803, 526)

# Open system apps
def open_system_app(app_name):
    apps = {
        "microsoft store": "ms-windows-store:",
        "notepad": "notepad",
        "calculator": "calc",
        "file explorer": "explorer",
        "settings": "ms-settings:",
        "command prompt": "cmd",
        "task manager": "taskmgr",
        "control panel": "control",
        "paint": "mspaint",
        "wordpad": "write",
        "powerpoint": "powerpnt",
        "excel": "excel",
        "word": "winword",
        "github": r"C:\Users\bishn\Desktop\GitHub.lnk",
        "vs code": os.getenv("VS_CODE_PATH"),
        "chrome": os.getenv("CHROME_PATH"),
        "edge": "msedge",
        "firefox": os.getenv("FIREFOX_PATH"),
        "vlc": os.getenv("VLC_PATH"),
        "spotify": os.getenv("SPOTIFY_PATH"),
    }
    if app_name.lower() in apps:
        subprocess.run(["start", apps[app_name.lower()]], shell=True)
        TextToSpeech(f"Opening .")
    else:
        TextToSpeech(f"Sorry, I don't recognize '{app_name}' as a system app.")

# Get News Headlines
def get_news():
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
    if r.status_code == 200:
        articles = r.json().get('articles', [])
        headlines = [article['title'] for article in articles[:5]]  # Get top 5
        TextToSpeech(f"Here are the top headlines: {', '.join(headlines)}")
    else:
        TextToSpeech("Sorry, I couldn't fetch the news at the moment.")

# Activate Jarvis
def activate_jarvis():
    print("Jarvis is listening...")
    TextToSpeech("Welcome back sir.")

    while True:
        command = SpeechRecognition()

        if command and "friday" in command.lower():
            TextToSpeech("Hello, how can I assist you?")
            print("Listening for task commands...")

            while True:
                command = SpeechRecognition().lower()

                if "open youtube" in command:
                    open_website("https://www.youtube.com")
                elif "open notepad" in command:
                    os.system("notepad")
                elif "open youtube music" in command:
                    open_website("https://music.youtube.com")
                elif "open netflix" in command:
                    open_website("https://www.netflix.com")
                elif command.startswith("play "):
                    search_youtube_music(command.split("play ", 1)[1])
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

                elif  "make " in command:
                    TextToSpeech("genrating image ")
                    gen_image(command)
                elif "open" in command:
                    open_system_app(command.replace("open", "").strip())
                elif "stop talking" in command:
                    TextToSpeech("Stopping as requested.")
                    break
                elif "goodbye" in command:
                    TextToSpeech("Goodbye! See you later.")
                    print("Goodbye! Deactivating Jarvis.")
                    return
                else:
                    call_groq(command)

# Start Jarvis
if __name__ == "__main__":
    activate_jarvis()
