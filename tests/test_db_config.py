import unittest
from api.db_config import create_connection

class TestDBConnection(unittest.TestCase):
    def test_connection(self):
        connection = create_connection()
        self.assertIsNotNone(connection)
        connection.close()

if __name__ == '__main__':
    unittest.main()
