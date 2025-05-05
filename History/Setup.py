import os
import json

Drive_Path = "C:"
Jivan_Main_Folder = os.path.join(Drive_Path, "Jivan")
Chat_History_Path = os.path.join(Jivan_Main_Folder, "Chat_History.json")

os.makedirs(Jivan_Main_Folder, exist_ok=True)

Temp = {
    "Chat_History": []
}

if not os.path.exists(Chat_History_Path):
    with open(Chat_History_Path, "w") as file:
        json.dump(Temp, file, indent=4)