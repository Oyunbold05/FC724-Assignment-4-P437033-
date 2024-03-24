from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField, IntegerField
from wtforms.validators import InputRequired

app = Flask(__name__)
# Secret key for security measure.
app.secret_key = "Password"


# Creating class for Form which is posted on the webpage and receives input from user.
class Survey(FlaskForm):
    # String and Integer fields for personal details.
    First_Name = StringField('First Name', validators=[InputRequired()])
    Last_Name = StringField('Last Name', validators=[InputRequired()])
    ID_Number = StringField('Student P Number', validators=[InputRequired()])
    Email = StringField('Mail Address', validators=[InputRequired()])
    Mobile_Number = IntegerField('Mobile Number', validators=[InputRequired()])

    # Selection field for gender selection and course selection.
    Gender = SelectField('Gender', choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ], validators=[InputRequired()])

    Course = SelectField('Foundation Course', choices=[
        ('FC for Arts and Humanities', 'Foundation Certificate for Arts and Humanities'),
        ('FC for Business and Social Sciences', 'Foundation Certificate for Business and Social Sciences'),
        ('FC for Science and Engineering', 'Foundation Certificate for Science and Engineering')
    ], validators=[InputRequired()])

    # Choice values for question section
    good_or_bad_choices = [('Very Good', 'Very Good'),
        ('Good', 'Good'),
        ('Neutral', 'Neutral'),
        ('Bad', 'Bad'),
        ('Very Bad', 'Very Bad')
    ]

    satisfied_or_unsatisfied_choices = [('Very Satisfied', 'Very Satisfied'),
        ('Satisfied', 'Satisfied'),
        ('Neutral', 'Neutral'),
        ('Unsatisfied', 'Unsatisfied'),
        ('Very Unsatisfied', 'Very Unsatisfied')
    ]
    between_1_and_5_scale_choice = [('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1')
    ]

    # Radio fields for question section.
    Question_1 = RadioField('How would you rate your overall academic experience at Glasgow International College (GIC)?', choices=good_or_bad_choices,
                            validators=[InputRequired()])
    Question_2 = RadioField('How would you describe the effectiveness of learning resources, such as libraries, labs, and online materials at GIC?', choices=good_or_bad_choices,
                            validators=[InputRequired()])
    Question_3 = RadioField('How satisfied are you with the academic courses offered at GIC in terms of content, structure, and delivery?', choices=satisfied_or_unsatisfied_choices,
                            validators=[InputRequired()])
    Question_4 = RadioField('How satisfied are you with the quality of teaching and support provided by faculty members at GIC?', choices=satisfied_or_unsatisfied_choices,
                            validators=[InputRequired()])
    Question_5 = RadioField('To what extent do you believe GIC has prepared you for further academic studies at the university level or in your chosen field? (Rate from 1(Not prepared) to 5(Prepared))', choices=between_1_and_5_scale_choice,
                            validators=[InputRequired()])

    Suggestions = TextAreaField('What suggestions do you have for enhancing the overall academic experience for students at GIC?')


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
        # Creating txt file and appending inputs given in the form.
        with open('feedback.txt', 'a') as file:
            file.write(f"First Name: {form.First_Name.data}\n")
            file.write(f"Last Name: {form.Last_Name.data}\n")
            file.write(f"Student P Number: {form.ID_Number.data}\n")
            file.write(f"Mail Address: {form.Email.data}\n")
            file.write(f"Mobile Number: {form.Mobile_Number.data}\n")
            file.write(f"Gender: {form.Gender.data}\n")
            file.write(f"Question 1 answer: {form.Question_1.data}\n")
            file.write(f"Question 2 answer: {form.Question_2.data}\n")
            file.write(f"Question 3 answer: {form.Question_3.data}\n")
            file.write(f"Question 4 answer: {form.Question_4.data}\n")
            file.write(f"Question 5 answer: {form.Question_5.data}\n")
            if form.Suggestions:
                file.write(f"Suggestions and feedback: {form.Suggestions.data}\n")

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