import os
import subprocess
import psutil
import webbrowser
import requests
from datetime import datetime
import pyttsx3
from bs4 import BeautifulSoup
import time
from threading import Thread
import pycaw
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Helper function to check if a process is running
def is_process_running(process_name):
    for proc in psutil.process_iter(attrs=['name']):
        if proc.info['name'] == process_name:
            return True
    return False

# Function to get weather information
def get_weather(city):
    api_key = "YOUR_WEATHER_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]["description"]
        temperature = main["temp"]
        return f"The weather in {city} is {weather} with a temperature of {temperature} degrees Celsius."
    else:
        return "Sorry, I couldn't find the weather for that location."

# Function to search for a YouTube video and open the first result
def search_youtube_video(query):
    api_key = "AIzaSyCGsPBEQheH3OsOk0c0mV1xRgLNLQ4utlo"
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={api_key}&type=video&maxResults=1"
    response = requests.get(search_url)
    if response.status_code == 200:
        data = response.json()
        if data["items"]:
            video_id = data["items"][0]["id"]["videoId"]
            video_title = data["items"][0]["snippet"]["title"]
            webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")
            speak(f"Now playing: {video_title}")
        else:
            speak("Sorry, I couldn't find any videos for that query.")
    else:
        speak("Failed to reach YouTube API.")

# Function to search the web using Google
def search_google(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    speak(f"Here are the search results for {query}")

# Function to handle voice commands
def handle_command(command, user_name):
    command = command.lower()

    if "play youtube" in command:
        search_term = command.replace("play", "" , "on youtube" ).strip()
        search_youtube_video(search_term)
    elif "search" in command:
        search_term = command.replace("search", "").strip()
        search_google(search_term)
    elif "weather" in command:
        city = command.replace("weather in", "").strip()
        weather_info = get_weather(city)
        speak(weather_info)
    elif "decrease volume" in command:
        adjust_volume("decrease")
    elif "mute volume" in command:
        adjust_volume("mute")
    elif "unmute volume" in command:
        adjust_volume("unmute")
    elif "shut down" in command:
        speak("Shutting down the computer.")
        os.system("shutdown /s /t 1")
    elif "restart" in command:
        speak("Restarting the computer.")
        os.system("shutdown /r /t 1")
    elif "lock screen" in command:
        speak("Locking the screen.")
        os.system("rundll32.exe user32.dll, LockWorkStation")
    elif "close" in command or "exit" in command or "stop" in command:
        speak("Goodbye!")
        return True  # This will break the loop in voice.py
    else:
        speak("Sorry, I don't know that command.")
    return False
