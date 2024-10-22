import speech_recognition as sr
import pyttsx3
from commands import handle_command

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return ""

def main():
    print("Starting the voice assistant!")
    user_name = input("Please enter your name: ")
    if user_name:
        speak(f"Welcome, {user_name}! I am your voice assistant.")
        
        while True:
            command = listen()
            if command:
                if handle_command(command, user_name):
                    break  # Break if the 'close' command is given
    else:
        speak("No name entered. Exiting the program.")

if __name__ == "__main__":
    main()
