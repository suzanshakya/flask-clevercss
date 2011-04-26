from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

if app.debug:
    import sys
    sys.stdout = sys.stderr
    sys.path.insert(0, '..')
    del sys.modules['flaskext']
    from flaskext.clevercss import clevercss
    clevercss(app)

app.run()
