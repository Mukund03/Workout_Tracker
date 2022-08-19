import requests
import json
from _datetime import datetime

APP_ID ="5aec5fde"
API_KEY = "422283d484876f13da45229f1ec0b3ba"


GENDER = "FEMALE"
WEIGHT_KG = 68
HEIGHT_CM = 157
AGE = 29

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/e4fb6d744b386234cb3fcb6eb0e91d63/myWorkoutsProject/workouts"


Headers = {
  "x-app-id": APP_ID,
  "x-app-key": API_KEY,
  "content-Type": "application/json"
}


bearer_headers = {
    "Authorization": "Bearer qwertyuiop"
}

user_input = input("Tell me which exercises you did. ")

query = {
  "query": user_input,
  "gender": GENDER,
  "weight_kg": WEIGHT_KG,
  "height_cm": HEIGHT_CM,
  "age": AGE
}

response = requests.post(url=exercise_endpoint, json=query,
                         headers=Headers)
result = json.loads(response.text)
new_string = json.dumps(result, indent=2)
print(new_string)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
