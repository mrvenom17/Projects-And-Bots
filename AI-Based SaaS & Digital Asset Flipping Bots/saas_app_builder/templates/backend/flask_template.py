from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import sqlite3

app = Flask(__name__)
model = load_model('{{ ai_model_path }}')
conn = sqlite3.connect('{{ database_url }}', check_same_thread=False)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict(data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)