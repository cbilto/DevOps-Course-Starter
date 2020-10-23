import flask
from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/')
def index():
    # return 'Hello World!'
    items = session.get_items()
    return render_template("index.html", items=items)

@app.route('/', methods=['POST'])
def add():
   session.add_item(request.form.get('input_title'))
   return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
