from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the value of the environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")