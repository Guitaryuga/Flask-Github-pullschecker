import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
LOGIN_NAME = os.getenv('LOGIN_NAME')
TOKEN = os.getenv('TOKEN')
