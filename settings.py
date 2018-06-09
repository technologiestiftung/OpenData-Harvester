from dotenv import load_dotenv
load_dotenv()

import os

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
