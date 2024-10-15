from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    # Logic to generate or retrieve your data
    data = {
        "version": "1.0",
        "message": "Hello from the API!"
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
