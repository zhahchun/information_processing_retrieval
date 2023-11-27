api_key = "2ba5dfcc2ae7af5aa00586fa68e17b30"

import requests
import json
import pprint

##### Useful URLS
# Base URL for accessing the TMBD API
movies_base= "https://api.themoviedb.org/3/"

# URL for getting information about the the Marvels (movie id 609681)
marvels = movies_base + "movie/609681"
new_movie = movies_base + "movie/945729"

# Additional URLS for searching
people_search = movies_base + "search/person"
movie_search = movies_base + "search/movie"

# URL for getting the cast and crew lists for movie 24428 (Avengers)
movie_credits = movies_base + "movie/945729/credits"

##### Code for accessing TMBD

# Request information about the Marvels, and pass the api_key as a parameter
parameter = {"api_key": api_key, "query": "Avengers"}
result_json = requests.get(movie_search, parameter)

# Convert the results from JSON to a dictionary
results = json.loads(result_json.text)

# Pretty print the dictionary so we can see what it looks like
pprint.pprint(results)




