import unittest
import sys
sys.path.append("C:\\Users\\randa\Documents\\restfulBooker\\")
import bookerapi
import requests
import json


class TestBookerAPI(unittest.TestCase):

    def test_token_connection(self, username="admin", password="password123"):
        url = bookerapi.BookerAPI._url('/auth')
        token = requests.post(url, json={
            "username" : username,
            "password" : password
        })

        self.assertEqual(token.status_code, 200)

        print(f'\ntest_token_connection:\nTest passed. Recieved: {token}')
        

    def test_get_token(self):
        token = bookerapi.BookerAPI.get_Token(bookerapi.BookerAPI)
        expected ='7caf06f80b3e295'
        
        
        self.assertEqual(len(token), len(expected))
        print("\ntest_get_token:\nTest: Passed")

    def test_gets_all_IDs(self):
        expected = [{'bookingid': 8}, {'bookingid': 1}, {'bookingid': 2},
        {'bookingid': 4}, {'bookingid': 6}, {'bookingid': 5},
        {'bookingid': 3}, {'bookingid': 10}, {'bookingid': 7}, 
        {'bookingid': 9}]
              
        allIDs = bookerapi.BookerAPI.gets_all_IDs(bookerapi.BookerAPI)
        
        subset = [booking for booking in allIDs if booking in expected]
        self.assertCountEqual(subset,expected)
        print('\ntest_gets_all_IDs:\n Test: Passed.')

    # def test_get_book_by_id(self):
    #     bookbyID = bookerapi.BookerAPI.get_book_by_id(bookerapi.BookerAPI, ID=5)
    #     expected = {
    #         'firstname': 'Mary', 'lastname': 'Jones', 
    #         'totalprice': 675, 'depositpaid': True, 
    #         'bookingdates': {'checkin': '2020-07-04', 
    #         'checkout': '2021-02-02'}}

    #     self.assertDictEqual(bookbyID,expected)
    #     print('\ntest_get_book_by_id:\nTest: Passed')

if __name__ == '__main__':
    unittest.main()