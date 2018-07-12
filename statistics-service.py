from flask import Flask, jsonify
import platform
import requests

# Edit in final deploy
CouchDB_Stat_users_URL = 'http://dapnetdc1.db0sda.ampr.org:5984/users'
CouchDB_Stat_transmitters_URL = 'http://dapnetdc1.db0sda.ampr.org:5984/transmitters/_design/statistics/_view/count?group_level=1'


app = Flask(__name__)

@app.route('/statistics/info')
def api_statistics_info():
    data = {}
    data['version'] = '0.0.6'
    data['python_version'] = platform.python_version()
    data['microservice'] = 'statistics'
    return jsonify(data)


@app.route('/statistics')
def api_statistics():
    data = {}

# Get total users
    response = requests.get(url=CouchDB_Stat_users_URL,
                            headers={'Cache-Control': 'no-cache'})
    if response.status_code == 200:
        response_data = response.json()
        data['users'] = response_data['doc_count']
    else:
        data['users'] = -1

#Get total transmitters
    data['transmitters'] = {}
    data['transmitters']['widerange'] = {}
    data['transmitters']['personal'] = {}

    response = requests.get(url=CouchDB_Stat_transmitters_URL,
                            headers={'Cache-Control': 'no-cache'})
    if response.status_code == 200:
        response_data = response.json()
        for row in response_data['rows']:
            if row['key'] == 'PERSONAL':
                data['transmitters']['personal']['total'] = row['value']
            elif row['key'] == 'WIDERANGE':
                data['transmitters']['widerange']['total'] = row['value']

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
