from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/profile', methods=['GET'])
def profile():
    data = {
        "name": "John Doe",
        "about": "A full stack developer who loves Python and JavaScript"
    }
    return jsonify(data)
