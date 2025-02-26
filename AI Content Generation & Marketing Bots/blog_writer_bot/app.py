# app.py (Flask Dashboard)

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    articles = pd.read_csv('output/articles.csv')
    return render_template('dashboard.html', articles=articles.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)