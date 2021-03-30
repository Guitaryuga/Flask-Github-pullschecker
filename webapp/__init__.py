from flask import Flask, render_template, redirect, request, url_for
from webapp.forms import RequestForm
from webapp.datacollect import CollectingData


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = RequestForm()
        username = form.username.data
        if request.method == 'POST':
            all_data = CollectingData(username)
            return render_template('index.html', form=form, all_data=all_data)
        return render_template('index.html', form=form)

    return app
