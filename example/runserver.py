from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.debug = True
if app.debug:
    from flaskext.clevercss import clevercss
    clevercss(app)

app.run()
