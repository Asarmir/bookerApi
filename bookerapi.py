import requests
import json

class BookerAPI:

    CONSTURL = "https://restful-booker.herokuapp.com"

    def createToken(self):
        payload = {
            "username" : "admin",
            "password" : "password123"
        }

        headers = {'content-Type' : 'application/json'}

        authURL = "/auth"
        print("Getting a Token from the Token Jar!")
        res = requests.post(self.CONSTURL+authURL, data=json.dumps(payload), headers=headers)
        token = json.loads(res.text)
        print(f'{res}\n{token}')
        return token

    def gets_all_IDs(self):
        booking = "/booking"
        r = requests.get(self.CONSTURL+booking)
        bookid = json.loads(r.text)
        print(f"{r}\n{bookid}")
        return bookid

    def get_book_by_id(self, ID):
       booking = "/booking/"
       r = requests.get(self.CONSTURL+booking+str(ID))
       print(r.text)

    def get_book_by_name(self, firstname, lastname):
        booking = "/booking?"
        firstname = "firstname="+ firstname
        lastname = "&lastname=" + lastname
        r = requests.get(self.CONSTURL+booking+firstname+lastname)
        print(r.text)
    
if __name__ == "__main__":
    # BookerAPI.createToken(BookerAPI)
    # BookerAPI.get_book_by_id(BookerAPI, 10)
    # BookerAPI.get_book_by_name(BookerAPI, "Sally", "Brown")