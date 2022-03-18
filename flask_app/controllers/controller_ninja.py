from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo
from flask_app import app
from flask import render_template, redirect, request


@app.route('/ninjas/new')
def new_ninja():
    all_dojos = Dojo.get_all_dojos()
    return render_template('new_ninja.html', all_dojos=all_dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    new_ninja_id = Ninja.create_ninja(request.form)
    print(request.form)
    new_ninjas_dojo_id = request.form['dojo_id']
    return redirect(f'/dojos/{new_ninjas_dojo_id}')