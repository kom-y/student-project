import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Student Information System")
DEBUG = os.getenv("DEBUG", "False").strip().lower() in {"1", "true", "yes", "on"}

try:
    MAX_STUDENTS = int(os.getenv("MAX_STUDENTS", "100"))
except ValueError:
    MAX_STUDENTS = 100

# Read the secret when needed; never print or log it.
API_KEY = os.getenv("API_KEY", "")
