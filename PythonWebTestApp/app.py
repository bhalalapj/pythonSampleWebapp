from flask import Flask
from pycricbuzz import Cricbuzz
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello! World, Welcome to flask python web app from visual studio 2019"



@app.route('/cricbuzz')
def circbuzz():
    c = Cricbuzz()
    matches = c.matches()
    newMatches = []
    for match in matches:
        try:
            if match['type'] == 'T20' :
                newMatches.append(match)
        except:
            return "Error occured in interation"             

    return json.dumps(newMatches, indent=4)

if __name__ == '__main__':
    app.run('localhost',4449)