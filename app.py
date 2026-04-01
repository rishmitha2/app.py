from flask import Flask, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"

@app.route('/')
def home():
    return jsonify({"message": "Using JSONPlaceholder API"})

@app.route('/posts')
def posts():
    data = requests.get(f"{BASE_URL}/posts").json()
    return jsonify(data[:5])

@app.route('/comments')
def comments():
    data = requests.get(f"{BASE_URL}/comments").json()
    return jsonify(data[:5])

@app.route('/albums')
def albums():
    data = requests.get(f"{BASE_URL}/albums").json()
    return jsonify(data[:5])

if __name__ == '__main__':
    app.run(debug=True)