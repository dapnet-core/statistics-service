from flask import Flask, jsonify
#from flask_restful import Resource, Api
import platform

app = Flask(__name__)

@app.route('/statistics')
def api_statistics():
    data = {}
    data['microservice'] = 'statistics'
    data['python_version'] = platform.python_version()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

