# import pywhatkit as kit
# import time
# from AppOpener import open as appopen
# import pyautogui
# from Backend.Chatbot import ChatBot
# from Backend.SpeechToText import SpeechRecognition

# def send_whatsapp_message_by_name(contact_name, message):
#     """
#     Sends a WhatsApp message to a saved contact name using pywhatkit.
#     :param contact_name: Name of the contact as saved in your phone (e.g., "John Doe")
#     :param message: The message to send
#     """
#     try:
#         # Open WhatsApp using AppOpener
#         appopen("whatsapp")
#         time.sleep(3)
#         # pyautogui.hotkey("win", "up")
        
#         # Click on the Search icon in WhatsApp
#         pyautogui.hotkey("ctrl", "f")  # This works for web WhatsApp
#         time.sleep(1)
#         # Type the contact name and press Enter
#         pyautogui.write(contact_name)
#         time.sleep(1)
#         pyautogui.press("enter")
#         time.sleep(1)
        
#         pyautogui.click(291,220)
#         time.sleep(2)
#         # Type the message and send it
#         pyautogui.write(message)
#         time.sleep(1)
#         pyautogui.press("enter")
#         print(f"Message sent to {contact_name}!")
        
#     except Exception as e:
#         print(f"An error occurred: {e}")
# # def massage_prompt(command):
# #     contact_name = input("Enter the contact name as saved in your phone: ")
# #     message = input("Enter the message you want to send: ")
# #     send_whatsapp_message_by_name(contact_name, message)
    




# def split_prompt(prompt):
#     # Convert the prompt to lowercase to handle case insensitivity
#     prompt = prompt.lower()
    
#     # Check if the prompt follows the expected pattern
#     if "send a message to" in prompt and "that" in prompt:
#         # Split the prompt to get name and message
#         name = prompt.split("send a message to")[1].split("that")[0].strip()

#         message = prompt.split("that")[1].strip()
#         return(name,message)
#     else:
#         return None, "Invalid prompt format"

# # Example input

# def whats_msg(command):
#     massage_ai = "i will give to prompt and send a  friendly keep massage short as it can , do not give discription"
#     new_msg=ChatBot(f"{command}{massage_ai}")
#     return new_msg

# if __name__ == "__main__":
#     prompt = SpeechRecognition()
#     name, message = split_prompt(prompt)
#     new_msg=whats_msg(prompt)
#     print(new_msg)
#     send_whatsapp_message_by_name(name,new_msg)



# import time
# from AppOpener import open as appopen
# import pyautogui

# def open_whatsapp_and_check_fullscreen():
#     """
#     Opens WhatsApp and checks if it's in full screen.
#     If not, maximizes the window.
#     """
#     try:
#         # Open WhatsApp using AppOpener
#         appopen("whatsapp")
#         time.sleep(3)  # Wait for WhatsApp to open
        
#         # Get screen size
#         screen_width, screen_height = pyautogui.size()
        
#         # Get active window size
#         active_window = pyautogui.getActiveWindow()
#         window_width, window_height = active_window.width, active_window.height
        
#         print(f"Screen Size: {screen_width}x{screen_height}")
#         print(f"Window Size: {window_width}x{window_height}")
        
#         # Check if the window is in full screen
#         if window_width < screen_width or window_height < screen_height:
#             print("WhatsApp is not in full screen. Maximizing...")
#             pyautogui.hotkey("win", "up")
#         else:
#             print("WhatsApp is already in full screen.")
            
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     open_whatsapp_and_check_fullscreen()



import requests
import json

# Replace with your Hugging Face API key
HUGGINGFACE_API_KEY = "your_huggingface_api_key"

# Hugging Face model endpoint (Change based on availability)
API_URL = "https://api-inference.huggingface.co/models/facebook/dino-vitb8"

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

def image_to_3d(image_path):
    """Sends an image to Hugging Face API to generate a 3D model."""
    
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    response = requests.post(API_URL, headers=headers, data=image_data)
    
    if response.status_code == 200:
        result = response.json()
        print("3D Model Generation Successful:", json.dumps(result, indent=2))
    else:
        print("Error:", response.status_code, response.text)

# Example usage
image_to_3d("your_image.jpg")
