import requests
from datetime import datetime
import os

name= os.environ.get("NAME")
Application_ID = os.environ.get("APP_ID")
Application_Keys = os.environ.get("APP_KEY")
SHEETS_ENDPOINT = os.environ.get("SHEET_ENDPOİNT")
headers = {
    "x-app-id": Application_ID,
    "x-app-key": Application_Keys,
}

requirement = {
    "query": input("Tell me, Which exercise you did ? "),
    "gender": "male",
    "weight_kg": 82,
    "height_cm": 170.00,
    "age": 20
}

Nutritionx_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
BAREER = os.environ.get("BAREER")

response = requests.post(Nutritionx_ENDPOINT, headers=headers, json=requirement)
result = response.json()
print(result)


# Adding Rows  in sheety

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


Rows_ENDPINT = os.environ.get("ROWS_ENDPOINT")

headers2 = {
    "email": {
	    f"name": {name},
	    "email": "emirboratasci@gmail.com"
    }
}

for exercise in result["exercises"]:
    sheets_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheets_response = requests.post(SHEETS_ENDPOINT, json=sheets_input).json()
    print(sheets_response)

#  Basic Authorization
    auth_code = os.environ.get("AUTH_CODE")
    sheet_response = requests.post(SHEETS_ENDPOINT, json=sheets_input, auth=(name,auth_code))
    print(sheet_response.text)

# Bareer authorization
    headers4 = {
        "Authorization": f"Bearer {BAREER}"
    }
    barer_auth = requests.post(SHEETS_ENDPOINT, json=sheets_input, headers=headers4).json()