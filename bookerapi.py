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
        bookIDs = BookerAPI.gets_all_IDs(self)
        for id in bookIDs:
            for key, value in id.items():
                if value == ID:
                    print(f"\nFound: {key} {value}")

if __name__ == "__main__":
    # CreateToken.createToken(CreateToken)
    #BookerAPI.get_book_by_id(BookerAPI, 7)