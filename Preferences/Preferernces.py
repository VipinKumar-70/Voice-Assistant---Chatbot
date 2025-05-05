import os
from .Template import PREFERENCE_TEMPLATE
from .Llm import llm
from .Setup import Preference_Path

# Function to update preferences based on the conversation
def set_preference(Conversation):
   # Check if the preference file exists
   if os.path.exists(Preference_Path):
      # Read existing preferences from the file
      with open(Preference_Path, 'r') as file:
         Existing_Preferences = file.read()
   else:
      Existing_Preferences = None

   # Format the prompt with existing preferences and conversation
   formatted_prompt = PREFERENCE_TEMPLATE.format(
      Existing_Preferences=Existing_Preferences,
      Conversation=Conversation
   )

   # Invoke the LLM with the formatted prompt
   result = llm.invoke(formatted_prompt)
   
   # Write the updated preferences back to the file
   with open(Preference_Path, 'w') as file:
      file.write(result.content)
      
# Function to read the current preferences from the file
def get_preference():
   # Check if the preference file exists
   if os.path.exists(Preference_Path):
      # Read and return the preferences from the file
      with open(Preference_Path, 'r') as file:
         return file.read()