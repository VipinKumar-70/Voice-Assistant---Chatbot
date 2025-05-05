# Import necessary modules
from langchain_google_community import GoogleSearchAPIWrapper
import os
from Config import GOOGLE_CSE_ID, GOOGLE_API_KEY

os.environ["GOOGLE_CSE_ID"] = GOOGLE_CSE_ID
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

Google_Search_Description = """
This tool allows users to perform a Google search and retrieve relevant information.  

## Parameters:  
- `query` (str): The search term or query entered by the user.
"""

# Initialize Google Search API Wrapper
class CustomGoogleSearchAPIWrapper(GoogleSearchAPIWrapper):
    def run(self, query):
        return super().run(query)

G_search = CustomGoogleSearchAPIWrapper()