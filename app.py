import requests
from datetime import datetime

APP_ID = "you app id"
API_KEY = "you api key"

gender = "male"
weight = 80
height = 160
age = 18


nt_endpoint= "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "your sheet endpoint"

user_query= input("Tell me which exercise you did?:\n")

header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

parameters = {
    "query": user_query,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}

response = requests.post(nt_endpoint, json=parameters, headers=header)
result = response.json()
print(f"Nutrition Api Call: \n{result} \n")

#*********************************************************#

today_date = datetime.now().strftime("%d/%m/%y")
now_time = datetime.now().strftime("%X")

#Bearer Token Authentication
bearer_headers = {
"Authorization": "Bearer qwertyuioasdfghjklzxcvbnm1234567890poiuytrewqasdfghjkl;mnbcxz"
}

for exercise in result['exercises']:
    sheet_input = {
        "workout": {
            "date" : today_date,
            "time" : now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheet_response = requests.post(sheet_endpoint, json= sheet_input, headers= bearer_headers)

    print(sheet_response.text)