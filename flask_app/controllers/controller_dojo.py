from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return render_template('/dojos.html', dojos=Dojo.get_all())

@app.route('/create_dojo', methods=['post'])
def create_dojo():
    data={
        'name': request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/')

@app.route('/dojos/<id>')
def get_one(id):
    data={
        "id": id
    }
    ninja=Dojo.get_one_dojo_all_ninjas(data)
    print(ninja)
    return render_template('/show_ninja.html', all_ninjas=ninja)







