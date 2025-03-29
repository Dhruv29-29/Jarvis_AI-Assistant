# from AppOpener import close, open as appopen  # Import functions to open and close apps.
# from webbrowser import open as webopen  # Import web browser functionality.
# from pywhatkit import search, playonyt  # Import functions for Google search and YouTube playback.
# from dotenv import dotenv_values  # Import dotenv to manage environment variables.
# from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML content.
# from rich import print  # Import rich for styled console output.
# from groq import Groq  # Import Groq for AI chat functionalities.
# import webbrowser  # Import webbrowser for opening URLs.
# import subprocess  # Import subprocess for interacting with the system.
# import requests  # Import requests for making HTTP requests.
# import keyboard  # Import keyboard for keyboard-related actions.
# import asyncio  # Import asyncio for asynchronous programming.
# import os  # Import os for operating system functionalities.

# # Load environment variables from the .env file.
# env_vars = dotenv_values(".env")
# GroqAPIKey = env_vars.get("GroqAPIKey")  # Fetch Groq API Key from environment variables.

# classes = ['_Zcubw', 'h9k6Lc', 'L1K0o sYJric', 'z0LCw', 'gsrt vk_bk FzvWSb WwPnhf', 'pclqee', 'tw-Data-text tw-text-small tw-ta',
#            'iZ6rdc', 'OSUBfd L1K0o', 'YL7xdc', 'webanswers-webanswers_table__webanswers-table', 'dONo ikb4Bb gsrt', 'sXLAoe',
#            'LWKfkc', 'VQF4g', 'q3wWpe', 'kno-rdesc', 'SPZz6b']

# # Define a user-agent for making web requests.
# useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

# # Initialize the Groq client with the API Key.
# Client = Groq(api_key=GroqAPIKey)

# # Predefined professional responses for user interactions.
# professional_responses = [
#     "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
#     "I'm at your service for any additional questions or support you may need—don't hesitate to ask."
# ]

# # List to store chatbot messages.
# messages = []

# # System message to provide context to the chatbot.
# SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ['Username']}, You're a content writer. You have to write content like a letter."}]

# # Function to perform a Google search.
# def GoogleSearch(Topic):
#     search(Topic)  # Use pywhatkit's search function to perform a Google search.
#     return True 

# def Content(Topic):
# # Automation
#     def OpenNotepad(File):
#         default_text_editor = 'notepad.exe'  # Default text editor.
#         subprocess.Popen([default_text_editor, File])  # Open the file in Notepad.

#     # Nested function to generate content using the AI chatbot.
#     def ContentWriterAI(prompt):
#         messages.append({"role": "user", "content": f"{prompt}"})  # Add the user's prompt to messages.

#         completion = Client.chat.completions.create(
#             model="mixtral-8x7b-32768",  # Specify the AI model.
#             messages=SystemChatBot + messages,  # Include system instructions and chat history.
#             max_tokens=2048,
#             temperature = 0.7,
#             top_p=1, # Use nucleus sampling for response diversity.
#             stream=True, # Enable streaming response.

#             stop=None # Allow the model to determine stopping conditions
#             )

#         Answer = "" # Initialize an empty string for the response.

#         # Process streamed response chunks.
#         for chunk in completion:

#             if chunk.choices[0].delta.content: # Check for content in the current chunk.
#                 Answer += chunk.choices[0].delta.content # Append the content to the answer

#         Answer = Answer.replace("</s>", "") # Remove unwanted tokens from the response.
#         messages.append({"role": "assistant", "content": Answer}) # Add the AI's response to messages
#         return Answer

#     Topic: str = Topic.replace("Content ", "") # Remove "Content " from the topic

#     ContentByAI = ContentWriterAI(Topic) # Generate content using AI.

#     # Save the generated content to a text file
#     # Limit the maximum tokens.
#     with open(rf"Data\\{Topic.lower().replace(' ', '')}.txt", "w", encoding="utf-8") as file:
#         file.write(ContentByAI)  # Write the content to the file.
#         file.close()

#     OpenNotepad(rf"Data\\{Topic.lower().replace(' ', '')}.txt")  # Open the file in Notepad.
#     return True  # Indicate success.

#     # Function to search for a topic on YouTube.
# def YouTubeSearch(Topic):
#     Url4Search = f"https://www.youtube.com/results?search_query={Topic}"  # Construct the YouTube search URL.
#     webbrowser.open(Url4Search)  # Open the search URL in a web browser.
#     return True  # Indicate success.

# def PlayYoutube(query):
#     playonyt(query)
#     return True

# def OpenApp(app, sess=requests.session()):

#     try:
#         appopen(app, match_closest=True, output=True, throw_error=True)  # Attempt to open the app
#         return True  # Indicate success.

#     except:

#         # Nested function to extract links from HTML content.
#         def extract_links(html):
#             if html is None:
#                 return []
#             soup = BeautifulSoup(html, 'html.parser')  # Parse the HTML content.
#             links = soup.find_all('a', {'jsname': 'UWckNb'})  # Find relevant links.
#             return [link.get('href') for link in links]  # Return the links.

        


#         def search_google(query):
#             url = f"https://www.google.com/search?q={query}"  # Construct the Google search URL.
#             headers = {"User-Agent": useragent}  # Use the predefined user-agent.
            
#             response = sess.get(url, headers=headers)  # Perform the GET request.

#             if response.status_code == 200:
#                 return response.text  # Return the HTML content.
#             else:
#                 print("Failed to retrieve search results.")  # Print an error message.
#                 return None

#         html = search_google(app)  # Perform the Google search.

#         if html:
#             link = extract_links(html)[0]  # Extract the first link from the search results.
#             webopen(link)  # Open the link in a web browser.

#         return True  # Indicate success.

#         # Function to close an application.
# def CloseApp(app):
#     if "chrome" in app:
#         pass  # Skip
#     else:
#         try:
#             close(app,match_closest=True,output=True,throw_error=True)
#             return True
#         except:
#             return False
# def System(command):


#     def mute():
#         keyboard.press_and_release("volume mute")

#     def unmute():
#         keyboard.press_and_release("volume mute")

#     def volume_up():
#         keyboard.press_and_release("volume up")

#     def volume_down():
#         keyboard.press_and_release("volume down")

#     if(command==mute):
#         mute()
#     elif(command==unmute):
#         unmute()
#     elif(command==volume_up):
#         volume_up()
#     elif(command==volume_down):
#         volume_down()

#     return True

# async def TranslateAndExecute(commands:list[str]):
#     funcs = []
#     for command in commands:
#         if command.startswith("open"):
#             if "open it" in command:
#                 pass
#             if "open file" == command:
#                 pass

        
#             else:
#                 fun = asyncio.to_thread(OpenApp, command.removeprefix("open "))  # Schedule app opening.
#                 funcs.append(fun)

#         elif command.startswith("general "):  # Placeholder for general commands.
#             pass

#         elif command.startswith("realtime "):  # Placeholder for real-time commands.
#             pass

#         elif command.startswith("close "):  # Handle "close" commands.
#             fun = asyncio.to_thread(CloseApp, command.removeprefix("close "))
#             funcs.append(fun)

#         elif command.startswith("play "):  # Handle "play" commands.
#             fun = asyncio.to_thread(PlayYoutube, command.removeprefix("play "))  # Schedule YouTube playback.
#             funcs.append(fun)

#         elif command.startswith("content "):  # Handle "content" commands.
#             fun = asyncio.to_thread(Content, command.removeprefix("content "))
#             funcs.append(fun)

#         elif command.startswith("google search "):  # Handle Google search commands.
#             fun = asyncio.to_thread(GoogleSearch, command.removeprefix("google search "))  # Schedule Google search.
#             funcs.append(fun)

#         elif command.startswith("youtube search "):  # Handle YouTube search commands.
#             fun = asyncio.to_thread(YouTubeSearch, command.removeprefix("youtube search "))  # Schedule YouTube search.
#             funcs.append(fun)


#         elif command.startswith("system "):  # Handle system commands.
#             fun = asyncio.to_thread(System, command.removeprefix("system "))  # Schedule system command.
#             funcs.append(fun)

#         else:
#             print(f"No Function Found. For {command}")  # Print an error for unrecognized commands.

#         results = await asyncio.gather(*funcs)  # Execute all tasks concurrently.

#         for result in results:  # Process the results.
#             if isinstance(result, str):
#                 yield result
#             else:
#                 yield result


#     # Asynchronous function to automate command execution.
# async def Automation(commands: list[str]):

#     async for result in TranslateAndExecute(commands):  # Translate and execute commands.
#         pass

#         return True  # Indicate success.
    



from AppOpener import close, open as appopen, give_appnames  # Import functions to open and close apps.
from webbrowser import open as webopen  # Import web browser functionality.
from pywhatkit import search, playonyt  # Import functions for Google search and YouTube playback.
from dotenv import dotenv_values  # Import dotenv to manage environment variables.
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML content.
from rich import print  # Import rich for styled console output.
from groq import Groq  # Import Groq for AI chat functionalities.
import webbrowser  # Import webbrowser for opening URLs.
import subprocess  # Import subprocess for interacting with the system.
import requests  # Import requests for making HTTP requests.
import keyboard  # Import keyboard for keyboard-related actions.
import asyncio  # Import asyncio for asynchronous programming.
import os  # Import os for operating system functionalities.

# Load environment variables from the .env file.
env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")  # Fetch Groq API Key from environment variables.

# Define a user-agent for making web requests.
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

# Initialize the Groq client with the API Key.
Client = Groq(api_key=GroqAPIKey)

# List to store chatbot messages.
messages = []

def OpenApp(app, sess=requests.session()):
    try:
        available_apps = give_appnames()
        if app.lower() in available_apps:
            subprocess.Popen(app, shell=True)
            return True
        else:
            print(f"Error: '{app}' not found in installed applications. Trying web search...")
            OpenAppFromWeb(app)
    except:
        print(f"Could not open '{app}' using AppOpener. Trying web search...")
        OpenAppFromWeb(app)
    return False

def OpenAppFromWeb(app):
    url = f"https://www.google.com/search?q={app} app download"
    webopen(url)

def extract_links(html):
    if html is None:
        return []
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', {'jsname': 'UWckNb'})
    extracted_links = [link.get('href') for link in links]
    return extracted_links if extracted_links else []

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": useragent}
    response = requests.get(url, headers=headers)
    return response.text if response.status_code == 200 else None

def PlayYoutube(query):
    playonyt(query)
    return True

def CloseApp(app):
    try:
        close(app, match_closest=True, output=True, throw_error=True)
        return True
    except:
        print(f"Error: Could not close '{app}'")
        return False

def System(command):
    actions = {
        "mute": lambda: keyboard.press_and_release("volume mute"),
        "unmute": lambda: keyboard.press_and_release("volume mute"),
        "volume_up": lambda: keyboard.press_and_release("volume up"),
        "volume_down": lambda: keyboard.press_and_release("volume down"),
    }
    if command in actions:
        actions[command]()
    else:
        print(f"Error: Unknown system command '{command}'")
    return True

async def TranslateAndExecute(commands: list[str]):
    funcs = []
    for command in commands:
        try:
            if command.startswith("open "):
                fun = asyncio.to_(OpenApp, command.removeprefix("open "))
                funcs.append(fun)
            elif command.startswith("play "):
                fun = asyncio.to_thread(PlayYoutube, command.removeprefix("play "))
                funcs.append(fun)
            elif command.startswith("close "):
                fun = asyncio.to_thread(CloseApp, command.removeprefix("close "))
                funcs.append(fun)
            elif command.startswith("system "):
                fun = asyncio.to_thread(System, command.removeprefix("system "))
                funcs.append(fun)
            else:
                print(f"No Function Found for '{command}'")
        except Exception as e:
            print(f"Error executing command '{command}': {e}")

    results = await asyncio.gather(*funcs, return_exceptions=True)
    for result in results:
        if isinstance(result, Exception):
            print(f"Command failed: {result}")
        else:
            yield result

async def Automation(commands: list[str]):
    async for result in TranslateAndExecute(commands):
        pass
    input("Press home to exit...")  # Prevents the script from closing immediately
    return True

# if __name__ == "__main__":
#     asyncio.run(Automation(["open facebook", "open youtube", "play karan aujla song"]))