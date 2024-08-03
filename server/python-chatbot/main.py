from flask import Flask, request, jsonify
from predict import respond

app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt')
    response = respond(prompt)
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
