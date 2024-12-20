import os 
import csv
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OMDb_API_Key')

def request_data():
    """

    
    """
    # Create list to store movie ids
    flick_ids=[]
    # reading the original file 
    with open('oscar_winners.csv') as oscar_file:
        try:
            reader=csv.DictReader(oscar_file)
            for row in reader:
                flick_id = row['IMDB'].strip()
                flick_ids.append(flick_id)
        except FileNotFoundError:
            print('The Oscar files have not been found')
    print(flick_ids)
           
       
request_data()