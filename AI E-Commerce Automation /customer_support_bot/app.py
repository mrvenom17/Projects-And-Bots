# app.py (Flask Chat Interface)

from flask import Flask, request, jsonify
from chatbot import generate_response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query')
    response = generate_response(query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)