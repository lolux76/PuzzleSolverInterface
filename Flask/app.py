import os

from flask import Flask, render_template, redirect, url_for, request, send_from_directory

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/favicon.icon')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/solve_puzzle', methods=['POST'])
def solve_puzzle():
    puzzle_type = request.form['puzzle_type']
    if puzzle_type == "pasta":
        return render_template("pasta.html")
    return f"Vous avez choisi de résoudre le puzzle : {puzzle_type}"


@app.route('/create_puzzle')
def create_puzzle():
    return "Page de création de puzzle"


if __name__ == '__main__':
    app.run(debug=True)
