from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def higher_lower():
    return "<div style='width:100%;display:grid'><h1 style='text-align:center'>Guess a number between 0 and 9</h1>" \
           "<img style='width:30%;margin:auto' src='https://media.giphy.com/media/ukgcHmvflVWjwE8eU5/" \
           "giphy.gif'></div>"


random_number = randint(0, 9)


@app.route('/<int:num>')
def check_num(num):
    if num == random_number:
        return "<div style='width:100%;display:grid'><h1 style='color:green;text-align:center' >You guessed it!</h1>" \
               "<img style='width:30%;margin:auto' src='https://media.giphy.com/media/VIPdgcooFJHtC/giphy.gif'></div>"
    elif num < random_number:
        return "<div style='width:100%;display:grid'><h1 style='color:orange;text-align:center'>Too low, try again</h1>" \
               "<img style='width:30%;margin:auto' src='https://media.giphy.com/media/2DqT8eRoIYElG/giphy.gif'></div>"
    elif num > random_number:
        return "<div style='width:100%;display:grid'><h1 style='color:red;text-align:center'>Too high, try again</h1>" \
               "<img style='width:30%;margin:auto' src='https://media.giphy.com/media/6uMqzcbWRhoT6/giphy.gif'></div>"


if __name__ == "__main__":
    app.run(debug=True)
