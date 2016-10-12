from flask import Flask
from flask import url_for
from flask import render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'MI-PYT je nejlepší předmět na FITu!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def profile(username):
    return 'User {}'.format(username)

if __name__ == '__main__':
	app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
