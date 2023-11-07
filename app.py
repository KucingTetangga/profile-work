from flask import Flask, render_template
from flask import request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def halaman_awal():
	return render_template('web.html')

@app.route('/profile/', methods=['GET'])
def profile():
	return render_template('profile.html')

if __name__ == '__main__':
	app.run(debug=True, port=8000, host='0.0.0.0')
