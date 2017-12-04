from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Luis'}
    return render_template(
        'index.html',
        title='Tu nueva aplicación',
        user=user
    )
