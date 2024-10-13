# chrome_action.py
import subprocess
import time

def open_chrome():
    try:
        # Adjust the command based on your operating system
        # For Windows:
        subprocess.Popen(["start", "chrome"], shell=True)
        return "Google Chrome is now open, sir"
    except Exception as e:
        return f"Error opening Google Chrome: {str(e)}"

def close_chrome():
    try:
        # Adjust the command based on your operating system
        # For Windows:
        subprocess.Popen(["taskkill", "/f", "/im", "chrome.exe"], shell=True)
        return "Closing Google Chrome"
    except Exception as e:
        return f"Error closing Google Chrome: {str(e)}"

def chrome_actions(action):
    if action == 'open':
        chrome = open_chrome()
        print(chrome)
        time.sleep(5)
    elif action == 'close':
        killchrome = close_chrome()
        print(killchrome)
        time.sleep(4)
