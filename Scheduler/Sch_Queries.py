from Jivan import QUERIES, RESPONSES, Run_Agent
import time
from History import set_chat_history
from Preferences import set_preference
import threading

# Function to check if there are any user queries
def Check() -> str:
    """
    This function checks the User Queries.
    """
    if len(QUERIES) > 0:
        return QUERIES[0]

# Function to perform action based on the user query
def Action(query : str) -> str:
    """
    This function performs the action based on the User Query.
    """
    Response = Run_Agent(query)
    # Perform action here
    del QUERIES[0]
    RESPONSES.append(Response)
    threading.Thread(target=After_Action, args=(query, Response)).start()

# Function to handle post-action tasks
def After_Action(query, Response):
    """
    This function handles tasks after the main action is performed.
    """
    set_chat_history(query, Response)
    set_preference(f"{query} | {Response}")

# Main function to schedule user queries and actions
def Queries_Scheduler():
    """
    This function schedules the User Queries and Actions.
    """
    while True:
        query = Check()
        if query:
            Action(query)
        time.sleep(0.5)