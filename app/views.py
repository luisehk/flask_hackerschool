from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Luis'}

    messages = [
        {
            'author': {'nickname': 'Héctor'},
            'body': 'El día de hoy tenemos clima incierto, como de costumbre.'
        },
        {
            'author': {'nickname': 'Mario'},
            'body': 'La Tierra sigue girando.'
        }
    ]

    return render_template(
        'index.html',
        title='Mi primera aplicación',
        user=user,
        messages=messages
    )
