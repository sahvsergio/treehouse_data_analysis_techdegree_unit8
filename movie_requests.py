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

    fieldnames =[
        'Title',
        'Runtime',
        'Genre',
        'Oscars',
        'Award Wins',
        'Award Nominations',
        'Box Office'
    ]
    with open('movies.csv', 'w') as movie_file:

        movie_writer = csv.DictWriter(movie_file, fieldnames=fieldnames)
        movie_writer.writeheader()
        for movie_id in flick_ids:
            try:
                payload = {'apikey': api_key, 'i': movie_id}
                res= requests.get('http://www.omdbapi.com/',params=payload)
                res_json = res.json()
                movie_data = {
                    'Title': res_json['Title'],
                    'Runtime': int(res_json['Runtime'].strip('').strip('min')),
                    'Genre': res_json['Genre'],
                    'Oscars': int(res_json['Awards'].split(' ')[1]),
                    'Award Wins': int(res_json['Awards'].split(' ')[3]),
                    'Award Nominations': int(res_json['Awards'].split(' ')[6]),
                    'Box Office': int(res_json['BoxOffice'].strip('$').replace(',', ''))
                }
                movie_writer.writerow(movie_data)
               
            except Exception as e:
                print(f'Error processing movie{movie_id}:{e}')



request_data()