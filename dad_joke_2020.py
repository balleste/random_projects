# # This is just a simple tool that queries the 'icanhazdadjoke' site via API.
# It asks you for a topic and returns a random joke based on the query results.

import requests
import json
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

title = 'Welcome to the Dad Joke 2020!!!'
url = 'https://icanhazdadjoke.com/search'

print(colored(figlet_format(title), color='magenta'))

def joke(topic):
    results= requests.get(
        url,
        headers={"Accept":"application/json"},
        params={
            'term': topic
        }
    ).json()

    if results['total_jokes'] == 1:
        print(f"I've got one joke about '{results['search_term']}'.  Here it is: ")
        print([query['results'][0]['joke']])
    elif results['total_jokes'] > 1:
        joke_list = [item['joke'] for item in results['results']]
        random_joke = choice(joke_list)
        print(f"I've got {results['total_jokes']} jokes about '{results['search_term']}'.  Here is one: ")
        print(random_joke)
    else:
        print(f"Sorry, I don't have any jokes about '{results['search_term']}', please try again.")

joke_question = input('Let me tell you a joke!  Give me a topic: ')
joke(joke_question)
