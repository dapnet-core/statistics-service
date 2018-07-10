from flask import Flask, jsonify
from flask_restful import Resource, Api
import platform

app = Flask(__name__)
api = Api(app)

class Status(Resource):
    def get(self):
        data = {}
        data['microservice'] = 'statistics'
        data['python_version'] = platform.python_version()
        return (data)

api.add_resource(Status, '/statistics')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

