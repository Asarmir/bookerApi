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
        token = BookerAPI.get_Token(BookerAPI)
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
        cookies = {"token" : token}
       
        return requests.put(BookerAPI._url("/booking/"+str(ID)+"/"), data=json.dumps(payload), headers=header, cookies=cookies).json()

    def delete_booking(self, ID):
        token = BookerAPI.get_Token(BookerAPI)
        return requests.delete(BookerAPI._url(f"/booking/{ID}"), cookies = {"token":token})
         
if __name__ == "__main__":
    # print(BookerAPI.get_Token(BookerAPI))
    # print(BookerAPI.gets_all_IDs(BookerAPI))
    
    # print(BookerAPI.get_book_by_id(BookerAPI, 13))
    
    # print(BookerAPI.get_book_by_name(BookerAPI, "Meral", "Wilke"))
    
    # print(BookerAPI.create_booking(BookerAPI, firstname="Jim", lastname="Brown",totalprice=111, 
    # depositpaid=True, checkin="2018-01-01", checkout="2019-01-01", additionalneeds="Breakfast"))
    
    # print(BookerAPI.update_booking(BookerAPI, ID=13, firstname="THOMAS", lastname="Brown",totalprice=111, 
    # depositpaid=True, checkin="2018-01-01", checkout="2019-01-01", 
    # additionalneeds="Breakfast"))

    # print(BookerAPI.delete_booking(BookerAPI, ID=1))
