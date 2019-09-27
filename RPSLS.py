from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random
import requests

app = Flask(__name__)
cors = CORS(app)


#this is reproducing the current json format being used for choices, but it is not the one specified in the google doc
choices_list = [
    {"id": 1,"name": "rock"},
    {"id": 2,"name": "paper"},
    {"id": 3,"name": "scissors"},
    {"id": 4,"name": "lizard"},
    {"id": 5,"name": "spock"}
    ]

#for it to match with the specification it would need to be changed to be formatted like this:

##choicesList = [
##    {"rock": {"id": 1,"name": "rock"}},
##    {"paper": {"id": 2,"name": "paper"}},
##    {"scissors": {"id": 3,"name": "scissors"}},
##    {"lizard": {"id": 4,"name": "lizard"}},
##    {"spock": {"id": 5,"name": "spock"}}
##    ]


@app.route('/choices', methods=['GET'])
def choices():
    return jsonify(choices_list)

@app.route('/choice', methods=['GET'])
def choice():

    #using the random number endpoint provided (1-100) to generate a random number in the appropriate range
    content = requests.get('https://codechallenge.boohma.com/random').json()
    random_choice = content['random_number'] % 5
    return jsonify(choices_list[random_choice])

@app.route('/play', methods=['POST'])
def play():
    
    #I need to use force=True here because the mimetype in the header isn't actually of type applicaton/json
    content = request.get_json(force=True)
    
    player_choice = content['player']

    #using the random number endpoint provided (1-100) to generate a random number in the appropriate range
    content = requests.get('https://codechallenge.boohma.com/random').json()
    computer_choice = (content['random_number'] % 5) + 1

    
    diff = (player_choice - computer_choice) % 5
    results =""
    
    if (player_choice == computer_choice):
        results = "tie"
    elif (diff == 4 or diff == 2):
        results = "lose"
    else:
        results = "win"
    
    return {
        "results": results,
        "player": player_choice,
        "computer": computer_choice
        }
