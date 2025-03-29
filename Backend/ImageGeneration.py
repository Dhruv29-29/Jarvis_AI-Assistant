import asyncio
from random import randint
from PIL import Image
import requests
from dotenv import get_key
import os
import threading
import asyncio
import time
from random import randint
from PIL import Image
import requests
from dotenv import get_key
import os

import threading


# Function to open and display the image immediately
def open_image(image_path):
    try:
        # Open and display the image
        img = Image.open(image_path)
        print(f"Opening image: {image_path}")
        img.show()
    except IOError:
        print(f"Unable to open {image_path}")


# API details for the Hugging Face Stable Diffusion model
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {get_key('.env', 'HuggingFaceAPIKey')}"}


# Async function to send a query to the Hugging Face API
async def query(payload):
    response = await asyncio.to_thread(requests.post, API_URL, headers=headers, json=payload)
    return response.content


# Async function to generate images based on the given prompt
async def generate_images(prompt: str, num_images: int):

     

    

    image_paths = []
    
    # Generate multiple images
    for i in range(num_images):
        payload = {
            "inputs": f"{prompt}, quality=4K, sharpness=maximum, Ultra High details, high resolution, seed={randint(0, 1000000)}",
        }

        image_bytes = await query(payload)
        
        # Save the generated image to a file
        image_path = f"Frontend/Files/generated_{prompt.replace(' ', '_')}_{i + 1}.jpg"
        with open(image_path, "wb") as f:
            f.write(image_bytes)
        
        # Save the path of the generated image in the ImageGeneration.data file
        with open("Frontend/Files/ImageGeneration.data", "a") as data_file:
            data_file.write(f"{image_path}\n")
        
        image_paths.append(image_path)

        # Open the image immediately after it's generated
        open_image(image_path)

    return image_paths


# Wrapper function to generate and open multiple images
def generate_and_open_images(prompt: str, num_images: int):
    # Run the async image generation
    asyncio.run(generate_images(prompt, num_images))


# Main function to call image generation
def gen_image(prompt):
    generate_and_open_images(prompt, num_images=5)



