import os
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({
        "version": "1.0",
        "message": "Hello from the API!"
    })


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
