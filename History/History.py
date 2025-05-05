import json
import os
from datetime import datetime
from .Setup import Chat_History_Path

def load_chat_history():
    """Load chat history from the JSON file, handling errors gracefully."""
    if not os.path.exists(Chat_History_Path):
        return {"Chat_history": []}

    try:
        with open(Chat_History_Path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        # Handle corrupted or inaccessible file
        return {"Chat_history": []}

def save_chat_history(data):
    """Save chat history to the JSON file safely."""
    try:
        with open(Chat_History_Path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error saving chat history: {e}")

def set_chat_history(query, response):
    """Add a new chat entry with a timestamp while keeping only the last 5 entries."""
    data = load_chat_history()

    # Append new chat entry with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data.setdefault("Chat_history", []).append({
        "Timestamp": timestamp,
        "Query": query,
        "Response": response
    })

    # Keep only the last 5 entries
    data["Chat_history"] = data["Chat_history"][-5:]

    save_chat_history(data)

def get_chat_history():
    """Retrieve the latest chat history entries."""
    return load_chat_history().get("Chat_history", [])
