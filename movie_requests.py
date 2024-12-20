import os 
import csv
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OMDb_API_Key')

