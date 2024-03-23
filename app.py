from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField, IntegerField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = "Password"


class Survey(FlaskForm):
    First_Name = StringField('First Name', validators=[InputRequired()])
    Last_Name = StringField('Last Name', validators=[InputRequired()])
    ID_Number = StringField('Student P Number', validators=[InputRequired()])
    Email = StringField('Mail Address', validators=[InputRequired()])
    Mobile_Number = IntegerField('Mobile Number', validators=[InputRequired()])
    Gender = SelectField('Gender', choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ], validators=[InputRequired()])
    Course=SelectField('Foundation Course', choices=[
        ('FCAH', 'Foundation Certificate for Arts and Humanities'),
        ('FCBSS', 'Foundation Certificate for Business and Social Sciences'),
        ('FCSE', 'Foundation Certificate for Science and Engineering')
    ], validators=[InputRequired()])


@app.route('/')
def homepage():
    return render_template('Welcome Page.html')


@app.route('/Information')
def informationpage():
    return render_template('Information Page.html')


@app.route('/Data Collection', methods=['GET', 'POST'])
def datacollection():
    form = Survey()
    if form.validate_on_submit():
        # Debugging message to check if form validation is successful
        print("Form validation successful")
        with open('feedback.txt', 'a') as file:
            file.write(f"First Name: {form.First_Name.data}\n")
            file.write(f"Last Name: {form.Last_Name.data}\n")
            file.write(f"Student P Number: {form.ID_Number.data}\n")
            file.write(f"Mail Address: {form.Email.data}\n")
            file.write(f"Mobile Number: {form.Mobile_Number.data}\n")
            file.write(f"Gender: {form.Gender.data}\n")
            file.write(f"Foundation Course: {form.Course.data}\n")

            file.write('\n')

            # Debugging message to ensure the redirection is attempted
        print("Redirecting to submitted page")
        return redirect(url_for('successful_submission'))

    # Debugging message to check if form validation fails
    print("Form validation failed")
    return render_template('Data Collection.html', form=form)


@app.route('/submitted')
def successful_submission():
    return 'Your form has been submitted successfully.'


if __name__ == '__main__':
    app.run(debug=True)