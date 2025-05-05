from Jivan import NOTIFICATIONS, SUGESTIONS, RESPONSES
from Speak import speak
import time
import threading

def Check() -> str:
    # Check for any available responses, notifications, or suggestions
    if len(RESPONSES) > 0:
        return RESPONSES.pop(0)
    elif len(NOTIFICATIONS) > 0:
        return NOTIFICATIONS.pop(0)
    elif len(SUGESTIONS) > 0:
        return SUGESTIONS.pop(0)

def Action(Text : str) -> None:
    # Perform the action of speaking the provided text
    print(Text)
    speak(Text)

def Speak_Scheduler():
    # Continuously check for new items to speak
    while True:
        response = Check()
        if response:
            Action(response)
            time.sleep(0.5)