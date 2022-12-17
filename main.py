from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def shuffle_cards():
    num_cards = request.args.get('num_cards')
    if num_cards is None:
        num_cards = 1
    else:
        num_cards = int(num_cards)

    cards = []
    with open('cards.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cards.append(row)

    return render_template('shuffle_cards.html', cards=cards[:num_cards])

if __name__ == '__main__':
    app.run()
##host='mickeysprojects.app', port=5000

