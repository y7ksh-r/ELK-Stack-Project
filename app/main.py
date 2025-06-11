import os
from flask import Flask, request
import logging, random

app = Flask(__name__)

# Set up logging to console (optional)
logging.basicConfig(level=logging.INFO)

# Set up file logging
os.makedirs('/app/logs', exist_ok=True)  

file_handler = logging.FileHandler('/app/logs/app.log')# You can use an absolute path if needed
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def home():
    app.logger.info("Home page accessed")
    return "Home Page"

@app.route('/login', methods=['POST'])
def login():
    app.logger.warning("Login attempt")
    return "Login Page"

@app.route('/error')
def error():
    app.logger.error("Error occurred")
    return "Error Page"

@app.route('/random')
def random_log():
    choice = random.choice(['info', 'warn', 'error'])
    if choice == 'info':
        app.logger.info("Random info log")
    elif choice == 'warn':
        app.logger.warning("Random warn log")
    else:
        app.logger.error("Random error log")
    return f"Random log generated: {choice}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
