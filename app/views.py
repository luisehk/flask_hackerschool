from flask import render_template
from app import app, db
from app.forms import MessageForm
from app.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    user = {'nickname': 'Luis'}
    form = MessageForm()

    if form.validate_on_submit():
        m = Message(author=form.author.data, body=form.body.data)
        db.session.add(m)
        db.session.commit()

    messages = Message.query.all()

    return render_template(
        'index.html',
        title='Mi primera aplicación',
        user=user,
        messages=messages,
        form=form
    )
