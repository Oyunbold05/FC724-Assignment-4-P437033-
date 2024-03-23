from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms.validators import InputRequired

app = Flask(__name__)


class Survey(FlaskForm):
    First_Name = StringField('First name', validators=[InputRequired()])
    Last_Name = StringField('Last name', validators=[InputRequired()])
    ID_Number = StringField('ID name', validators=[InputRequired()])


@app.route('/')
def mainpage():
    return render_template('Welcome Page.html')


@app.route('/Welcome Page.html')
def homepage():
    return render_template('Welcome Page.html')


@app.route('/Information Page.html')
def informationpage():
    return render_template('Information Page.html')


@app.route('/Data Collection.html', methods=['GET', 'POST'])
def datacollection():
    return render_template('Data Collection.html')

def feedback():
    form = Survey()
    if form.validate_on_submit():
        with open('feedback.txt', 'a') as file:
            file.write(f"Name: {form.First_Name.data}\n")
            file.write(f"Course: {form.Last_Name.data}\n")
            file.write(f"Short-form Answer: {form.ID_Number.data}\n")

            file.write('\n')
    return render_template('Data Collection.html', form=form)





if __name__ == '__main__':
   app.run(debug = True)