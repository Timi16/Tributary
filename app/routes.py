from flask import request, jsonify
from app import app, r

@app.route('/record', methods=['POST'])
def record():
    data = request.json
    if 'temperature' not in data:
        return jsonify({'error': 'Temperature is required'}), 400
    temperature = data['temperature']
    r.lpush('temperatures', temperature)
    return jsonify({'status': 'Temperature recorded'}), 200

@app.route('/collect', methods=['GET'])
def collect():
    temperatures = r.lrange('temperatures', 0, -1)
    if not temperatures:
        return jsonify({'error': 'No data available'}), 404
    temperatures = [float(temp) for temp in temperatures]
    average_temp = sum(temperatures) / len(temperatures)
    return jsonify({'average_temperature': average_temp}), 200
