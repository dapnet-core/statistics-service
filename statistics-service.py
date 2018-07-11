from flask import Flask, jsonify
import platform
import requests

# Edit in final deploy
CouchDB_Stat_users_URL = 'http://dapnetdc1.db0sda.ampr.org:5984/users'
CouchDB_Stat_transmitters_URL = 'http://dapnetdc1.db0sda.ampr.org:5984/transmitters'


app = Flask(__name__)

@app.route('/statistics/info')
def api_statistics_info():
    data = {}
    data['version'] = '0.0.4'
    data['python_version'] = platform.python_version()
    data['microservice'] = 'statistics'
    return jsonify(data)


@app.route('/statistics')
def api_statistics():
    data = {}

# Get total users
    response = requests.get(url=CouchDB_Stat_users_URL)
    if response.status_code == 200:
        response_data = response.json()
        data['users'] = response_data['doc_count']
    else:
        data['users'] = -1

#Get total transmitters
    data['transmitters'] = {}
#Widerange
    data['transmitters']['widerange'] = {}
    response = requests.get(url=CouchDB_Stat_transmitters_URL + '_design/docs/_view/countwiderangetotal')
    if response.status_code == 200:
        response_data = response.json()
#No idea how the output of the view looks like
        data['transmitters']['widerange']['total'] = 11
    else:
        data['transmitters']['widerange']['total'] = -1

#Get total widerange transmitters
    data['transmitters']['personal'] = {}
    response = requests.get(url=CouchDB_Stat_transmitters_URL + '_design/docs/_view/countpersonaltotal')
    if response.status_code == 200:
        response_data = response.json()
#No idea how the output of the view looks like
        data['transmitters']['personal']['total'] = 11
    else:
        data['transmitters']['personal']['total'] = -1
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

