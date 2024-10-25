import unittest
from api.fetch_weather import fetch_and_store_weather

class TestFetchWeather(unittest.TestCase):
    def test_fetch_weather_invalid_venue(self):
        with self.assertRaises(ValueError):
            fetch_and_store_weather(999, "2024-01-01", "2024-01-02")  

if __name__ == '__main__':
    unittest.main()
