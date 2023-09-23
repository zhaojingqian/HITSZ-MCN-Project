from flask import Flask
from flask import request, make_response
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

ROOT_PATH = 'database/data'

@app.route('/test', methods=['GET'])
def test_ping():
    app.logger.info("Ping Success")
    return "Ping Success"

@app.route('/get_data_list', methods=['GET'])
def get_data_list():
    file_names = []
    for root, dirs, files in os.walk(ROOT_PATH):
        for file in files:
            file_names.append(file.split('.')[0])
    return file_names

@app.route('/upload', methods=['POST', 'OPTIONS'])
def save_file():
    if request.method == 'OPTIONS':  # 处理OPTIONS请求
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
    file = request.files['file']
    file_name = file.filename
    file.save(os.path.join(ROOT_PATH, file_name))
    return "success"


if __name__ == '__main__':
    app.run(port=8280, debug=True)