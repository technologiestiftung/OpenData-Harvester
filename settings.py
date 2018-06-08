from dotenv import load_dotenv
load_dotenv()

import os

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
