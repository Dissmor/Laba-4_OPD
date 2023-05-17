import unittest
import requests

class Test(unittest.TestCase):
    def test_upload_file(self):
        url = "http://127.0.0.1:5000"
        file_path = "testing/test.txt"
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, files=files)
        self.assertEqual(response.status_code, 200)