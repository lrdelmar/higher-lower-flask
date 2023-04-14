from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def higher_lower():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img width=300px src='https://media.giphy.com/media/ukgcHmvflVWjwE8eU5/giphy.gif'>"


random_number = randint(0, 9)


@app.route('/<int:num>')
def check_num(num):
    if num == random_number:
        return "<h1 style='color:green'>You guessed it!</h1>" \
               "<img src='https://media.giphy.com/media/VIPdgcooFJHtC/giphy.gif'>"
    elif num < random_number:
        return "<h1 style='color:orange'>Too low, try again</h1>" \
               "<img src='https://media.giphy.com/media/2DqT8eRoIYElG/giphy.gif'>"
    elif num > random_number:
        return "<h1 style='color:red'>Too high, try again</h1>" \
               "<img src='https://media.giphy.com/media/6uMqzcbWRhoT6/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
