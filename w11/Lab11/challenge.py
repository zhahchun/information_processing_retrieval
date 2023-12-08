api_key = "2ba5dfcc2ae7af5aa00586fa68e17b30"

import requests
import json
import pprint

##### Useful URLS
# Base URL for accessing the TMBD API
movies_base= "https://api.themoviedb.org/3/"

# Additional URLS for searching
people_search = movies_base + "search/person"
movie_search = movies_base + "search/movie"

##### Code for accessing TMBD

# Request information about a movie, and pass the api_key as a parameter
movie = str(input('What movie do you want to search? '))
# parameter = {"api_key": api_key, "query": "Harry Potter"}
parameter = {"api_key": api_key, "query": movie}
result_json = requests.get(movie_search, parameter)

# Convert the results from JSON to a dictionary
results = json.loads(result_json.text)

# Pretty print the dictionary so we can see what it looks like
# get the first movie id
# pprint.pprint(results)
movie_id = str(results['results'][0]['id'])
# print(movie_id)

# URL for getting information about Harry Potter
hp_movie = movies_base + "movie/" + movie_id

# URL for getting the cast and crew lists for movie 24428 (Avengers)
movie_credits = movies_base + "movie/" + movie_id + "/credits"

# Request information about the Marvels, and pass the api_key as a parameter
parameter02 = {"api_key": api_key}
result_json02 = requests.get(hp_movie, parameter02)
result_json03 = requests.get(movie_credits, parameter02)

# Convert the results from JSON to a dictionary
results02 = json.loads(result_json02.text)
results03 = json.loads(result_json03.text)

print(results02['title'])
print(results02['tagline'])
print('----------------------')
print(results02['overview'])
for i in results02['genres']:
    print('-', i['name'])

count = 0
print('Starring:')
for i in results03['cast']:
    print('*', i['name'])
    count += 1
    if count == 10:
        break
    



