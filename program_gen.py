import re
import os
import requests
from Backend.TextToSpeech import TextToSpeech

PROGRAM_FILES_DIR = "ProgramFiles"
os.makedirs(PROGRAM_FILES_DIR, exist_ok=True)

def generate_code(prompt):
    API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"
    headers = {"Authorization": "Bearer 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"}
    
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        response.raise_for_status()
        response_json = response.json()
        content = response_json.get("generated_text", "") if isinstance(response_json, dict) else response_json[0].get("generated_text", "")
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return ""
    except (KeyError, IndexError):
        print("Unexpected API response format.")
        return ""
    
    match = re.search(r"```(?:\w+)?\n(.*?)```", content, re.DOTALL)
    return match.group(1).strip() if match else content.strip()

def get_file_extension(language):
    extensions = {
        "python": ".py", "java": ".java", "c": ".c", "c++": ".cpp",
        "javascript": ".js", "html": ".html", "css": ".css",
        "ruby": ".rb", "php": ".php", "go": ".go", "swift": ".swift",
        "kotlin": ".kt", "r": ".r", "typescript": ".ts"
    }
    return extensions.get(language.lower())

def code_main(command):
    words = command.lower().split()
    if len(words) < 3:
        TextToSpeech("Please specify the language and what the program should do.")
        return
    
    language, request = words[0], " ".join(words[1:])
    file_extension = get_file_extension(language)
    if not file_extension:
        TextToSpeech(f"Unrecognized programming language: {language}.")
        return
    
    code = generate_code(f"Write a {language} program to {request}. Only code, no explanations.")
    if not code:
        TextToSpeech("Code generation failed. Please try again.")
        return
    
    filename = os.path.join(PROGRAM_FILES_DIR, f"generated_code{file_extension}")
    
    with open(filename, "w") as file:
        file.write(code)
    
    TextToSpeech(f"The {language} program has been saved as {filename}.")
    print(f"Saved: {filename}")

if __name__ == "__main__":
    code_main("html code only the complete to print hello world 5. No explanations. only clear code")
