from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/add_ninja')
def ninja():
    return render_template("ninjas.html", dojos=Dojo.get_all())

@app.route('/create_ninja', methods=['post'])
def create_ninja():
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['location']
    }
    id=Ninja.create_ninja(data)
    print(id)
    return redirect('/add_ninja')

# @app.route('/show/<id>')
# def show_ninja(id):
#     data={
#         "id": id
#     }
#     return render_template('/show_ninja.html', ninja=Ninja.show_ninja(data))