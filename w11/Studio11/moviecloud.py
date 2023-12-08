import sys
import random
import requests
import json
from pprint import pprint
from turtle import *
from random import randrange

api_key = "cac7404b25f07c75e9f9a3ee1d0c0979"
# Challenge User Input
movie_keyword = textinput('Search Movie','What movie do you want to search? ')

speed(9)
def draw_word(dict_pop, movie_name):
    # change color setting into (r,g,b)
    colormode(255) 

    max_font = max(dict_pop.values())
    penup()
    goto(0, 200)
    write(movie_name, font=("Times New Roman", 60 , "normal", 'underline'), align = 'center')
    penup()
    goto(-600, 0)
    for k in dict_pop:
        penup()
        #randomize the color
        color(randrange(255),randrange(255),randrange(255))
        write(k, font=("Arial", int(dict_pop[k]) , "normal"), move=True)
        
        x, y = pos()
        if x >= 600.0:
            goto(-600, y-max_font)

##### Useful URLS
# Base URL for accessing the TMBD API
movies_base= "https://api.themoviedb.org/3/"

# Additional URLS for searching
people_search = movies_base + "search/person"
movie_search = movies_base + "search/movie"

# URL for getting the cast and crew lists for movie 24428 (Avengers)
movie_credits = movies_base + "movie/945729/credits"

##### Code for accessing TMBD
def search_movie(movie_keyword):
    parameter = {"api_key": api_key, "query": movie_keyword}
    result_json = requests.get(movie_search, parameter)

    # Convert the results from JSON to a dictionary
    results = json.loads(result_json.text)
    #pprint(results)
    id = ''
    name = ''
    for result in results['results']:
        id = str(result['id'])
        name = str(result['original_title'])
        break
    movie = {'id': str(id), 'name': name}
    return movie


def get_actors(id):
    movie_credits = movies_base + "movie/" + id + "/credits"

    parameter = {"api_key": api_key}
    result_json = requests.get(movie_credits, parameter)
    results = json.loads(result_json.text)
    # pprint(results, depth=1)
    count = 0
    actors = {}
    for cast in results['cast']:
        if count >= 30:
            break
        actors[cast['name']] = cast['popularity']
        #print("* " + cast['name'] + "    " + str(cast['popularity']))
        count += 1
    return actors

#main
movie = search_movie(movie_keyword)
movie_name = movie['name']
movie_id = movie['id']
actors = get_actors(movie_id)
#print(actors)
# print(words)
draw_word(actors, movie_name)
done()