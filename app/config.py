import os
from dotenv import load_dotenv

# 1. Open the vault: Load variables from .env into Python's memory
load_dotenv()

# 2. Grab the specific variables we need safely
# The second argument (e.g., "Default App") is a fallback just in case the .env file goes missing!
APP_NAME = os.getenv("APP_NAME", "Default App")
DEBUG = os.getenv("DEBUG", "False") == "True"