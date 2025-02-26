# app.py (Flask Dashboard)

from flask import Flask, render_template
import logging

app = Flask(__name__)

@app.route('/')
def dashboard():
    with open('logs/grid_bot.log', 'r') as f:
        logs = f.readlines()[-50:]  # Show last 50 log entries
    return render_template('dashboard.html', logs=logs)

if __name__ == "__main__":
    app.run(debug=True)