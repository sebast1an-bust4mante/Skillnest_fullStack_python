import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("APP_SECRET", "dev-only-change-this-secret")