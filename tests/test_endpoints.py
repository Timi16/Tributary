import unittest
from app import app

class EndpointTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_record(self):
        response = self.app.post('/record', json={'temperature': 75})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Temperature recorded', response.get_data(as_text=True))

    def test_collect(self):
        self.app.post('/record', json={'temperature': 75})
        response = self.app.get('/collect')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('average_temperature', data)

if __name__ == '__main__':
    unittest.main()
