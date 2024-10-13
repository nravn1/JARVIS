# youtube_action.py
import subprocess
import time

def open_youtube():
    try:
        # Adjust the command based on your operating system
        # For Windows:
        subprocess.Popen(["start", "chrome", "https://www.youtube.com"], shell=True)
        return "Youtube is now open, sir"
    except Exception as e:
        return f"Error opening YouTube in Google Chrome: {str(e)}"

def youtube_action():
    youtube = open_youtube()
    print(youtube)
    time.sleep(4)
