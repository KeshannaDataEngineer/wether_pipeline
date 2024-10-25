from flask import Flask, request, jsonify
from fetch_weather import fetch_and_store_weather
from db_config import create_connection

app = Flask(__name__)

@app.route('/fetch_weather', methods=['POST'])
def fetch_weather():
    data = request.get_json()
    venue_id = data.get('venue_id')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    if not venue_id or not start_date or not end_date:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        result = fetch_and_store_weather(venue_id, start_date, end_date)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
