from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/dashboard')
def dashboard():
    # Here, you would fetch data from your CSV and pass it to your template
    return render_template('dashboard.html')
