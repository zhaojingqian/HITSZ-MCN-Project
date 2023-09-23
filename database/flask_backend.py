from flask import Flask
from flask import request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def test_ping():
    app.logger.info("Ping Success")
    return "Ping Success"

if __name__ == '__main__':
    app.run(port=8280, debug=True)