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
    with open('oscar_winners.csv','r') as oscar_file:
        try:
            
            reader=csv.DictReader(oscar_file)
            for row in reader:
                #stripping the movie id of any  leading or trailing space
                flick_id = row['IMDB'].strip()
                # append each id to the list of movie ids
                flick_ids.append(flick_id)
        except FileNotFoundError:
            print('The Oscar files have not been found')
    # get  movie info from ip
    for movie_id in flick_ids:
        try:
            payload = {'apikey': api_key, 'i': movie_id}
            res= requests.get('http://www.omdbapi.com/',params=payload)
               
        except Exception as e:
            print(e)
        res_json=res.json()
        #print(res_json)
        
        movie_title:str =res_json['Title']
        movie_runtime:int = int(res_json['Runtime'].strip('').strip('min'))
        movie_genre:str = res_json['Genre']
       
        movie_awards = res_json['Awards'].split(' ')
        movie_oscars=int(movie_awards[1])
        movie_wins=int(movie_awards[3])
        movie_nominations=int(movie_awards[6])
        movie_box_office=int(res_json['BoxOffice'].strip('$').replace(',', ''))
        print(type(movie_box_office))
        
    




 
request_data()