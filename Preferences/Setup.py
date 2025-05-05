import os

Drive_Path = "C:"
Jivan_Main_Folder = os.path.join(Drive_Path, "Jivan")
Preference_Path = os.path.join(Jivan_Main_Folder, "Preferences.log")

os.makedirs(Jivan_Main_Folder, exist_ok=True)

if not os.path.exists(Preference_Path):
    with open(Preference_Path, "w") as file:
        file.write("")