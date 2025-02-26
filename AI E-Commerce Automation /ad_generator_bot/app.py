# app.py (Flask Dashboard)

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    ads = pd.read_csv('output/ads.csv')
    return render_template('dashboard.html', ads=ads.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)