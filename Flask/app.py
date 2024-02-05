import os
import sys

from flask import Flask, render_template, redirect, url_for, request, send_from_directory, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from pycsp.parallel import *

from models import puzzleAlPaccino

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lacletressecrete'


class ProblemForm(FlaskForm):
    person1 = StringField('Person 1')
    person2 = StringField('Person 2')
    person3 = StringField('Person 3')

    place1 = StringField('Place 1')
    place2 = StringField('Place 2')
    place3 = StringField('Place 3')

    object1 = StringField('Object 1')
    object2 = StringField('Object 2')
    object3 = StringField('Object 3')

    constraints = StringField('Constraints')
    submit = SubmitField('Generate Problem')


class People(Process):
    def __init__(self, people, channel):
        super(People, self).__init__()
        self.people = people
        self.channel = channel
        self.start()

    def run(self):
        self.channel.write(list(self.people))
        self.channel.poison()


class Places(Process):
    def __init__(self, places, channel):
        super(Places, self).__init__()
        self.places = places
        self.channel = channel
        self.start()

    def run(self):
        self.channel.write(list(self.places))
        self.channel.poison()


class Objects(Process):
    def __init__(self, objects, channel):
        super(Objects, self).__init__()
        self.objects = objects
        self.channel = channel
        self.start()

    def run(self):
        self.channel.write(list(self.objects))
        self.channel.poison()


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/favicon.icon')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()

        # Vérifier les contraintes à l'aide des modèles PyCSP
        print(puzzleAlPaccino.logic_puzzle_alPacino(), file=sys.stderr)
        result = ""

        return jsonify({'success': result})

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/solve_puzzle', methods=['POST'])
def solve_puzzle():
    puzzle_type = request.form['puzzle_type']
    if puzzle_type == "pasta":
        return render_template("pasta.html")
    if puzzle_type == "film":
        return render_template("film.html")
    if puzzle_type == "computer":
        return render_template("computer.html")
    return f"Vous avez choisi de résoudre le puzzle : {puzzle_type}"


@app.route('/create_puzzle')
def create_puzzle():
    form = ProblemForm()
    if form.validate_on_submit():
        # Récupérer les données du formulaire
        people = [form.person1.data, form.person2.data, form.person3.data]
        places = [form.place1.data, form.place2.data, form.place3.data]
        objects = [form.object1.data, form.object2.data, form.object3.data]
        constraints = form.constraints.data

        # Traiter les données et générer le problème pyCSP
        # Créer des canaux pour les variables CSP
        people_channel = Channel()
        places_channel = Channel()
        objects_channel = Channel()

        # Envoyer les domaines des variables aux canaux
        people_channel.write(range(3))
        places_channel.write(range(3))
        objects_channel.write(range(3))

        # Créer des processus CSP pour chaque catégorie
        people_process = People(people, people_channel.reader())
        places_process = Places(places, places_channel.reader())
        objects_process = Objects(objects, objects_channel.reader())

        # Attendre la fin des processus CSP
        people_process.join()
        places_process.join()
        objects_process.join()

        # Récupérer les solutions
        people_solution = people_channel.read()
        places_solution = places_channel.read()
        objects_solution = objects_channel.read()

        solutions = [{'People': people_solution, 'Places': places_solution, 'Objects': objects_solution}]
        return render_template('solution.html', solutions=solutions)
    return render_template('create.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
