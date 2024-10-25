import unittest
from api.app import app

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_fetch_weather_success(self):
        response = self.app.post('/fetch_weather', json={
            "venue_id": 1,
            "start_date": "2024-01-01",
            "end_date": "2024-01-02"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

    def test_fetch_weather_invalid_data(self):
        response = self.app.post('/fetch_weather', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

if __name__ == '__main__':
    unittest.main()
