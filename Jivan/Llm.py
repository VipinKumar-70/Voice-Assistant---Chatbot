from langchain_google_genai import ChatGoogleGenerativeAI
from Config import GOOGLE_API_KEY
import os

# Set the GOOGLE_API_KEY environment variable
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


# Initialize the ChatGoogleGenerativeAI model with specified parameters
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # Specify the model to use
    temperature=0.7,           # Set the temperature for Generating Response by Agent
    max_retries=3,             # Set the maximum number of retries for API calls
)