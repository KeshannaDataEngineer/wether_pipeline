import requests
from db_config import create_connection

def fetch_and_store_weather(venue_id, start_date, end_date):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM venues WHERE id = %s", (venue_id,))
    venue = cursor.fetchone()
    
    if not venue:
        raise ValueError("Venue not found")
    if not start_date or not end_date:
        raise ValueError('')

    lat, lon = venue['latitude'], venue['longitude']
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m,relative_humidity_2m,dewpoint_2m,apparent_temperature,precipitation,rain,showers,snowfall,snow_depth"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch data from API")

    weather_data = response.json().get("hourly", {})

    insert_query = """
        INSERT INTO weather (venue_id, timestamp, temperature, relative_humidity, dewpoint, apparent_temperature, precipitation, rain, showers, snowfall, snow_depth)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        on conflict (venue_id,timestamp)
        do update set temparature=Excluded.temparature,
    """
    
    for i, timestamp in enumerate(weather_data['time']):
        values = (
            venue_id,
            timestamp,
            weather_data['temperature_2m'][i],
            weather_data['relative_humidity_2m'][i],
            weather_data['dewpoint_2m'][i],
            weather_data['apparent_temperature'][i],
            weather_data['precipitation'][i],
            weather_data['rain'][i],
            weather_data['showers'][i],
            weather_data['snowfall'][i],
            weather_data['snow_depth'][i],
        )
        cursor.execute(insert_query, values)
    
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Weather data saved successfully!"}
