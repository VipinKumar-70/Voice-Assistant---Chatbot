from Jivan import QUERIES
from Scheduler import Queries_Scheduler, Speak_Scheduler
import threading
import logging
from Speak import *

logging.getLogger().addHandler(logging.NullHandler())

threading.Thread(target=Queries_Scheduler, daemon=True).start()
threading.Thread(target=Speak_Scheduler, daemon=True).start()

while True:
    command = input("Enter command: ")
    QUERIES.append(command)
