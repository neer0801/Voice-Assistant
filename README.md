# Python Voice Assistant

## Project Overview
This project is a Python-based voice assistant capable of performing various tasks such as searching YouTube, retrieving weather information, controlling system volume, and more. It listens to voice commands and responds accordingly using speech recognition and text-to-speech features.

## Requirements
To set up and use the assistant, you will need the following Python libraries:
- `speech_recognition`
- `pyttsx3`
- `requests`
- `psutil`
- `beautifulsoup4`
- `pycaw` (For controlling system audio)
- `comtypes`

You can install the required libraries with the following command:



## How to Run
1. Clone or download the project.
2. Make sure you have Python installed (Python 3.x is recommended).
3. Install the required Python libraries using the `pip install` command above.
4. Add your YouTube Data API key and weather API key in the `commands.py` file where placeholders are indicated.
5. Run the assistant using the `voice.py` file:


6. The assistant will prompt you to enter your name. Once entered, it will start listening for voice commands.

## Available Commands
Here are the available commands you can use with the assistant:

1. **Play YouTube Video**: Searches for a YouTube video and plays the first result.
- Example: `play Despacito on YouTube`

2. **Search Google**: Opens a Google search for the specified query.
- Example: `search Python programming`

3. **Get Weather**: Retrieves and announces the weather for a specific city.
- Example: `weather in Rajkot`

4. **Volume Control**:
- **Decrease Volume**: Lowers the system volume.
  - Example: `decrease volume`
- **Mute Volume**: Mutes the system volume.
  - Example: `mute volume`
- **Unmute Volume**: Unmutes the system volume.
  - Example: `unmute volume`

5. **System Control**:
- **Shut Down**: Shuts down the computer.
  - Example: `shut down`
- **Restart**: Restarts the computer.
  - Example: `restart`
- **Lock Screen**: Locks the screen.
  - Example: `lock screen`

6. **Exit the Assistant**: Stops the voice assistant.
- Example: `close` or `exit`

## Testing Example
To test if the assistant is working properly, you can try the following command after starting it:


This will open YouTube and play the first search result for "a song".

## Note
- Ensure that your microphone is working properly and you are connected to the internet for web-based commands like YouTube and weather.
