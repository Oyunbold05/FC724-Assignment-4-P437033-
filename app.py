from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def mainpage():
    return render_template('Welcome Page.html')


@app.route('/Welcome Page.html')
def homepage():
    return render_template('Welcome Page.html')


@app.route('/Information Page.html')
def informationpage():
    return render_template('Information Page.html')


@app.route('/Data Collection.html', methods=['GET'])
def datacollection():
    return render_template('Data Collection.html')


if __name__ == '__main__':
   app.run(debug = True)