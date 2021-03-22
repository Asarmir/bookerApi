import requests
import json

class BookerAPI:

    def _url(path):
        return "https://restful-booker.herokuapp.com" + path

    def get_Token(self, username="admin", password="password123"):
        url = BookerAPI._url('/auth')
        return requests.post(url, json={
            "username" : username,
            "password" : password
        }).json()['token']
      

    def gets_all_IDs(self):
        url = BookerAPI._url("/booking")
        return requests.get(url).json()

    def get_book_by_id(self, ID):
       url = BookerAPI._url(f"/booking/{str(ID)}")
       return requests.get(url).json()
      

    def get_book_by_name(self, firstname, lastname):
        url = BookerAPI._url(f"/booking?firstname={firstname}&lastname={lastname}")
        return requests.get(url).json()

    def create_booking(self, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
        url = BookerAPI._url("/booking")
        header = {'Content-Type': 'application/json'}
        payload = {
            "firstname" : firstname,
            "lastname" : lastname,
            "totalprice" : totalprice,
            "depositpaid" : depositpaid,
            "bookingdates" : {
                "checkin" : checkin,
                "checkout" : checkout
            },
            "additionalneeds" : additionalneeds
        }
        print("Creating new Booking.")
        return requests.post(url, data=json.dumps(payload), headers=header).json()

    def update_booking(self, ID, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
        pass

if __name__ == "__main__":
    # BookerAPI.get_Token(BookerAPI)
    # BookerAPI.gets_all_IDs(BookerAPI)
    
    # print(BookerAPI.get_book_by_id(BookerAPI, 8))
    
    # print(BookerAPI.get_book_by_name(BookerAPI, "Mary", "Ericsson"))
    
    print(BookerAPI.create_booking(BookerAPI, firstname="Jim", lastname="Brown",totalprice=111, 
    depositpaid=True, checkin="2018-01-01", checkout="2019-01-01", additionalneeds="Breakfast"))
    
    # BookerAPI.update_booking(BookerAPI, ID=13, firstname="James", lastname="Brown",totalprice=111, 
    # depositpaid=True, checkin="2018-01-01", checkout="2019-01-01", 
    # additionalneeds="Breakfast")