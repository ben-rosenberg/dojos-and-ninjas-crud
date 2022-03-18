from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja
from flask_app import app
from flask import render_template, redirect, request


@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def show_all_dojos() -> str:
    all_dojos = Dojo.get_all_dojos()
    return render_template('read.html', all_dojos=all_dojos)

""" @app.route('/dojos/<dojo_id>')
def show_dojo(dojo_id: str) -> str:
    this_dojo = Dojo.get_dojo(dojo_id)
    this_dojos_ninjas = Dojo.get_dojos_ninjas(dojo_id)
    return render_template('dojo.html', this_dojo=this_dojo, this_dojos_ninjas=this_dojos_ninjas) """

@app.route('/dojos/<dojo_id>')
def show_dojo(dojo_id: str) -> str:
    this_dojo_with_ninjas = Dojo.get_dojo_with_ninjas_by_dojo_id(dojo_id)
    return render_template('dojo.html', this_dojo_with_ninjas=this_dojo_with_ninjas)

""" @app.route('/dojos/<dojo_id>')
def show_dojo(dojo_id: str) -> str:
    this_dojos_ninjas = Ninja.get_ninjas_by_dojo_id(dojo_id)
    return render_template('dojo.html', this_dojo_with_ninjas = this_dojos_ninjas)         """


@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    new_dojo_id = Dojo.create_dojo(request.form)
    return redirect(f'/dojos/{str(new_dojo_id)}')