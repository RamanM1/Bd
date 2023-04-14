from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///birthdays.db'
db = SQLAlchemy(app)


# Define a class for the database table
class Birthday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Birthday(name='{self.name}', month={self.month}, day={self.day})>"


# Define the route for adding a new birthday
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data and add new birthday to the database
        name = request.form['name']
        month = int(request.form['month'])
        day = int(request.form['day'])
        new_birthday = Birthday(name=name, month=month, day=day)
        db.session.add(new_birthday)
        db.session.commit()
        return redirect('/')
    else:
        # Retrieve all birthdays from the database and display them on the page
        birthdays = Birthday.query.all()
        return render_template('index.html', birthdays=birthdays)


if name == '__main__':
    app.run(debug=True)
