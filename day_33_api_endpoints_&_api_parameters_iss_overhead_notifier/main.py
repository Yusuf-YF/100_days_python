import requests
from datetime import datetime

# response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
#
# iss_position = (latitude, longitude)
# print(iss_position)

LAT = 24.713552
LNG = 46.675297

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunrise.split("T")[1].split(":")[0])
print(sunset)

time_now = datetime.now()
print(time_now.hour)
