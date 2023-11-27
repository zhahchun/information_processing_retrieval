api_key = "2ba5dfcc2ae7af5aa00586fa68e17b30"

import requests
import json
import pprint


##### Useful URLS
# Base URL for accessing the TMBD API
movies_base= "https://api.themoviedb.org/3/"

# URL for getting information about the the Marvels (movie id 609681)
# marvels = movies_base + "movie/609681"
new_movie = movies_base + "movie/945729"

# Additional URLS for searching
people_search = movies_base + "search/person"
movie_search = movies_base + "search/movie"

# URL for getting the cast and crew lists for movie 24428 (Avengers)
# movie_credits = movies_base + "movie/24428/credits"
# movie_credits = movies_base + "movie/609681/credits"
movie_credits = movies_base + "movie/945729/credits"



##### Code for accessing TMBD

# Request information about the Marvels, and pass the api_key as a parameter
parameter = {"api_key": api_key}
result_json = requests.get(new_movie, parameter)
result_json02 = requests.get(movie_credits, parameter)


# Convert the results from JSON to a dictionary
results = json.loads(result_json.text)
results02 = json.loads(result_json02.text)


# Pretty print the dictionary so we can see what it looks like
# pprint.pprint(results)
print(results['title'])
print(results['tagline'])
print('----------------------')
print(results['overview'])
for i in results['genres']:
    print('-', i['name'])


count = 0
print('Starring:')
for i in results02['cast']:
    print('*', i['name'])
    count += 1
    if count == 10:
        break
    



