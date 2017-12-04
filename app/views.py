from flask import render_template
from app import app
from app.forms import MessageForm


@app.route('/', methods=['GET', 'POST'])
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

    form = MessageForm()

    if form.validate_on_submit():
        messages.append({
            'author': {'nickname': form.author.data},
            'body': form.body.data
        })

    return render_template(
        'index.html',
        title='Mi primera aplicación',
        user=user,
        messages=messages,
        form=form
    )
