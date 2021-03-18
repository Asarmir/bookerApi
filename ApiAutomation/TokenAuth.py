import requests
import json

CONSTURL = "https://restful-booker.herokuapp.com"
headers = {'content-Type' : 'application/json'}

payload = {
    "username" : "admin",
    "password" : "password123"
}

def createToken():
    authURL = "/auth"
    print("Getting a Token from the Token Jar!")
    res = requests.post(CONSTURL+authURL, data=json.dumps(payload), headers=headers)
    token = json.loads(res.text)
    print(f'{res}\n{token}')
    return token

createToken()