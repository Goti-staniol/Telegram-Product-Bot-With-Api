import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

#use this when you have a problem with creating a db
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_URL = f'sqlite:///{BASE_DIR}/db/database.db'

# DB_URL = f'sqlite:///db/database.db'