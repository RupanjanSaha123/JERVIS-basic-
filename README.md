# JERVIS-basic-

J.A.R.V.I.S. - A Simple Python Voice Assistant
A simple, yet powerful, voice assistant inspired by Tony Stark's J.A.R.V.I.S. This project is built entirely in Python and relies on a collection of robust libraries to provide a seamless voice-controlled experience. It can understand your commands to perform tasks like opening websites, searching Wikipedia, and offering timely greetings, all without requiring any external API keys.

🚀 Features
Voice-Activated Commands: Interact with your computer using just your voice.

Web Automation:

"Open YouTube"

"Open Google"

"Open Spotify"

Information Retrieval:

Ask questions like, "who is Albert Einstein according to Wikipedia?" to get a spoken summary.

Time-Based Greetings:

Greets you with "Good Morning," "Good Afternoon," or "Good Evening" based on the time of day.

API-Free: Works completely offline for greetings and locally for web tasks, with no need for paid API keys.

🛠️ How It Works
This assistant utilizes a combination of Python libraries to function:

pyttsx3: A text-to-speech conversion library that allows the assistant to speak back to you.

SpeechRecognition: Recognizes your voice commands and converts them into text. It uses the system's default microphone.

wikipedia: Fetches and summarizes information from Wikipedia.

webbrowser: Opens web pages in your default browser.

datetime: Used to determine the current time for personalized greetings.

📋 Getting Started
Follow these instructions to get your own J.A.R.V.I.S. assistant up and running on your local machine.

Prerequisites
Make sure you have Python 3.6 or newer installed on your system.

Installation
Clone the repository to your local machine:

git clone https://github.com/RupanjanSaha123/JERVIS(basic).git

Navigate to the project directory:

cd JERVIS(basic)

Install the required Python libraries using pip:

pip install -r requirements.txt

If a requirements.txt file is not available, you can install the packages manually:

pip install pyttsx3 speechrecognition wikipedia

Note: webbrowser and datetime are part of the standard Python library and do not need to be installed separately.

▶️ Usage
To start the voice assistant, simply run the main Python script from your terminal:

python main.py

The assistant will greet you and then start listening for your commands.

Example Commands
"Jarvis, open YouTube"

"Jarvis, what is the capital of France according to Wikipedia?"

"Jarvis, open Google"

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request


Made with ❤️ by Rupanjan Saha.
