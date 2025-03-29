import json
from flask import flash,render_template


def load_chat_log(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def print_chat_log(chat_log):
    print("User's Messages:")
    for entry in chat_log:
        if entry["role"] == "user":
            return(f"User: {entry['content']}")
    
    print("\nAssistant's Messages:")
    for entry in chat_log:
        if entry["role"] == "assistant":
            return render_template('index.html', username= entry['content'])

if __name__ == "__main__":
    filename = "Data\ChatLog.json"  # Change this to your actual JSON file name
    chat_log = load_chat_log(filename)
    print_chat_log(chat_log)

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     name = "Dhruv"  # Python variable
#     return render_template('index.html', username=name)

# if __name__ == '__main__':
#     app.run(debug=True)