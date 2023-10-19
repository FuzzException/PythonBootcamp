from flask import Flask
import random

app = Flask(__name__)

global rn 
rn = random.randint(0, 9)

@app.route("/")
def start() :
    return "<h3>Guess a number between 0 and 9</h3>"\
    "<img src='https://media.giphy.com/media/Kzbfaz4Bm27sCzZNDQ/giphy.gif'>"

@app.route("/number/<int:num>")
def number(num) :
    if num == rn :
        return "<p>You have guessed the number!!</p>"\
            "<img src='https://media.giphy.com/media/rplBYQtQebO5ARHyHU/giphy.gif'>"
    
    elif num > rn :
        return "<p>You have guessed too high!!</p>"\
        "<img src='https://media.giphy.com/media/3og0IuWMpDm2PdTL8s/giphy-downsized-large.gif'>"
    
    else :
        return "<p>You have guessed too low!!</p>"\
        "<img src='https://media.giphy.com/media/3oKHWfu68Q6XOz2I6Y/giphy.gif'>"

if __name__ =="__main__":
    app.run(port=8080)