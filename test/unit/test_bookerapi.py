import unittest
import sys
sys.path.append("C:\\Users\\randa\Documents\\restfulBooker\\")
import bookerapi
import requests
import json


class TestBookerAPI(unittest.TestCase):

    def test_token_connection(self):
        payload = {
            "username" : "admin",
            "password" : "password123"
        }

        headers = {'content-Type' : 'application/json'}

        authURL = "/auth"
        res = requests.post(bookerapi.BookerAPI.CONSTURL+authURL, data=json.dumps(payload), headers=headers)
       
        self.assertEqual(res.status_code, 200)
        print(f"Test Response: {res}: Pass")
        print('Test Completed\n')

    def test_create_token(self):
        token = bookerapi.BookerAPI.createToken(bookerapi.BookerAPI)
        expected = {'token': 'f6bca255a383085'}
        
        
        self.assertEqual(len(token), len(expected))
        print("Test token is same length: Pass")
        print('Test Completed\n')

if __name__ == '__main__':
    unittest.main()

# Idea to help with figuring out the api.
